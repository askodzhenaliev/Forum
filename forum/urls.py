from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from rest_framework.routers import DefaultRouter

from main.views import ArticleViewSet, CategoryListView

router = DefaultRouter()
router.register('articles', ArticleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('v1/api/categories/', CategoryListView.as_view()),
    path('v1/api/account/', include('account.urls')),
    path('v1/api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)