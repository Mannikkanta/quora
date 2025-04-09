from django.urls import path
from . import views
from .views import QuestionListView, QuestionDetailView

urlpatterns = [
    path('', QuestionListView.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('question/new/', views.create_question, name='create_question'),
    path('question/<int:pk>/answer/', views.create_answer, name='create_answer'),
    path('answer/<int:pk>/like/', views.like_answer, name='like_answer'),
]