from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^api/(?P<api>[a-zA-Z0-9]*)/(?P<args>\S*)/$', views.proxy, name='proxy'),
]
