from django.db.models.expressions import Case
from users.models import Group
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from datetime import datetime

class TeacherTask(models.Model):
    id = models.IntegerField(primary_key=True)
    task_name = models.CharField("Nazwa zadania", max_length=100, blank=False, default=None)
    task_content = models.TextField('Treść zadania', max_length=500, blank=False,default=None)
    max_points = models.IntegerField("Maksymalne punkty", default=0)
    file = models.FileField("Plik", upload_to="task/promela/teacher_ltl")
    group_id = models.ForeignKey(Group,on_delete=CASCADE)
    date_end = models.DateTimeField(auto_now=False, auto_now_add=False,)

    def __str__(self) -> str:
        return self.task_name
    
class StudentTask(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.ForeignKey(TeacherTask, on_delete=CASCADE)
    task_name = models.CharField(max_length=100, blank=False, default = '0')
    task_file = models.FileField("Plik", upload_to = "task/promela/student_files")
    output_file = models.FileField("Output")
    points = models.IntegerField(default=0)
    snumber = models.CharField(max_length=6)
    group_id = models.CharField(max_length=100, default='0')
    has_been_tested= models.BooleanField(default=False)
    class Meta:
        ordering = ('group_id','task_id',)