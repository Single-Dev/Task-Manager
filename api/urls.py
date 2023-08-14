from django.urls import path
from .views import *
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

app_name="api"

urlpatterns = [
  path('users/', UserListView.as_view(), name='users'), # Read
  path('users/<str:username>/', UserApiView, name='user'), # Read
  path('user/id/<int:pk>/', UserIDApiView, name='user_id'), # Updata
  path('users/updata/<int:pk>/', UpdataUserApiView, name='updata_user'), # Updata
  path('profiles/', ProfilesApiView, name='profiles'), #Read
  path('profiles/<int:user>/', ProfileApiView, name='profile'), #Read
  path('profiles/updata/<int:user>/', UpdataProfileApiView, name='updata_profile'), #Updata
  path('tasks/', TasksApiView, name='tasks'), #Read
  path('tasks/<int:pk>/', TaskApiView, name='task'), #Read
  path('create-task/', CreateTaskApiView, name='post_task'), #Create
  path('updata/<int:pk>/', UpdataTaskApiView, name='updata_task'), #Updata
  path('delete/<int:pk>/', DeleteTaskApiView, name='delete_task'), #Delete
  path('shared-tasks/', SharedTasksApiView, name='shared_tasks'), # Read
  path('add-shared-task/', CreateSharedToDoApiView, name='shared_tasks'), # Post
  path('updata/shared-todo/<int:pk>/', UpdataSharedToDoApiView, name='shared_task'), # Updata
  path('shared-tasks/<int:pk>/', SharedToDoApiView, name='shared_task'), # Read
  path('shared-tasks-list/<int:pk>/', SharedTasksListApiView, name='shared_task'), # Read
]