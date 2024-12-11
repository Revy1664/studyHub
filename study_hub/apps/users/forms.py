from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


from .models import CustomUser, Profile


class RegisterForm(UserCreationForm):

	class Meta:
		model = CustomUser
		fields = ["username"]


class EditProfileForm(ModelForm):

	class Meta:
		model = Profile
		fields = ["age", "phone_number"]
