from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-pub_date'
    template_name = 'news.html'
    context_object_name = 'posts'


class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
