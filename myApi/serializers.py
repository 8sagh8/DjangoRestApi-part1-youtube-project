from rest_framework import serializers
from .models import *

class TaskSerializers(serializers.ModelSerializer):
    taskList = serializers.CharField(required=False)
    class Meta:
        model = MyTaskList
        fields = '__all__'