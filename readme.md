#Object Level Permission Explained

1 . Install the requirements.txt file in your Virtual env 
2 . [https://django-guardian.readthedocs.io/]()

Explaination :

this project consists of single app posts . We have simply implement a Post model 
and made a rule that superuser will perform CRUD all the post and owner of post also do 
the same rest will only can view  them.

I have taken Two Users:(username:password)
suvam:123 => superuser
user1:tepa1234 => user

1. First Open adminsite in two browsers and login with mentioned credentials accordingly
2. Trigger the api [http://localhost:8000/role-based/](http://localhost:8000/role-based/) in both browser 
3. You will start seeing all posts for suvam user and only one post for user1 to update


Check SS Folder for screenshots