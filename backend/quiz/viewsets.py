from rest_framework import viewsets, serializers
from rest_framework.response import Response

from .models import Answer, Question
from .serializers import AnswerSerializer, QuestionSerializer
from drf_spectacular.utils import extend_schema, OpenApiExample

descr = '{"question": "Question", "answer": "Correct answer", "choices": [{"text": "Other answer"}, {"text": "Other answer"}, {"text": "Other answer"}]}'


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


    def get_queryset(self):
        question = Question.objects.all()
        return question

    @extend_schema(
        # attach request/response examples to the operation.
        examples=[
            OpenApiExample(
                'Query 1',
                value=descr
            ),
        ],
    )
    def create(self, request, *args, **kwargs):
        data = request.data
        correct_answer = data['answer']

        new_correct_answer = Answer.objects.get_or_create(text=correct_answer)

        if Question.objects.filter(question=data['question']).exists():
            raise serializers.ValidationError(f"{data['question']} already exists.")

        new_question = Question.objects.create(question=data['question'], answer=new_correct_answer[0])

        new_question.save()

        new_question.choices.add(new_correct_answer[0])

        for answer in data['choices']:
            answer_obj = Answer.objects.get_or_create(text=answer['text'])
            new_question.choices.add(answer_obj[0])

        serializer = QuestionSerializer(new_question)

        return Response(serializer.data)

    @extend_schema(
        # attach request/response examples to the operation.
        examples=[
            OpenApiExample(
                'Query 1',
                value=descr
            ),
        ],
    )
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data

        question_obj = Question.objects.get(id=instance.id)
        correct_answer = Answer.objects.get_or_create(text=data['answer'])[0]

        question_obj.question = data['question']
        question_obj.answer = correct_answer

        question_obj.choices.set([])

        question_obj.choices.add(correct_answer)

        for answer in data['choices']:
            answer_obj = Answer.objects.get_or_create(text=answer['text'])
            question_obj.choices.add(answer_obj[0])

        question_obj.save()

        serializer = QuestionSerializer(question_obj)

        return Response(serializer.data)
