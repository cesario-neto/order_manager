from datetime import date
from django.shortcuts import render
from .models import Order, ProductOrder


def index(request):

    context = {
        'orders': Order.objects.filter(created_at__gte=date.today())
    }

    return render(request, 'order/index.html', context)

# def
