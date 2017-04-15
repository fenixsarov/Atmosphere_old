from django.conf.urls import url
from .views import main
from .views import photograph
from .views import about

urlpatterns = [
    url(r'^$', main, name='index'),
    url(r'^photographs', photograph, name='photograph'),
    url(r'^photographs/', photograph, name='photograph'),
    url(r'^about', about, name='about')
]