from django import forms
from .models import SendedTasks

class SendedTasksForm(forms.ModelForm):
    class Meta:
        model = SendedTasks
        fields = ('taskid','snumber','task')
