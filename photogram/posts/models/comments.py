from django.db import models
from django.conf import settings


class Comment(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    post = models.ForeignKey(
        "Post",
    )

    content = models.Textfield()

    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)
