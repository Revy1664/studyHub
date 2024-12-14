from django.shortcuts import render, redirect, get_object_or_404

from .forms import ArticleCreationForm, ArticleFileForm
from .models import Article, ArticleFile


def index(request):

	return render(request, "articles/index.html")


def create_article(request):

	article_form = ArticleCreationForm()
	article_file_form = ArticleFileForm()

	if request.method == "POST":
		
		article_form = ArticleCreationForm(request.POST)
		article_file_form = ArticleFileForm(request.POST, request.FILES)
		
		# if forms are valid then get the values
		if article_form.is_valid() and article_file_form.is_valid():
			title = article_form.cleaned_data.get("title")
			text = article_form.cleaned_data.get("text")
			author = article_form.cleaned_data.get("author")

			# article creating
			art = Article.objects.create(
				title = title,
				text = text,
				author = author
			)

			art.save()

			# get all the files from form
			files = request.FILES.getlist("file")

			# creating those files from form
			for file in files:
				ArticleFile.objects.create(
					file = file,
					article = art,
				)


			return redirect("profile")

	return render(request, "articles/create_article.html", {"article_form": article_form, "article_file_form": article_file_form})


def detail_article(request, pk):

	article = get_object_or_404(Article, id=pk)

	return render(request, "articles/detail_article.html", {"article": article})		
