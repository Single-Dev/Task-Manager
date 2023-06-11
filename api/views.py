from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from authentication.models import CustomUser
from app.models import ToDo
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
    todo = ToDo.objects.all()
    serializer = ToDoSerializer(todo, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def MyTasksApiView(request):
    tasks = ToDo.objects.get(owner=request.user.id)
    serializer = ToDoSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def CreateTaskApiView(request):
    serializer = ToDoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.error_messages)
