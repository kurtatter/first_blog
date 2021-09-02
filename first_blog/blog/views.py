from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title': 'Чисто Блог'
    }
    return render(request, 'blog/index.html', context)


def articles(request):
    context = {
        'title': 'Статьи'
    }
    return render(request, 'blog/articles.html', context)


def post(request):
    context = {
        'title': 'Название стетьи'
    }
    return render(request, 'blog/post.html', context)


def about(request):
    context = {
        'title': 'Обо мне'
    }
    return render(request, 'blog/about.html', context)
