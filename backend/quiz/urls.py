from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from django.urls import path
from . import viewsets

router = DefaultRouter()
router.register('questions', viewsets.QuestionsViewSet, basename='question')

urlpatterns = [
    path('', include(router.urls)),
]
