from django.core.management.base import BaseCommand
from feelback.models import Customer, Package, Deliverer, Delivery, Feedback
from faker import Faker
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Generate fake data for testing'

    def handle(self, *args, **kwargs):
        fake = Faker('fr_FR')  # Utiliser Faker en français si nécessaire

        # Générer des clients fictifs
        for _ in range(10):  # Générer 10 clients
            Customer.objects.create(
                name=fake.first_name(),
                surname=fake.last_name(),
                phone_number=fake.phone_number(),
                email=fake.email(),
                address=fake.street_address(),
                zip_code=fake.postcode(),
                town=fake.city(),
                country=fake.country()
            )
        
        # Générer des livreurs fictifs
        for _ in range(5):  # Générer 5 livreurs
            Deliverer.objects.create(
                name=fake.first_name(),
                surname=fake.last_name(),
                phone_number=fake.phone_number(),
            )

        # Générer des colis fictifs
        for _ in range(10):  # Générer 10 colis
            Package.objects.create(
                departure_state=random.choice(Package.STATE)[0],  # Choisir un état de départ aléatoire
                arival_state=random.choice(Package.STATE)[0],  # Choisir un état d'arrivée aléatoire
                weight=round(random.uniform(0.5, 50.0), 2),  # Poids entre 0.5 et 50 kg
                fragile=random.choice([True, False])
            )

        # Générer des livraisons fictives
        customers = list(Customer.objects.all())
        deliverers = list(Deliverer.objects.all())
        packages = list(Package.objects.all())

        for _ in range(10):  # Générer 10 livraisons
            scheduled_time = fake.date_time_this_year(before_now=False, after_now=True)
            arrival_time = scheduled_time + timedelta(hours=random.randint(1, 24))

            Delivery.objects.create(
                package=random.choice(packages),
                customer=random.choice(customers),
                deliverer=random.choice(deliverers),
                scheduled_time=scheduled_time,
                arrival_time=arrival_time
            )

        # Générer des feedbacks fictifs
        deliveries = list(Delivery.objects.all())
        for _ in range(10):  # Générer 10 feedbacks
            Feedback.objects.create(
                delivery=random.choice(deliveries),
                delays_rate=random.randint(1, 5),  # Note de retard entre 1 et 5
                state_rate=random.choice(Feedback.STATE)[0],  # Choisir un état de colis
                behaviour_rate=random.randint(1, 5),  # Note de comportement entre 1 et 5
                created_at=fake.date_time_this_year(before_now=True, after_now=False),
            )

        self.stdout.write(self.style.SUCCESS('Données fictives générées avec succès !'))
