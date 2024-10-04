# feelback/serializers.py
from rest_framework import serializers
from .models import Customer, Deliverer, Package, Delivery, Form, Question, FormQuestion
from .models import FormQuestion, Form, Question

# Serializers pour convertir des objets Python complexes
# en types de données simples comme des JSON, et inversement.


class CustomerSerializer(serializers.ModelSerializer): #CustomerSerializer Sérialise le modèle Customer
    class Meta: #Meta : Définit le modèle associé et les champs à inclure.
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

# Explication d'un Serializer avec relation

# PackageSerializer, CustomerSerializer, DelivererSerializer
# sont imbriqués à l'intérieur du DeliverySerializer pour permettre la sérialisation de ces relations.
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


class FormQuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormQuestion
        fields = ['form', 'question', 'answer', 'customer']
        
    # Validate permet de vérifié ldes données soumises avant traitement
    def validate(self, data):
        form = data.get('form')

        if not form:
            raise serializers.ValidationError("Le formulaire est obligatoire.")

        # Récupérer toutes les questions soumises pour détecter des doublons
        question_ids = [item.get('question') for item in self.initial_data]

        # Vérifier qu'il n'y a pas de questions dupliquées dans la même soumission
        if len(question_ids) != len(set(question_ids)):
            raise serializers.ValidationError("Une même question ne peut pas être répondue plusieurs fois dans la même soumission.")

        # Vérifier que l'utilisateur a fourni le bon nombre de réponses
        total_questions = Question.objects.filter(formquestion__form=form).distinct().count()
        if total_questions != len(self.initial_data):
            raise serializers.ValidationError(f"Il y a {total_questions} questions dans ce formulaire, mais seulement {len(self.initial_data)} réponses soumises.")

        return data
        # ! A ajouter quand on pourra crée des users etc
        # # Vérifier qu'aucune des questions n'a déjà été répondue par ce client
        # for answer_data in self.initial_data:
        #     question_id = answer_data.get('question')

        #     # Vérifier si la question appartient bien au formulaire
        #     if not Question.objects.filter(id=question_id, formquestion__form=form).exists():
        #         raise serializers.ValidationError(f"Invalid question pk '{question_id}' for this form.")
            
        #     # Vérifier si l'utilisateur a déjà répondu à cette question
        #     if FormQuestion.objects.filter(form=form, question_id=question_id, customer=customer).exists():
        #         raise serializers.ValidationError(f"La question '{question_id}' a déjà une réponse pour ce formulaire et client.")
        
