from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views, viewsets

router = DefaultRouter()
router.register('questions', viewsets.QuestionsViewSet, basename='question')
router.register('answers', viewsets.AnswersViewSet, basename='answer')

urlpatterns = [
    path('<int:pk>/', views.QuestionDetailAPIView.as_view()),
    #path('', views.QuestionListCreateAPIView.as_view()),
    path('', include(router.urls)),
]
