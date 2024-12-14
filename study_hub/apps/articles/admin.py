from django.contrib import admin

from .models import Article, ArticleFile


class ArticleFileInline(admin.StackedInline):
	model = ArticleFile
	extra = 0


class ArticleAdmin(admin.ModelAdmin):
		inlines = [
			ArticleFileInline,
		]

admin.site.register(Article, ArticleAdmin)
