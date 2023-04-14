from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer, LoginSerializer
from authentication.models import CustomUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import permissions
from django.contrib.auth import login
# Class based view to Get User Details using Token Authentication
# @login_required('api:login')
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def UserDetailAPI(request):
  authentication_classes = (TokenAuthentication,)
  user = CustomUser.objects.get(id=request.user.id)
  serializer = UserSerializer(user)
  return Response({'is_ok': True})

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

class LoginView(APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({'is_ok': True, 'username': user.username })