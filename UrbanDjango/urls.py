from django.contrib import admin
from django.urls import path
from task5 import views as task5_views
from task4 import views as task4_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task5_views.sign_up_by_html, name='sign_up_by_html'),
    path('django_sign_up/', task5_views.sign_up_by_django, name='sign_up_by_django'),
    path('shop/', task4_views.shop, name='shop'),
    path('cart/', task4_views.cart, name='cart'),
]
