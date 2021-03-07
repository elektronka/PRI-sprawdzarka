from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from .models import *
from django.forms import Form , fields, ModelForm
from captcha.fields import CaptchaField
from django import forms


class RegistrationForm(UserCreationForm):
    
    captcha = CaptchaField()
    class Meta:
        model = Account
        fields = ('username', 'snumber', 'password1', 'password2','group_id')
    def __init__(self, *args, **kwargs):
        group_ids = Group.objects.filter(is_active = True)
        this_choices = []
        for i in group_ids:
            this_choices.append(tuple([i.id,str(i)]))
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['group_id'] = forms.ChoiceField(choices=this_choices)
term_choices = (
        ('zima','Semestr Zimowy'),
        ('lato','Semestr Letni')
    ) 

class GroupForm(Form):
    name = fields.CharField(label='Nazwa grupy', max_length=255)
    year = fields.CharField(label='Rok akademicki', max_length=10)
    term = fields.ChoiceField(choices=term_choices)

class PassForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('password1', 'password2')

class DeleteGroup(Form):
    delete = fields.CharField(label="Czy na pewno chcesz usunąć grupę? Wpisz 'Usuń'.")
    class Meta:
        fields = ('delete',)
    
class ChangeGroup(Form):
    def __init__(self, *args, **kwargs):
        group_ids = Group.objects.filter(is_active = True)
        this_choices = []
        for i in group_ids:
            this_choices.append(tuple([i.id,str(i)]))
        super(ChangeGroup, self).__init__(*args, **kwargs)
        self.fields['group_id'] = forms.ChoiceField(choices=this_choices)