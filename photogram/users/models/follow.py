from django.db import models
from django.conf import settings

from users.models import User


class Follow(models.Model):
    Follower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
    )
    Followee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
    )

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )
