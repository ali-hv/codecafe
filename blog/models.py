from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from mysite.models import TimeStampedModel
from django.contrib.auth.models import User
from courses.models import Category
from comments.models import Comment


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(verbose_name="Author Bio")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def get_full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Article(TimeStampedModel):
    title = models.CharField(max_length=250, verbose_name='Article Title')
    slug = models.SlugField(unique=True, max_length=255, allow_unicode=True)
    detail = models.TextField(verbose_name='Article Detail')
    image = models.ImageField(upload_to='photos/articles/%Y-%m-%d/', verbose_name='Article Detail')
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Article Category')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Article Author')
    comments = GenericRelation(Comment)
