from django.db import models
from users.user import User


class Post(models.Model):

    user = models.Foreignkey(
        User,
    )

    image = models.ImageField()

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add = True
    )

    updated_at = models.DateTimeField(
        auto_now = True
    )
