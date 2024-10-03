from django.db.models import Avg, Count
from .models import FormQuestion


def get_feedback_stats():
    stats = FormQuestion.objects.values('form_id', 'question_id').annotate(
        nb_people=Count('customer_id', distinct=True), # * Distinct permet de ne pas recompter
        avg_answer=Avg('answer')
    )
    return stats