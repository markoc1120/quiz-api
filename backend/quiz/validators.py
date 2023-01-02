from rest_framework.validators import UniqueValidator
from .models import Question

unique_question_title = UniqueValidator(queryset=Question.objects.all(), lookup='iexact')
