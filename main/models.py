from django.core.validators import MinValueValidator, MaxValueValidator
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
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Статья", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="Имя")
    comment_content = models.CharField(max_length=200, verbose_name="Комментарий")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']


class Likes(models.Model):
    liked_articles = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_likes')
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='author_likes')


class RatingStar(models.Model):
    value = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Rating Star'
        verbose_name_plural = 'Rating Stars'
        ordering = ['-value']


class Rating(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='rating')
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE,
                               related_name='rating')
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE,
                             related_name='rating')

    def __str__(self):
        return f'{self.star} - {self.article}'

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
