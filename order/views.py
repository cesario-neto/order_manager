from datetime import date
from django.shortcuts import render, redirect
from .models import Order, ProductOrder


def index(request):

    context = {
        'orders': Order.objects.filter(created_at__gte=date.today()),
    }

    return render(request, 'order/index.html', context)


def create_order(request):
    Order.objects.create()

    return redirect('order:index')


def order_edit(request, id):
    return render(request, 'order/order.html')
