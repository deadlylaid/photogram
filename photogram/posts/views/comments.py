from django.views.generic import CreateView
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

from posts.models import Post, Comment


@method_decorator(require_POST, name="dispatch")
class PostCommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = [
        'content',
    ]

    def form_valid(self, form):
        post = Post.objects.get(
            hash_id=self.kwargs.get('slug'),
        )

        form.instance.post = post
        form.instance.user = self.request.user

        return super(PostCommentCreateView, self).form_valid(form)

    def get_success_url(self):
        post = Post.objects.get(
            hash_id=self.kwargs.get('slug'),
        )
        return post.get_absolute_url()
