from django.db import models
from django.contrib.auth.models import  User

class SimpleModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120,blank=False)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (
            ('assign_post', 'Assign post'),
            ("view_project","View Posts"),

            # ("view_simplemodel", "View Posts"),
            # ("add_simplemodel","Add Posts"),
            # ("change_simplemodel", "Edit Posts"),
            # ("delete_simplemodel", "Delete Posts")

        )


