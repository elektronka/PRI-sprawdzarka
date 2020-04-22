from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api import serializers
from django.shortcuts import render
from api import models
from django.http import HttpResponse


class StudentViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = serializers.StudentSerializer

posts = [
    {
        'author': 'Patryk Łukasiewicz',
        'title': 'Forum Post 1',
        'content': 'Test post 1',
        'date_posted': '22 April 2020'
    },
    {
        'author': 'Patryk Łukasiewicz',
        'title': 'Forum post 2',
        'content': 'Test post 1',
        'date_posted': '21 April 2020'
    }
]


def index(request):
    return render(request, "index.html")

def forum(request):
    context = {
        'posts': posts
    }
    return render(request, 'forum/forum.html', context)