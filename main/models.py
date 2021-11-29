from django.db import models
from account.models import MyUser


class Category(models.Model):
    slug = models.SlugField(max_length=255, primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    article_image = models.FileField(blank=True, null=True, verbose_name="Добавить фото в статью")

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


class Likes(models.Model):
    liked_articles = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_likes')
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='author_likes')
