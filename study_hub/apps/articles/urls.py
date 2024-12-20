from django.urls import path

from .views import *


urlpatterns = [
	path('', index, name="index"),
	path('create_article/', create_article, name="create_article"),
	path('<int:pk>/', detail_article, name="detail_article"),
	path('edit_article/<int:pk>/', edit_article, name="edit_article"),
	path('delete/<int:pk>/', delete_article, name="delete_article"),
]