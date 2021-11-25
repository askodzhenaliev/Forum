from django.urls import path

from main import views

urlpatterns = [
    path('categories/', views.categories, name='categories-list'),
    path('articles/', views.ArticleListView.as_view(), name='articles-list'),
]