from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.articles, name='articles'),
    path('articles/tag/<int:tag_id>', views.get_tag, name='tag'),
    path('post/<int:post_id>', views.post, name='post'),
    path('about/', views.about, name='about'),
]
