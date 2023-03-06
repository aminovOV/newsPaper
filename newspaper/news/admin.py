from django.contrib import admin
from .models import Category, Post, PostCategory, Comment


class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = (PostCategoryInline,)
    list_display = ('post_type', 'display_category', 'headline', 'preview', 'pub_date', 'author', 'rating')
    fields = ('post_type', 'headline', 'body_text', 'author', 'rating')
    list_filter = ('pub_date', 'author', 'rating', 'post_type')
    search_fields = ('headline', 'body_text')
    date_hierarchy = 'pub_date'
    ordering = ['pub_date']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'short_comment_text', 'post', 'date', 'rating')
    list_filter = ('user', 'post', 'date', 'rating')
    search_fields = ('user', 'text')

    @admin.display(description='Текст')
    def short_comment_text(self, obj):
        return obj.text[:32]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
