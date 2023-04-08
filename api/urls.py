from django.urls import path
from .views import *

app_name="api"

urlpatterns = [
  path("get-details/",UserDetailAPI, name='get-details'),
  path("login/",LoginView.as_view(), name='login'),
  path('register/',RegisterUserAPIView.as_view(), name='signup'),
]