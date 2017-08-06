from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.sellers, name='sellers'),
    url(r'(?P<id>\d+)/$', views.seller_details, name='seller_details'),
]