from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import Article, Tag


def index(request):
    articles4 = Article.objects.filter(is_published=True)[:4]
    context = {
        'title': 'Чисто Блог',
        'articles': articles4,
    }
    return render(request, 'blog/index.html', context)


def articles(request):
    articles = Article.objects.filter(is_published=True)
    paginator = Paginator(articles, 3)
    page_number= request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Статьи',
        'articles': articles,
        'page_obj': page_obj
    }
    return render(request, 'blog/articles.html', context)



def get_tag(request, tag_id):
    articles = Article.objects.filter(is_published=True).filter(tag__id=tag_id)
    tag_name = Tag.objects.get(id=tag_id).title
    context = {
        'title': f'#{tag_name}',
        'articles': articles
    }
    return render(request, 'blog/articles-tag.html', context)

def post(request, post_id):
    article = Article.objects.get(id=post_id)
    context = {
        'title': 'Название стетьи',
        'article': article
    }
    return render(request, 'blog/post.html', context)


def about(request):
    context = {
        'title': 'Обо мне'
    }
    return render(request, 'blog/about.html', context)
