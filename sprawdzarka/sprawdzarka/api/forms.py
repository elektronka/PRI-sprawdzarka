from django import forms
from . import models

class SendedTasksForm(forms.ModelForm):
    class Meta:
        model = models.SendedTasks
        fields = ('taskid','snumber','task')

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('title','content','date_posted','author')



