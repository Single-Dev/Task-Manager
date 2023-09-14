# Your Task Manager for free

## Frontend
### Task Manager's interface is very comfortable and very awsome because we used for interface from vue. That's create comfortable interface for users and developers can create quickly vue app so we decided use from vue

![home](<static/screenshots/Skrinshot 2023-09-06 184638.png>)
#### Home
![profile](<static/screenshots/Skrinshot 2023-09-06 184727.png>)
#### Profile
![search](<static/screenshots/Skrinshot 2023-09-06 185106.png>)
#### Search for users
![sharedtasks](<static/screenshots/Skrinshot 2023-09-06 185047.png>)
#### Shared Tasks
![login](<static/screenshots/Skrinshot 2023-09-06 185407.png>)
#### SignIn
![signup](<static/screenshots/Skrinshot 2023-09-06 185424.png>)
#### SignUp

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

##### You can create a task:
    /api/create-task/
##### More details
    {
        owner: 1,
        name: 'ToDo',
        caption: 'caption',
        done: false,
        created_on: new Date()
    }

##### You can a task by the id:
    /api/task/{id}/