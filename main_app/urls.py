from django.conf.urls import url
from .views import index
from .views import post_relief_effort

urlpatterns = [
    url(r'^$', index),
    url(r'^post_url/$', post_relief_effort, name="post_relief_effort")
]
