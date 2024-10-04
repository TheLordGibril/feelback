# feelback/views_api.py
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from .models import Customer, Deliverer, Package, Delivery, Form, Question, FormQuestion
from .serializers import (
    CustomerSerializer, DelivererSerializer, PackageSerializer,
    DeliverySerializer, FormSerializer, QuestionSerializer, FormQuestionSerializer, FormQuestionCreateSerializer
)
from .utils import get_feedback_stats
from rest_framework.response import Response


# ListAPIView => retourne une liste de ce qu'on lui donne (ici query permet de définir les objets retourné (TOUS) 
# CustomerSerialize serialize les objets récupéré
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

# FormQuestionCreate crée des réponses a des questions dans un formulaire

class FormQuestionCreate(APIView):
    #args pour passer un argument
    #kwargs (keyword args pour passer une liste d'arguments)
    def post(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = FormQuestionCreateSerializer(
                data=request.data, many=True) #many = True permet de prendre plusieurs objet

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Une liste d'objets est attendue."}, status=status.HTTP_400_BAD_REQUEST)


class AnswerStatsList(APIView):
    def get(self, request):
        stats = get_feedback_stats()
        return Response(stats)
