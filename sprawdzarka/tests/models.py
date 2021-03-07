from django.db import models
from users.models import *

class TestFileModel(models.Model):
    id = models.IntegerField(primary_key=True)
    file = models.FileField(verbose_name="Plik", upload_to='task/tests')
    name = models.CharField(verbose_name="Wyświetlana nazwa testu", max_length=100)
    has_been_chcecked = models.BooleanField(default=False)
    date_start = models.DateTimeField(verbose_name="Data rozpoczęcia testu", auto_now=False, auto_now_add=False)
    date_end = models.DateTimeField(verbose_name="Data zakończenia testu",auto_now=False, auto_now_add=False)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Grupa",)

class TestQuestionModel(models.Model):
    id = models.IntegerField(primary_key=True)
    test_id = models.IntegerField(default=0)
    question_id = models.IntegerField(default=0)
    content = models.CharField(max_length=100)

class QuestionAnswerModel(models.Model):
    id = models.IntegerField(primary_key=True)
    test_id = models.IntegerField(default=0)
    question_id = models.IntegerField(default=0)
    letter = models.CharField(max_length=1)
    content = models.CharField(max_length=100)
    is_right = models.BooleanField(default=False)

class StudentAnswerModel(models.Model):
    id = models.IntegerField(primary_key=True)
    snumber = models.CharField(max_length=6)
    test_id = models.IntegerField(default=0)
    question_id = models.IntegerField(default=0)
    answer = models.CharField( max_length=1)
    is_right = models.BooleanField(default=False)

class StudentPointsTest(models.Model):
    id = models.IntegerField(primary_key=True)
    snumber = models.CharField(max_length=6)
    test_id = models.IntegerField(default=0)
    points = models.IntegerField(default=0)