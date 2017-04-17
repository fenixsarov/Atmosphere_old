from django.conf.urls import url
from .views import main, photograph, photographs, about

urlpatterns = [
    url(r'^$', main, name='index'),
    url(r'^photographs/$', photographs, name='photographs'),
    url(r'^photograph/$', photograph, name='photograph'),
    url(r'^about/$', about, name='about')
]