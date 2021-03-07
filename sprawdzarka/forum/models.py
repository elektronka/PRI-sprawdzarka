from typing import ChainMap
from django.db import models
from Promela.models import *
from upload.models import *


class QuestionXml(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.ForeignKey(TaskList, on_delete=CASCADE)
    question_content = models.TextField("Zadaj pytanie", max_length=1024, blank=False, default=None)
    date = models.DateTimeField(auto_now_add= True)
    has_teacher_answer = models.BooleanField(default= False)
    asking_student = models.CharField(max_length= 6)

    class Meta:
        ordering = ('-date',)

class QuestionPromela(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.ForeignKey(TeacherTask, on_delete=CASCADE)
    question_content = models.TextField("Zadaj pytanie", max_length=1024, blank=False, default=None)
    date = models.DateTimeField(auto_now_add= True)
    has_teacher_answer = models.BooleanField(default= False)
    asking_student = models.CharField(max_length= 6)

    class Meta:
        ordering = ('-date',)

class Answer(models.Model):
    id = models.IntegerField(primary_key=True)
    section = models.CharField(max_length=10)
    question_id = models.IntegerField()
    who_answered = models.CharField(max_length= 30)
    content = models.TextField(max_length=1024, blank=False, default=None)
    date = models.DateTimeField(auto_now_add= True)
    has_teacher_answered = models.BooleanField(default=False)
