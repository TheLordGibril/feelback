# feelback/views_api.py
from rest_framework import generics
from rest_framework.views import APIView
from .models import Customer, Deliverer, Package, Delivery, Form, Question, FormQuestion
from .serializers import (
    CustomerSerializer, DelivererSerializer, PackageSerializer,
    DeliverySerializer, FormSerializer, QuestionSerializer, FormQuestionSerializer
)
from .utils import get_feedback_stats
from rest_framework.response import Response

class CustomerList(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class DelivererList(generics.ListAPIView):
    queryset = Deliverer.objects.all()
    serializer_class = DelivererSerializer

class PackageList(generics.ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class DeliveryList(generics.ListAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class FormList(generics.ListAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class FormQuestionList(generics.ListAPIView):
    queryset = FormQuestion.objects.all()
    serializer_class = FormQuestionSerializer

class AnswerStatsList(APIView):
    def get(self, request):
        stats = get_feedback_stats()
        return Response(stats)