from django.urls import path
from .views import *
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

app_name="api"

urlpatterns = [
  # path('obtain_jwt_token/', obtain_jwt_token),
  # path('refresh_jwt_token/', refresh_jwt_token),
  # path("get-details/",UserDetailAPI, name='get-details'),
  # path("login/",LoginView.as_view(), name='login'),
  # path('register/',RegisterUserAPIView.as_view(), name='signup'),
]