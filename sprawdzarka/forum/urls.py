from django.urls import include, path
from .views import *


urlpatterns = [
    path('', choose, name='forum'),
    path('<str:choose>/', home, name='home'),
    path('all/<str:choose>', all, name='all'),
    path('new/<str:choose>', new, name='new'),
    path('<str:choose>/<int:id>/', question, name='question'),
    path('question_choose/<str:choose>', question_fake, name= 'add_question_choose'),
    path('answer/<str:choose>/<int:id>/', add_answer, name = 'add_answer'),
    path('ask_question/<str:choose>/<int:id>/', add_question, name = 'ask_question'),
]
