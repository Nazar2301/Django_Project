from django.shortcuts import render
from django.views import View

# Главная страница
def index(request):
    return render(request, 'third_task/index.html')

# Магазин
def shop(request):
    items = ['Товар 1', 'Товар 2', 'Товар 3']
    context = {'items': items}
    return render(request, 'third_task/shop.html', context)

# Корзина
def cart(request):
    return render(request, 'third_task/cart.html')
