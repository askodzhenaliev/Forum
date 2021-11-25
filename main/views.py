from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Article, ArticleImage
from .serializers import CategorySerializer, ArticleSerializer


@api_view(['GET'])
def categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


class ArticleListView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        article = request.data
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article.saved = serializer.save()
        return Response(serializer.data)


