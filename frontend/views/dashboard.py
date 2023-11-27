from django.shortcuts import render
from order.models import Order
from django.core.paginator import Paginator


def index(request):

    orders = Order.objects.all().order_by('-created_at').order_by('-status')
    paginator = Paginator(orders, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'orders': orders,
        'page_obj': page_obj,
    }

    return render(request, 'order/index.html', context)
