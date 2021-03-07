from django import forms
from .models import *
from django.forms import fields
from users.models import *

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class ChooseGroup(forms.Form):
    class Meta:
        fields = ('group','plagiarism',)
    def __init__(self, *args, **kwargs):
        group = Group.objects.filter(is_active = True)
        this_choices = []
        for i in group:
            this_choices.append(tuple([i.id,str(i)]))
        super(ChooseGroup, self).__init__(*args, **kwargs)
        self.fields['group'] = forms.ChoiceField(choices=this_choices)
        self.fields['plagiarism'] = forms.FloatField()

class SendedTasksForm(forms.ModelForm):
    class Meta:
        model = SendedTasks
        fields = ('task', 'taskid')
		

class TasksListForm(forms.ModelForm):
    date_end = forms.DateTimeField(widget=DateInput)
    class Meta:
        model = TaskList
        fields = ('taskname','task','group_id','date_end',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        active_groups = Group.objects.filter(is_active = True)
        self.fields['group_id'].queryset  = active_groups
        
class TransformersForm(forms.Form):
    NewPoints=forms.IntegerField(label='Nowe punkty')
    class Meta:
        fields = ('NewPoints',)




