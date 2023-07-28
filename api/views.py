from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from authentication.models import CustomUser
from app.models import Task
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, generics, filters
from django.shortcuts import get_object_or_404

#---------- users api ----------------
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def UserApiView(request, username):
    user = User.objects.get(username=username)
    serializer = UsersSerializer(user, many=False)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def UserIDApiView(request, pk):
    user = User.objects.get(id=pk)
    serializer = UsersSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def UpdataUserApiView(request, pk):
    user = User.objects.get(id=pk)
    serializer = UsersSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'first_name']

#------------- Profile API

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def ProfileApiView(request):
    profile = Profile.objects.all()
    serializer = ProfileSerializer(profile, many=True)
    return Response(serializer.data)


#---------- Task api ----------------
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def TasksApiView(request):
    tasks = Task.objects.filter(owner=request.user.id)
    serializer = TaskSerializer(tasks, many=True)
    if request.user.is_authenticated:
        return Response(serializer.data)
    else:
        return Response({"detail": "Authentication credentials were not provided."})

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def TaskApiView(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def CreateTaskApiView(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.error_messages)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def UpdataTaskApiView(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid() and task.owner == request.user:
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def DeleteTaskApiView(request, pk):
    task = Task.objects.get(id=pk)
    if task.owner == request.user:
        task.delete()
        return Response({"deleted": "true"})
    else:
        return Response({"deleted": "false"})

#---------- Shared Task api ----------------
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def SharedTasksApiView(request):
    shared_task = SharedTask.objects.filter(users=request.user)
    serializer = SharedTaskSerializer(shared_task, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def SharedTaskApiView(request, pk):
    shared_task = SharedTask.objects.filter(users=request.user).get(id=pk)
    serializer = SharedTaskSerializer(shared_task, many=False)
    return Response(serializer.data)