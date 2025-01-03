from django.shortcuts import render

from .models import Pizza
# Create your views here.

def index(request):
    """ピザノートのホームページ"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """ピザの種類を表示する"""
    pizzas = Pizza.objects
    context = {'pizzas':pizzas}
    return render(request, 'pizzas/pizzas_menu.html', context)
