from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Post, Comment


class PostCommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = [
        'content',
    ]
