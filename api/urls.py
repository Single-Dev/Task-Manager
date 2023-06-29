from django.urls import path
from .views import *
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

app_name="api"

urlpatterns = [
  path('users/', UsersApiView, name='users'), # Read
  path('users/<int:pk>/', UpdataUserApiView, name='_updata_user'), # Updata
  path('tasks/', TasksApiView, name='tasks'), #Read
  path('tasks/<int:pk>/', TaskApiView, name='task'), #Read
  path('create-task/', CreateTaskApiView, name='post_task'), #Create
  path('updata/<int:pk>/', UpdataTaskApiView, name='updata_task'), #Updata
  path('delete/<int:pk>/', DeleteTaskApiView, name='delete_task'), #Delete
  path('shared-task/', SharedTaskApiView, name='shared_task'), # Read
]