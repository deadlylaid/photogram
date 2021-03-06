from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        'user',

        'content',

        'created_at',
        'updated_at',
    )
