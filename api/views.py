from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from authentication.models import CustomUser
from app.models import Task
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.shortcuts import get_object_or_404

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def UsersApiView(request):
    user = User.objects.all()
    serializer = UsersSerializer(user, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def TasksApiView(request):
    tasks = Task.objects.filter(owner=request.user.id)
    serializer = TaskSerializer(tasks, many=True)
    if request.user.is_authenticated:
        return Response(serializer.data)
    else:
        return Response({"detail": "Authentication credentials were not provided."})

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
    return Response({"deleted": "done"})