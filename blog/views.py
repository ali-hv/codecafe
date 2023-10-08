from django.shortcuts import render, get_object_or_404
from .models import Article


def article_list(request):
    articles = Article.objects.filter(is_published=True)
    context = {'articles': articles}

    return render(request, 'blog/index.html', context=context)


def article_detail(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    context = {'article': article}

    return render(request, 'blog/article.html', context=context)
