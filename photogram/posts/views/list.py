from django.views.generic import ListView

from .base import PostBaseView
from django.http import HttpResponse


class PostListView(PostBaseView, ListView):
    template_name = "posts/list.html"
    context_object_name = "posts"
