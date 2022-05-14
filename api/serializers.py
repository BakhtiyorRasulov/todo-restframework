from dataclasses import field
from rest_framework import serializers
from dba.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'