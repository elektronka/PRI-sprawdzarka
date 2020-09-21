from django.db import models



class Student(models.Model):
    snumber = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    email = models.EmailField()