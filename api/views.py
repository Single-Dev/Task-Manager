from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from authentication.models import CustomUser
from app.models import Task
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.shortcuts import get_object_or_404

#---------- users api ----------------
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def UsersApiView(request):
    user = User.objects.all()
    serializer = UsersSerializer(user, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def UserApiView(request, username):
    user = User.objects.get(username=username)
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
    sharred_task = task.task.get(task__id=pk)
    if request.user in sharred_task.users.all() or request.user == task.owner:
        return Response(serializer.data)
    else:
        return Response({"detail": "You can not get this data"})

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
def SharedTaskApiView(request):
    sharred_task = SharredTask.objects.all()
    serializer = SharredTaskSerializer(sharred_task, many=True)
    return Response(serializer.data)
    # if request.user.is_authenticated:
    # else:
    #     return Response({"detail": "Authentication credentials were not provided."})