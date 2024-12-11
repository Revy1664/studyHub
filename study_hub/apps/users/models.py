from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

	STATUS_CHOICES = (
		("Student", "Student"),
		("Teacher", "Teacher"),
	)

	bio = models.TextField(verbose_name="Biography")
	status = models.CharField(
		max_length=20, 
		choices=STATUS_CHOICES, 
		default="Student",
		verbose_name="Status"
	)


class Profile(models.Model):
	age = models.IntegerField(verbose_name="Age", null=True, blank=True)
	phone_number = models.CharField(max_length=50, verbose_name="Phone number", null=True, blank=True)
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username
