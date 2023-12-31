from django.shortcuts import render, redirect, get_object_or_404
from order.models import Order, ProductOrder
from order.forms import OrderForms, ProductForms


def create_order(request):
    Order.objects.create()

    return redirect('index')


def checkout(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'finalizado'
    order.save()
    return redirect('index')


def delete_order(request, id):
    order = get_object_or_404(Order, pk=id)
    order.delete()

    return redirect('index')


def order_edit(request, id):
    order = get_object_or_404(
        Order.objects.prefetch_related('products').all(), pk=id)
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
    order = get_object_or_404(
        Order.objects.prefetch_related('products').all(), pk=id)
    products = order.products.select_related('product').all()

    if request.method == 'POST':
        form = ProductForms(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            order.products.add(product)
            order.save()

    form = ProductForms()

    context = {
        'order': order,
        'products': products,
        'form': form
    }

    return render(request, 'order/add_product.html', context)


def decrease_quantity(request, order_id, product_id):
    order = get_object_or_404(Order, pk=order_id)
    product = get_object_or_404(ProductOrder, pk=product_id)
    product.quantity -= 1
    product.save()
    if product.quantity <= 0:
        product.delete()
    order.save()

    return redirect('add_product', id=order_id)


def increase_quantity(request, order_id, product_id):
    order = get_object_or_404(Order, pk=order_id)
    product = get_object_or_404(ProductOrder, pk=product_id)
    product.quantity += 1
    product.save()
    order.save()

    return redirect('add_product', id=order_id)
