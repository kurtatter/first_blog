from django.contrib import admin

from .models import Article, Tag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'date_created', 'is_published')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('title', 'text')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
