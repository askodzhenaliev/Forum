from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from main import views
from main.views import ArticleViewSet, CategoryListView, LikesView, AddStarRatingView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register('articles', ArticleViewSet)
router.register('like', LikesView)
router.register('rating', AddStarRatingView)


schema_view = get_schema_view(
   openapi.Info(
      title="Forum Kuiruk-Mai API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui()),
    path('api-auth/', include('rest_framework.urls')),
    path('v1/api/categories/', CategoryListView.as_view()),
    path('v1/api/account/', include('account.urls')),
    path('v1/api/', include(router.urls)),
    path('comment/<slug:slug>', views.addComment, name="comment"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





