from django.shortcuts import render

# Главная страница
def index(request):
    return render(request, 'fourth_task/index.html')

# Магазин
def shop(request):
    games = ['Atomic Heart', 'Cyberpunk 2077']
    context = {'games': games}
    return render(request, 'fourth_task/shop.html', context)

# Корзина
def cart(request):
    return render(request, 'fourth_task/cart.html')
