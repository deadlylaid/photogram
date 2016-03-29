from django.conf.urls import url
from django.contrib import admin

from photogram.views import *
from users.views import *
from posts.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^signup/$', SignupView.as_view(), name='signup'),

    url(r'^posts/$', PostListView.as_view(), name="list"),
    url(r'^posts/new/$', PostCreateView.as_view(), name="new-post"),
    url(r'^posts/(?P<pk>\d+)/$', PostDetailView.as_view(), name="post"),
    url(r'^posts/(?P<pk>\d+)/comments/$', PostCommentCreateView.as_view(), name="comment"),

    url(r'^(?P<slug>\w+)/$', ProfileView.as_view(), name='profile'),

    ]
