from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=1)
    zip_code = models.CharField(max_length=10)
    town = models.CharField(max_length=20)
    country = models.CharField(max_length=20) 
    
    def __str__(self):
        return 

    def __unicode__(self):
        return 

class Package(models.Model):
    STATE = ['Excellent, Très bon état, Bon état, État correct, Endommagé , Inutilisable']
    departure_state = models.CharField(choices=STATE)
    arival_state = models.CharField(choices=STATE)
    weight = models.FloatField()
    fragile = models.BooleanField()

    def __str__(self):
        return 

    def __unicode__(self):
        return 

class Deliverer(models.Model):
    name = models.CharField(max_length="50")
    surname = models.CharField(max_length="50")
    phone_number = models.CharField(max_length="50")

    def __str__(self):
        return 

    def __unicode__(self):
        return 

class Delivery(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    deliverer = models.ForeignKey(Deliverer, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 

class Feedback(models.Model):
    STATE = ['Excellent, Très bon état, Bon état, État correct, Endommagé , Inutilisable']
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    delays_rate = models.IntegerField()
    state_rate =  models.CharField(choices=STATE)
    behaviour_rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    edited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 

    def __unicode__(self):
        return 
