from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d/%m/%Y %H:%M', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'author', 'category', 'title', 'text', 'created_date')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ArticleImageSerializer(instance.images.all(), many=True, context=self.context).data
        return representation

class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = '__all__'
