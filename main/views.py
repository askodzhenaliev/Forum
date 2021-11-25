from django.shortcuts import render
from rest_framework import generics

from .models import Category, Article, ArticleImage
from .serializers import CategorySerializer, ArticleSerializer, ArticleImageSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleUpdateView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDeleteView(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleImageView(generics.ListAPIView):
    queryset = ArticleImage.objects.all()
    serializer_class = ArticleImageSerializer

    def get_serializer_context(self):
        return {'request': self.request}



