from django.db import models
from django.utils.text import slugify
from account.models import MyUser


class Category(models.Model):
    slug = models.SlugField(max_length=64, primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)


class ArticleImage(models.Model):
    article_image = models.ImageField(upload_to='posts', blank=True, null=True)
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
