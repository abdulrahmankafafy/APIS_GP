from django.contrib import admin

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_id', 'title', 'content']
    list_display_links = ['id']

admin.site.register(Article, ArticleAdmin)