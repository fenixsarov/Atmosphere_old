from django.conf.urls import url
from .views import Master_Page

urlpatterns = [
    url(r'^$', Master_Page, name='master_page'),
]