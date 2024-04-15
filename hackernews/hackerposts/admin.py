from django.contrib import admin

from .models import Author, Post, Comment

per_page = 10


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_per_page = per_page
    list_display = ('id', 'nickname')
    list_display_links = ('id', 'nickname')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_per_page = per_page
    list_display = ('id', 'title', 'author', 'rating', 'created_at', 'url')
    list_display_links = ('id', 'title')
    ordering = ['created_at', 'title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_per_page = per_page
    list_display = ('id', 'author', 'text','created_at')
    list_display_links = ('id', 'author', 'text','created_at')
