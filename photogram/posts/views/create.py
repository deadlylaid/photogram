from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .base import PostBaseView


class PostCreateView(LoginRequiredMixin, PostBaseView, CreateView):
    template_name = "posts/new.html"
    fields = [
        'content',
    ]
