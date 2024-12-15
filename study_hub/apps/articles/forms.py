from django.forms import ModelForm

from .models import Article, ArticleFile


class ArticleForm(ModelForm):

	class Meta:
		model = Article
		fields = ["title", "text",]


class ArticleFileForm(ModelForm):

	class Meta:
		model = ArticleFile
		fields = ["file",]
