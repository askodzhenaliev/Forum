from django.contrib import admin

from .models import *


admin.site.register(Article)
admin.site.register(Category)


admin.site.register(Likes)

admin.site.register(RatingStar)

admin.site.register(Comment)




