from django.conf.urls import url
from .views import main, photograph, photographs, about, contacts, galery

urlpatterns = [
    url(r'^$', main, name='index'),
    url(r'^about/$', about, name='about'),
    url(r'^photographs/$', photographs, name='photographs'),
    url(r'^photograph/$', photograph, name='photograph'),
    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^galery/$', galery, name='galery')
]
