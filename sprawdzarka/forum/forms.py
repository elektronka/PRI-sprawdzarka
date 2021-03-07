from django.db.models import fields
from django.forms import models
from .models import *
from django import forms
from captcha.fields import CaptchaField

class AddQuestionXmlForm(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = QuestionXml
		fields = ('task_id','question_content')

class AddQuestionPromelaForm(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = QuestionPromela
		fields = ('task_id','question_content')

class AddQuestionXmlFormNew(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = QuestionXml
		fields = ('question_content',)

class AddQuestionPromelaFormNew(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = QuestionPromela
		fields = ('question_content',)

class AddAnswerForm(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = Answer
		fields= ('content',)