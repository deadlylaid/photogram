from django.db import models
from django.conf import settings
from tags.models import Tag


class Post(models.Model):
    hash_id = models.CharField(
        max_length=8,
        null=True,
        blank=True,
        unique=True,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    image = models.ImageField()

    content = models.TextField()

    tag_set = models.ManyToManyField(
        Tag,
        blank=True,
    )

    like_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_post_set',
        through="Like",
    )

    @property
    def tagified_content(self):
        return self.content.replace("#핵폭탄", "<a href='/eae/'>#핵폭탄</a>")

    created_at = models.DateTimeField(auto_now_add=True,)

    updated_at = models.DateTimeField(auto_now=True,)

    def get_hash_id(self):
        from photogram.utils.hash_id import get_hash_id
        self.hash_id = get_hash_id(self)
        self.save()

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse(
                "post",
                kwargs={
                    "slug": self.hash_id,
                }
        )
