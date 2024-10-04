from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#Max et minValue Permettent de limiter les valeurs possible entre 1 et 5

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    lane_number = models.CharField(max_length=255)
    address = models.TextField() # TODO a modifier en charfield (TextField conçu pour long paragraphe)
    zip_code = models.CharField(max_length=20)
    town = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    #  __str__ Permet de retourner une réprésentation lisible de l'objet mais non nécéssaire dans notre cas
    def __str__(self):
        return ""


class Deliverer(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return ""


class Package(models.Model):
    STATES = [
        ('EXCELLENT', 'Excellent'),
        ('TRES_BON_ETAT', 'Très bon état'),
        ('ETAT_CORRECT', 'État correct'),
        ('ENDOMMAGE', 'Endommagé'),
        ('TRES_ENDOMMAGE', 'Très endommagé')
    ]
    departure_state = models.CharField(max_length=14, choices=STATES)
    arrival_state = models.CharField(max_length=14, choices=STATES)
    weight = models.FloatField()
    fragile = models.BooleanField(default=False)

    def __str__(self):
        return ""


class Delivery(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    deliverer = models.ForeignKey(Deliverer, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return ""


class Form(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return ""


class Question(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return ""


class FormQuestion(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField(
        validators=[
            MaxValueValidator(5), MinValueValidator(1)] #Ici on a un validators qui vérifie les entrés saisies en BDD pour plus de robustesse
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return ""
