from django.conf.urls import url
from MainApp import views


urlpatterns = [
    url(r'^$', views.main, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^photographs/$', views.photographs, name='photographs'),
    url(r'^photograph/$', views.photograph, name='photograph'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^galery/$', views.galery, name='galery'),
    url(r'^request_form/$', views.request_form, name='request_form')
]
