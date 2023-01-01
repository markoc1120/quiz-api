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
            'choices'
        ]
        read_only_fields = ('answer',)
        depth = 1

    # def create(self, validated_data):
    #     answers_data = validated_data.pop('answers')
    #     question = Question.objects.create(**validated_data)
    #     for answer_data in answers_data:
    #         Answer.objects.create(**answer_data)
    #     return question
