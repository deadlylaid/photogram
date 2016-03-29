from django.views.generic import DetailView

from .base import PostBaseView


class PostDetailView(PostBaseView, DetailView):
    template_name = "posts/detail.html"
    object_context_name = "post"
    slug_name = "hash_id"
