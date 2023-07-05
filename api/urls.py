from django.urls import path
from .views import *
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

app_name="api"

urlpatterns = [
  path('users/', UsersApiView, name='users'), # Read
  path('users/<str:username>/', UserApiView, name='user'), # Read
  path('user/id/<int:pk>/', UserIDApiView, name='user_id'), # Updata
  path('users/update/<int:pk>/', UpdataUserApiView, name='updata_user'), # Updata
  path('profiles/', ProfileApiView, name='profiles'), #Read
  path('tasks/', TasksApiView, name='tasks'), #Read
  path('tasks/<int:pk>/', TaskApiView, name='task'), #Read
  path('create-task/', CreateTaskApiView, name='post_task'), #Create
  path('updata/<int:pk>/', UpdataTaskApiView, name='updata_task'), #Updata
  path('delete/<int:pk>/', DeleteTaskApiView, name='delete_task'), #Delete
  path('shared-task/', SharedTaskApiView, name='shared_task'), # Read
]