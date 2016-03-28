from django.apps import AppConfig


class PostAppConfig(AppConfig):

    name = "posts"

    def ready(self):
        from .signals import post_save_post
