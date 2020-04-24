from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api import models


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Student
        fields = ('snumber', 'name', 'surname', 'email')

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Task
        fields = ('id_zadania', 'temat', 'deadline', 'desc')