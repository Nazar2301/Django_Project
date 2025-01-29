from django.contrib import admin
from django.urls import path
from task3 import views as task3_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task3_views.index, name='index'),
    path('shop/', task3_views.shop, name='shop'),
    path('cart/', task3_views.cart, name='cart'),
]
