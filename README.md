# Your Task Manager for free

## Frontend
### Task Manager's interface is very comfortable and very awsome because we used for interface from vue. That's create comfortable interface for users and developers can create quickly vue app so we decided use from vue

#### Home
![home](<static/screenshots/Skrinshot 2023-09-06 184638.png>)
#### Profile
![profile](<static/screenshots/Skrinshot 2023-09-06 184727.png>)
#### Search for users
![search](<static/screenshots/Skrinshot 2023-09-06 185106.png>)
#### Shared Tasks
![sharedtasks](<static/screenshots/Skrinshot 2023-09-06 185047.png>)
#### Login
![login](<static/screenshots/Skrinshot 2023-09-06 185407.png>)
#### SignUp
![signup](<static/screenshots/Skrinshot 2023-09-06 185424.png>)

## Launch
### You should install this repository

#### First of all create environment for `backend`
    python -m venv .{venv name}
#### and then activate it
    .{venv name}/Scripts/Activate
#### and install necessary apps
    pip install -r requirements.txt
#### you must migrate
    python manage.py makemigrations authentication
    python manage.py migrate
#### now you must migrate all
    python manage.py makemigrations
    python manage.py migrate
#### finally you can run django app
    python manage.py runserver 8000
#### Now you must install some apps for `frontend`
##### first you must change directory
    cd frontend
##### install apps
    npm install
#### finally you can run vue app
    npm run serve

## Backend
### We used django for the backend part of the site because it is fast, high quality and provides smooth service to many users

#### Users' data:
##### You can get all users
    /api/users/

##### You can get a user by the username
    /api/users/{username}/

##### You can get a user by the id
    /api/user/id/{id}/
    
##### You can updata a user by the id:
    /api/users/updata/{id}/

#### Profies:

##### You can get all profiles
    /api/profiles/

##### You can get a profile by the username
    /api/profiles/{username}/

##### You can updata a profile by the username:
    /api/profiles/updata/{username}/

#### Tasks

##### You can get all task
    /api/tasks/

##### You can a task by the id:
    /api/task/{id}/

##### You can post a task:
    /api/create-task/

##### More details
    {
        owner: 1,
        name: 'ToDo',
        caption: 'caption',
        done: false,
        created_on: new Date()
    }

##### You can updata a task by the id:
    /api/updata/{id}/

##### You can delete a task by the id:
    /api/delete/{id}/

#### Shared Tasks

##### You can get all shared tasks
    /api/shared-tasks/

##### You can get a shared task by the id
    /api/shared-tasks/{id}

##### You can updata a shared task by the id
    /api/updata/shared-todo/{id}/

##### You can get a task by the shared task id
    /api/shared-tasks-list/{id}