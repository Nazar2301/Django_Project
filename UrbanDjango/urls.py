from django.contrib import admin
from django.urls import path
from task4 import views as task4_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task4_views.index, name='index'),
    path('shop/', task4_views.shop, name='shop'),
    path('cart/', task4_views.cart, name='cart'),
]
