from django.urls import path
from .views import *
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

app_name="api"

urlpatterns = [
  path('users/', UsersApiView, name='users'),
  path('todo/', ToDoApiView, name='todo'),
  path('mytasks/', MyTasksApiView, name='my_task'),
  path('create-task/', CreateTaskApiView, name='post_todo'),
]