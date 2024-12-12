from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .models import CustomUser, Profile
from .forms import RegisterForm, EditProfileForm


def register(request):

	form = RegisterForm()

	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("edit_profile")

	return render(request, "registration/register.html", {"form": form})


@login_required
def profile(request):
	return render(request, "registration/profile.html")


@login_required
def edit_profile(request):

	form = EditProfileForm(instance=request.user.profile)

	if request.method == "POST":
		form = EditProfileForm(request.POST)
		if form.is_valid():
			age = form.cleaned_data.get("age")
			phone_number = form.cleaned_data.get("phone_number")
			bio = form.cleaned_data.get("bio")

			request.user.profile.age = age
			request.user.profile.phone_number = phone_number
			request.user.profile.bio = bio

			request.user.profile.save()
			return redirect("profile")

	return render(request, "registration/edit_profile.html", {"form": form})


def logout_view(request):

	logout(request)

	return redirect("login")
