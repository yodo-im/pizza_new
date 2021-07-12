from django.urls import path, re_path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    re_path('add/(?P<house_id>[0-9]+)/$',views.cart_add),
    path('remove/<int:product_id>/',
         views.cart_remove,
         name='cart_remove'),
]