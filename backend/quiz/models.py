from django.db import models


class Answer(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Question(models.Model):
    question = models.CharField(max_length=255, unique=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE,
                                  related_name='correct_answer')
    choices = models.ManyToManyField(Answer, related_name='choices')
