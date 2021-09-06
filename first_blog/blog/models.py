from django.db import models
from tinymce.models import HTMLField


class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = HTMLField(null=False, blank=False, verbose_name='Текст')
    date_created = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовать')
    tag = models.ManyToManyField('Tag', verbose_name='Тег')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False, unique=True, verbose_name='Заголовок')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']

    def __str__(self):
        return self.title
