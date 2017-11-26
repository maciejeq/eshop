from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^order/$', views.order_create, name='order_create'),
    url(r'^add/(?P<product_id>\d+)/$', views.admin_order_detail, name='admin_order_detail'),
    url(r'^remove/(?P<product_id>\d+)/$', views.admin_order_pdf, name='admin_order_pdf'),
]
