from django.db import models

from users.models import CustomUser


class Article(models.Model):
	title = models.CharField(max_length=50, verbose_name="Title")
	text = models.TextField(verbose_name="Body")
	author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Author")


	def __str__(self):
		return self.title


class ArticleFile(models.Model):

	file = models.FileField(upload_to="files/")
	article = models.ForeignKey(Article, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.article.title}_article_file"
