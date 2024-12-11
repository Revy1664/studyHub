from django.urls import path

from .views import *


urlpatterns = [
	path("register/", register, name="register"),
	path("profile/", profile, name="profile"),
	path("edit_profile/", edit_profile, name="edit_profile"),
	path("logout_user/", logout_view, name="logout_account"),
]