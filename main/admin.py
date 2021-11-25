from django.contrib import admin

from .models import *


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    max_num = 10
    min_num = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImageInline,]





