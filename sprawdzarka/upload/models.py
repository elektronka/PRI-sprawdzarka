from django.db import models
from django.db.models.fields import IntegerField
from users.models import *
from datetime import datetime

class TaskList(models.Model):
    id = models.IntegerField(primary_key=True)
    taskname = models.CharField("Nazwa zadania", max_length=200, blank=False, default=None)
    tname = models.CharField(max_length=100)
    task = models.FileField("Plik", upload_to='task/tasklist/')
    group_id = models.ForeignKey(Group,on_delete=CASCADE, default='0')
    date_end = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self) -> str:
        return self.taskname

class SendedTasks(models.Model):
    id = models.IntegerField(primary_key=True)
    taskid = models.ForeignKey(TaskList, on_delete=CASCADE)
    snumber = models.CharField(max_length=6)
    task = models.FileField("Plik",upload_to='task/sendedtasks/')
    has_been_tested = models.BooleanField(default=False)
    group = models.CharField(max_length=100, default="0")
    class Meta:
        ordering = ('group','taskid',)
        
class StudentsPoints(models.Model):
    id = models.IntegerField(primary_key=True)
    snumber=models.CharField(max_length=6)
    taskid=models.ForeignKey(TaskList, on_delete=CASCADE)
    number_task=models.CharField(max_length=3)
    points=models.IntegerField(default=0)
    class Meta:
        ordering=('taskid','snumber')

class Plagiat(models.Model):
    id = models.IntegerField(primary_key=True)
    snumber1 = models.CharField(max_length=6)
    snumber2 = models.CharField(max_length=6)
    name1 = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)
    plagiat = models.FloatField()
    group_id = models.IntegerField(default=-1)
    class Meta:
        ordering=('-plagiat',)
    
