from quiz.models import Quiz

from rest_framework.decorators import api_view
from rest_framework.response import Response
from quiz.serializers import QuizSerializer


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    """
    DRF API view
    """
    instance = Quiz.objects.all().order_by('?').first()
    data = {}
    if instance:
        #data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
        data = QuizSerializer(instance).data
    return Response(data)
