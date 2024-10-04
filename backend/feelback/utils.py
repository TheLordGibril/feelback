from django.db.models import Avg, Count
from .models import FormQuestion


def get_feedback_stats():
    stats = FormQuestion.objects.values('form_id', 'question_id').annotate(
        # On compte la soumission d'un form et non le nombre de question de ce formulaire
        nb_submissions=Count('created_at', distinct=True),
        avg_answer=Avg('answer')
    )
    return stats