from django.urls import path, re_path
from .views import article_list, article_detail

app_name = 'blog'

urlpatterns = [
    path('', article_list, name="blog_list"),
    re_path(r'(?P<article_slug>[-\w]+)/', article_detail, name="article_detail"),
]