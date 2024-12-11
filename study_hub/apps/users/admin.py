from django.contrib import admin

from .models import CustomUser, Profile


# register models in admin panel
admin.site.register(CustomUser)
admin.site.register(Profile)
