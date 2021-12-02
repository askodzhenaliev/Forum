from django.db.models import Avg
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
        fields = ('id', 'category', 'title', 'text', 'created_date', 'article_image')

    def create(self, validated_data):
        request = self.context.get('request')
        user_id = request.user.id
        validated_data['author_id'] = user_id
        post = Article.objects.create(**validated_data)
        return post

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.author.email
        representation['likes'] = Likes.objects.filter(liked_articles=instance).count()
        representation['rating'] = instance.rating.aggregate(Avg('rating'))
        return representation


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user
        comment = Comment.objects.create(author=author, **validated_data)
        return comment


class LikeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Likes
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        articles = validated_data.get('liked_articles')

        if Likes.objects.filter(author=user, liked_articles=articles):
            return Likes.objects.get(author=user, liked_articles=articles)
        else:
            return Likes.objects.create(author=user, liked_articles=articles)


class RatingSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Rating
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user
        post = validated_data.get('post')
        rating = Rating.objects.get_or_create(author=author, post=post)[0]
        rating.rating = validated_data['rating']
        rating.save()
        return rating


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.email
        representation['post'] = instance.post.title
        return representation


