from rest_framework import generics, viewsets

from .models import Category, Article, ArticleImage
from .serializers import CategorySerializer, ArticleSerializer, ArticleImageSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleImageView(generics.ListAPIView):
    queryset = ArticleImage.objects.all()
    serializer_class = ArticleImageSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


