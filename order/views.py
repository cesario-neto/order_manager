from datetime import date
from django.shortcuts import render, redirect
from .models import Order, ProductOrder
from .forms import OrderForms


def index(request):

    context = {
        'orders': Order.objects.filter(created_at__gte=date.today()),
    }

    return render(request, 'order/index.html', context)


def create_order(request):
    Order.objects.create()

    return redirect('order:index')


def order_edit(request, id):
    order = Order.objects.get(pk=id)
    form = OrderForms(instance=order)

    if request.method == 'POST':
        form = OrderForms(request.POST, instance=order)
        if form.is_valid():
            form.save()

    try:
        order_products = order.products.all()
    except ValueError:
        pass

    context = {
        'form': form,
        'order': order,
        'order_products': order_products,
    }

    return render(request, 'order/order.html', context)
