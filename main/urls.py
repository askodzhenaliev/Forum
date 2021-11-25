from django.urls import path

from main import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='categories-list'),
    path('articles/', views.ArticleView.as_view(), name='articles-list'),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view()),
    path('articles-update/<int:pk>/', views.ArticleUpdateView.as_view()),
    path('articles-delete/<int:pk>/', views.ArticleDeleteView.as_view()),
]