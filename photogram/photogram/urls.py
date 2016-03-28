from django.conf.urls import url
from django.contrib import admin
from users.views import user

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', user),
]
