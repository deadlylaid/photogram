from django.conf.urls import url
from django.contrib import admin
from users.views import *
from photogram.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', LoginView.as_view()),

    url(r'^$', HomeView.as_view(), name='home'),
]
