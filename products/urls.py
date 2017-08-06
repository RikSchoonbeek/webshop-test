from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.show_products, name='all_products'),
    url(r'^(food)/$', views.show_food, name='show_food'),
    url(r'^(non-food)/$', views.show_non_food, name='show_non_food'),
    url(r'(?P<pk>\d+)/$', views.product_details, name='product_details'),
]