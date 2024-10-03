from django.core.management.base import BaseCommand
import random
from faker import Faker
from feelback.models import Customer, Deliverer, Package, Delivery, Form, Question, FormQuestion

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with fake data'

    def handle(self, *args, **kwargs):
        self.populate()

    def populate(self):
        self.create_deliverers(5)           # Crée 5 livreurs
        self.create_customers(20)           # Crée 20 clients
        self.create_packages(20)            # Crée 20 colis
        self.create_deliveries()            # Crée des livraisons pour chaque client avec un colis et un livreur
        form, questions = self.create_single_form_and_questions()  # Crée 1 formulaire et ses questions
        self.create_form_responses_for_all_customers(form, questions)  # Crée des réponses pour tous les clients
        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))

    def create_deliverers(self, n):
        """ Crée 5 livreurs fictifs """
        for _ in range(n):
            deliverer = Deliverer(
                name=fake.first_name(),
                last_name=fake.last_name(),
                phone_number=fake.phone_number(),
                email=fake.email()
            )
            deliverer.save()
        self.stdout.write(f"{n} deliverers created.")

    def create_customers(self, n):
        """ Crée 20 clients fictifs """
        for _ in range(n):
            customer = Customer(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone_number=fake.phone_number(),
                email=fake.email(),
                lane_number=fake.street_address(),
                address=fake.address(),
                zip_code=fake.zipcode(),
                town=fake.city(),
                country=fake.country()
            )
            customer.save()
        self.stdout.write(f"{n} customers created.")

    def create_packages(self, n):
        """ Crée 20 colis fictifs """
        states = ['EXCELLENT', 'TRES_BON_ETAT', 'ETAT_CORRECT', 'ENDOMMAGE', 'TRES_ENDOMMAGE']
        for _ in range(n):
            package = Package(
                departure_state=random.choice(states),
                arrival_state=random.choice(states),
                weight=random.uniform(0.5, 10.0),  # Poids entre 0.5 et 10kg
                fragile=random.choice([True, False])
            )
            package.save()
        self.stdout.write(f"{n} packages created.")

    def create_deliveries(self):
        """ Associe chaque client à une livraison avec un colis et un livreur """
        customers = Customer.objects.all()
        deliverers = Deliverer.objects.all()
        packages = Package.objects.all()

        for customer in customers:
            delivery = Delivery(
                package=random.choice(packages),
                customer=customer,
                deliverer=random.choice(deliverers),
                scheduled_time=fake.date_time_between(start_date='-30d', end_date='now'),
                arrival_time=fake.date_time_between(start_date='now', end_date='+30d')
            )
            delivery.save()
        self.stdout.write("Deliveries created for all customers.")

    def create_single_form_and_questions(self):
        """ Crée un seul formulaire avec 3 questions """
        form = Form(title="Feedback sur la livraison")
        form.save()

        # Les 3 questions
        questions_text = [
            "Évaluer de 1 à 5 le respect du délai de livraison",
            "Évaluer de 1 à 5 l’état de votre colis à sa réception",
            "Évaluer de 1 à 5 le comportement du livreur"
        ]
        
        questions = []
        for question_text in questions_text:
            question = Question(title=question_text)
            question.save()
            questions.append(question)
        
        self.stdout.write("Form and questions created.")
        return form, questions

    def create_form_responses_for_all_customers(self, form, questions):
        """ Associe le formulaire à chaque client et génère des réponses pour chaque question """
        customers = Customer.objects.all()

        for customer in customers:
            for question in questions:
                answer = random.randint(1, 5)  # Réponse aléatoire entre 1 et 5
                form_question = FormQuestion(
                    form=form,
                    question=question,
                    answer=answer,
                    customer=customer,
                    created_at=fake.date_time_between(start_date='-30d', end_date='now'),
                    updated_at=fake.date_time_between(start_date='-30d', end_date='now')
                )
                form_question.save()
        
        self.stdout.write(f"Form questions filled for all {len(customers)} customers.")