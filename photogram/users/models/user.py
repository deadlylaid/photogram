from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    description = models.TextField()

    followee_set = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name='follower_set',
        through='Follow',
    )
