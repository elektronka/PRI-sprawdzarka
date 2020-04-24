from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api import serializers
from django.shortcuts import render, redirect
from . import models, forms
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
        form = forms.SendedTasksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=forms.SendedTasksForm()
    return render(request,'task_sended_upload.html', {'form': form})

def forum(request):
    context = models.Post.objects.all
    if request.method=='POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.PostForm()
    return render(request, 'forum/forum.html', {'context': context})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('api:')
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
		    return redirect('api:forum')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
	    logout(request)
	    return redirect('api:')

def read_file(request, file_to_open):
    f = open(r'task/SendedTasks/'+file_to_open, 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")