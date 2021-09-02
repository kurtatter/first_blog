from django.db import models


# class Article(models.Model):
#     title = models.CharField(max_length=250)
#     text = models.TextField(null=False, blank=False)
#     date_publication = models.DateTimeField(auto_now=True)
#     tag = models.ForeignKey('Tag', null=True, blank=True, on_delete=models.SET_NULL, default='default')
#
#
# class Tag(models.Model):
#     title = models.CharField(null=False, blank=False, unique=True)
#     article = models.ForeignKey('Article', null=True, blank=True, on_delete=models.SET_NULL, unique=True)
