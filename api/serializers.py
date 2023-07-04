from rest_framework import serializers
from authentication.models import CustomUser
from app.models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "username","email", "gender", "followers"]

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class SharredTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharredTask
        fields = ['id', 'name', 'task', 'users']