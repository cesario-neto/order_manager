from django.contrib import admin
from .models import Order, ProductOrder


@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = 'product', 'quantity'
    search_fields = 'product__name',


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'total_value', 'status',
                    'created_at', 'updated_at',)
    search_fields = 'client',
