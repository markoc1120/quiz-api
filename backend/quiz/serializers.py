from rest_framework import serializers
from .models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'text',
        ]


class QuestionSerializer(serializers.ModelSerializer):
    choices = AnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = [
            'id',
            'question',
            'answer',
            'choices',
        ]
        depth = 1

