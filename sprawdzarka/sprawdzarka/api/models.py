from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Student(models.Model):
    snumber = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    email = models.EmailField()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
