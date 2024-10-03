# feelback/api_urls.py
from django.urls import path
from .views_api import (
    CustomerList, DelivererList, PackageList, DeliveryList,
    FormList, QuestionList, FormQuestionList, AnswerStatsList, FormQuestionCreate
)

urlpatterns = [
    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('deliverers/', DelivererList.as_view(), name='deliverer-list'),
    path('packages/', PackageList.as_view(), name='package-list'),
    path('deliveries/', DeliveryList.as_view(), name='delivery-list'),
    path('forms/', FormList.as_view(), name='form-list'),
    path('questions/', QuestionList.as_view(), name='question-list'),
    path('form-questions/', FormQuestionList.as_view(), name='form-question-list'),
    path('answer-stats/', AnswerStatsList.as_view(), name='answer-stats-list'),
    path('create-answer/', FormQuestionCreate.as_view(), name='create-answer')


]
