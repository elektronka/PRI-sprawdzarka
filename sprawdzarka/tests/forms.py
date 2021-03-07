from django.db.models import fields
from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class TestFileForm(forms.ModelForm):
    date_start = forms.DateTimeField(widget=DateInput)
    date_end = forms.DateTimeField(widget=DateInput)
    class Meta:
        model = TestFileModel
        fields = ('file', 'name', 'date_start', 'date_end', 'group_id')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        active_groups = Group.objects.filter(is_active = True)
        self.fields['group_id'].queryset  = active_groups

class TestViewForm(forms.ModelForm):

    class Meta:
        model = StudentAnswerModel
        fields = ('answer',)
    
    def __init__(self, *args, **kwargs):
        this_choices = []
        test_id = kwargs.pop('test_id')
        question_id = kwargs.pop('question_id')
        user = kwargs.pop('user')
        
        answers = [str(elem) for elem in list(QuestionAnswerModel.objects.filter(test_id = test_id, question_id = question_id ).values_list('content', flat=True))]
        letter_answer = [str(elem) for elem in list(QuestionAnswerModel.objects.filter(test_id = test_id, question_id = question_id ).values_list('letter', flat=True))]
        
        if len(answers) > 0 and len(letter_answer) > 0:
            for i,j in zip(answers, letter_answer):
                this_choices.append(tuple([j,i]))

        super(TestViewForm, self).__init__(*args, **kwargs)
        self.fields['answer'] = forms.ChoiceField(label = "Wybierz odpowiedź z podanych: ",choices=this_choices, widget = forms.RadioSelect)
        self.fields['test_id'] = forms.IntegerField(widget=forms.HiddenInput(),initial = test_id)
        self.fields['question_id'] = forms.IntegerField(widget=forms.HiddenInput(),initial = question_id)
        self.fields['snumber'] = forms.CharField(widget=forms.HiddenInput(), initial = user)


    
         