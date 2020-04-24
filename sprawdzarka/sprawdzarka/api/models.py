from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Student(models.Model):
    snumber = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    email = models.EmailField()
    
class Task(models.Model):
    id_zadania = models.IntegerField(primary_key=True)
    temat = models.CharField(max_length=256)
    deadline = models.DateTimeField()
    desc = models.CharField(max_length=256)

class SendedTasks(models.Model):
    id = models.IntegerField(primary_key=True)
    taskid = models.CharField(max_length=5)
    snumber = models.CharField(max_length=6)
    task = models.FileField(upload_to='task/SendedTasks/')

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


