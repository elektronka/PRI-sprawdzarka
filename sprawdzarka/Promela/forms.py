from users.models import Group
from django import forms
from .models import *
from django.forms import fields

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class TeacherTaskForm(forms.ModelForm):
    date_end = forms.DateTimeField(widget=DateInput)
    class Meta:
        model = TeacherTask
        fields = ('task_name','task_content','max_points','file','group_id','date_end',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        active_groups = Group.objects.filter(is_active = True)
        self.fields['group_id'].queryset  = active_groups

class StudentTaskForm(forms.ModelForm):
    class Meta:
        model = StudentTask
        fields = ('task_file','task_id')
class TransformersForm(forms.Form):
    NewPoints=forms.IntegerField(label='Nowe punkty')
    class Meta:
	    fields = ('NewPoints',)