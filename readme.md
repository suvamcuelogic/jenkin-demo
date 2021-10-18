#Object Level Permission Explained

1. Install the requirements.txt file in your Virtual env 
2. [https://django-guardian.readthedocs.io/]()

Explaination :

this project consists of single app posts . We have simply implement a Post model 
and made a rule that superuser will perform CRUD all the post and owner of post also do 
the same rest will only can view  them.

I have taken Some Users:(username:password)

suvam:123 => superuser ,
user1:tepa1234 => user
post-admin-1:tepa1234 => user
site-admin-1:tepa1234 => user

Then we Created Different Groups :
1. Site-admin (User List => site-admin-1)
2. Post-admin (User List => post-admin-1)
3. Viewers (User List => user1)

Then We set Rules For different Groups from admin ui (we can also do it by code):
1. For Site-admin Group ,users only can view,approve and delete posts
2. For Post-admin Group ,users only can view,create,change and delete posts
3. For Viewers Group ,users only can view posts


1. First Open admin-site in two browsers and login with mentioned credentials accordingly
2. Trigger the api [http://localhost:8000/role-based/](http://localhost:8000/role-based/) in both browser 
3. You will start seeing all posts for differerent permission for different users :
 
For User belong to Viewers you will get response like this :

`{
    "message": [
        {
            "author": 4,
            "title": "test 1",
            "description": "desciption \r\nby post-admin-1",
            "status": false,
            "datetime": "2021-10-18T11:16:12.748624Z",
            "permission_crud": {
                "can_view": true,
                "can_update": false,
                "can_delete": false
            },
            "object_level_permission": false,
            "permission_level": [
                {
                    "name": "Viewers",
                    "allowed_permissions": [
                        {
                            "name": "Can view simple model",
                            "codename": "view_simplemodel"
                        }
                    ]
                }
            ]
        }
    ],
    "status": 200
}`


For User belong to Post-admin you will get response like this :

`{
    "message": [
        {
            "author": 4,
            "title": "test 1",
            "description": "desciption \r\nby post-admin-1",
            "status": false,
            "datetime": "2021-10-18T11:16:12.748624Z",
            "permission_crud": {
                "can_view": true,
                "can_update": true,
                "can_delete": true
            },
            "object_level_permission": false,
            "permission_level": [
                {
                    "name": "Post-admin",
                    "allowed_permissions": [
                        {
                            "name": "Can add simple model",
                            "codename": "add_simplemodel"
                        },
                        {
                            "name": "Can change simple model",
                            "codename": "change_simplemodel"
                        },
                        {
                            "name": "Can view simple model",
                            "codename": "view_simplemodel"
                        }
                    ]
                }
            ]
        }
    ],
    "status": 200
}`

For User belong to Site-admin you will get response like this :

`{
    "message": [
        {
            "author": 4,
            "title": "test 1",
            "description": "desciption \r\nby post-admin-1",
            "status": false,
            "datetime": "2021-10-18T11:16:12.748624Z",
            "permission_crud": {
                "can_view": true,
                "can_update": true,
                "can_delete": true
            },
            "object_level_permission": false,
            "permission_level": [
                {
                    "name": "Site-admin",
                    "allowed_permissions": [
                        {
                            "name": "Can change simple model",
                            "codename": "change_simplemodel"
                        },
                        {
                            "name": "Can delete simple model",
                            "codename": "delete_simplemodel"
                        },
                        {
                            "name": "Can view simple model",
                            "codename": "view_simplemodel"
                        }
                    ]
                }
            ]
        }
    ],
    "status": 200
}`



Check SS Folder for screenshots