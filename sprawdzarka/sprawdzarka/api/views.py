from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api import serializers
from django.shortcuts import render, redirect
from . import models
from .forms import SendedTasksForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


class StudentViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = serializers.StudentSerializer

class taskViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = serializers.TaskSerializer


def index(request):
    return render(request,"index.html")

def task(request):
    return render(request, "task.html")

def task_sended_list(request):
    sended=models.SendedTasks.objects.all
    return render(request,'task_sended_list.html',{'sended': sended})

def task_sended_upload(request):
    if request.method=='POST':
        form = SendedTasksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=SendedTasksForm()
    return render(request,'task_sended_upload.html', {'form': form})

def forum(request):
    context = models.Post.objects.all
    return render(request, 'forum/forum.html', {'context': context})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
	    form = AuthenticationForm(data=request.POST)
	    if form.is_valid():
	      #log in the user
		    user = form.get_user()
		    login(request,user)
		    return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
	    logout(request)
	    return redirect('articles:list')