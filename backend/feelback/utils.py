from django.db.models import Avg, Count
from .models import FormQuestion


def get_feedback_stats():
    # values permet de récupéré uniquement certain champs et non l'ensemble du model
    # annotate permet d'ajouter des champs selon les values indiqués (ici on ajoute deux nouveau champs nb_submissions et avg_answers)
    stats = FormQuestion.objects.values('form_id', 'question_id').annotate(
        # On compte la soumission d'un form et non le nombre de question de ce formulaire
        nb_submissions=Count('created_at', distinct=True),
        avg_answer=Avg('answer')
    )
    return stats