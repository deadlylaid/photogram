from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .base import PostBaseView


class PostCreateView(LoginRequiredMixin, PostBaseView, CreateView):

    login_url = '/login/'

    template_name = "posts/new.html"
    fields = [
        'content',
        'image',
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)
