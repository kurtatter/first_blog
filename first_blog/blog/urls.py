from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.articles, name='articles'),
    path('post/', views.post, name='post'),
    path('about/', views.about, name='about'),
]
