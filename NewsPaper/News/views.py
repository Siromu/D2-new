from django.views.generic import ListView, DetailView
from .models import Post, Comment


class NewsPost(ListView):
    model = Post
    template_name = 'flatpages/news.html'
    context_object_name = 'News'
    queryset = Post.objects.order_by('-dateCreation')


class NewsID(DetailView):
    model = Post
    template_name = 'flatpages/NewsId.html'
    context_object_name = 'NewsId'


class CommentID(ListView):
    model = Comment
    template_name = 'flatpages/NewsId.html'
    context_object_name = 'CommentId'
    queryset = Post.objects.order_by('-dateCreation')

