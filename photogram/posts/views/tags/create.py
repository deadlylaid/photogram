from django.views.generic import View
from django.shortcuts import redirect

from posts.models import Post
from tags.models import Tag


class PostTagCreateView(View):

    def get(self, request, *args, **kwargs):
        post = Post.objects.get(
            hash_id=self.kwargs.get('slug'),
        )
