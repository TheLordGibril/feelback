# feelback/serializers.py
from rest_framework import serializers
from .models import Customer, Deliverer, Package, Delivery, Form, Question, FormQuestion

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class DelivererSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliverer
        fields = '__all__'

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

class DeliverySerializer(serializers.ModelSerializer):
    package = PackageSerializer()
    customer = CustomerSerializer()
    deliverer = DelivererSerializer()

    class Meta:
        model = Delivery
        fields = '__all__'

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class FormQuestionSerializer(serializers.ModelSerializer):
    form = FormSerializer()
    question = QuestionSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = FormQuestion
        fields = '__all__'
