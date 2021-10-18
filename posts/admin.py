from django.contrib import admin

# Register your models here.

from .models import SimpleModel

admin.site.register(SimpleModel)
