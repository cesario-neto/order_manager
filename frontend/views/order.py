from django.shortcuts import render, redirect
from order.models import Order, ProductOrder
from order.forms import OrderForms, ProductForms
from django.db import connection


def create_order(request):
    Order.objects.create()

    return redirect('index')


def checkout(request, order_id):
    order = Order.objects.get(id=order_id)
    order.status = 'finalizado'
    order.save()
    return redirect('index')


def delete_order(request, id):
    order = Order.objects.get(pk=id)
    order.delete()

    return redirect('index')


def order_edit(request, id):
    order = Order.objects.prefetch_related('products').get(pk=id)
    form = OrderForms(instance=order)

    if request.method == 'POST':
        form = OrderForms(request.POST, instance=order)
        if form.is_valid():
            form.save()

    try:
        order_products = order.products.select_related('product').all()
    except ValueError:
        pass

    context = {
        'form': form,
        'order': order,
        'order_products': order_products,
    }

    return render(request, 'order/order.html', context)


def add_product(request, id):
    order = Order.objects.prefetch_related('products').get(pk=id)
    products = order.products.select_related('product').all()
    form = ProductForms()

    if request.method == 'POST':
        form = ProductForms(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            order.products.add(product)
            order.save()

    context = {
        'order': order,
        'products': products,
        'form': form
    }

    return render(request, 'order/add_product.html', context)


def delete_product(request, id):
    product = ProductOrder.objects.get(pk=id)
    order = Order.objects.get(products=product)
    product.delete()
    order.save()

    return redirect('order', id=order.id)
