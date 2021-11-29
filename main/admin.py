from django.contrib import admin

from .models import *


admin.site.register(Article)
admin.site.register(Category)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Likes)

admin.site.register(Comment, CommentAdmin)



