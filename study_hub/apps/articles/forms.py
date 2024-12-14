from django.forms import ModelForm

from .models import Article, ArticleFile


class ArticleCreationForm(ModelForm):

	class Meta:
		model = Article
		fields = "__all__"


class ArticleFileForm(ModelForm):

	class Meta:
		model = ArticleFile
		fields = ["file"]
