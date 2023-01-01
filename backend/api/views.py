from quiz.models import Question

from rest_framework.decorators import api_view
from rest_framework.response import Response
from quiz.serializers import QuestionSerializer


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    """
    DRF API view
    """
    instance = Question.objects.all().order_by('?').first()
    data = {}
    if instance:
        #data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
        data = QuestionSerializer(instance).data
    return Response(data)
