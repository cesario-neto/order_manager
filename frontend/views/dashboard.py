from django.shortcuts import render
from order.models import Order
from datetime import date


def index(request):

    context = {
        'orders': Order.objects.filter(created_at__gte=date.today()),
    }

    return render(request, 'order/index.html', context)
