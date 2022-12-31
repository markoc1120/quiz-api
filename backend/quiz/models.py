from django.db import models

# Create your models here.
class Quiz(models.Model):
    subject = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    answer = models.CharField(max_length=255)
