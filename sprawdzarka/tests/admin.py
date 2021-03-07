from django.contrib import admin
from .models import *

admin.site.register(TestFileModel)
admin.site.register(TestQuestionModel)
admin.site.register(QuestionAnswerModel)
admin.site.register(StudentAnswerModel)
admin.site.register(StudentPointsTest)
