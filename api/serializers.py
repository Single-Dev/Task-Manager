from rest_framework import serializers
from authentication.models import CustomUser, Profile
from app.models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "username","email", "gender"]

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class SharedTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedTask
        fields = '__all__'