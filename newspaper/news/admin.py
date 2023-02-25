from django.contrib import admin
from .models import Category, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_type', 'headline', 'body_text', 'pub_date', 'author', 'rating')
    list_filter = ('pub_date', 'author', 'rating', 'post_type')
    search_fields = ('headline', 'body_text')
    date_hierarchy = 'pub_date'
    ordering = ['pub_date']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'post', 'date', 'rating')
    list_filter = ('user', 'post', 'date', 'rating')
    search_fields = ('user', 'text')


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
