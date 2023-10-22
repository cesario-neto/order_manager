from django.db import models
from product.models import Product
from django.dispatch import receiver
from django.db.models.signals import pre_save


class ProductOrder(models.Model):
    class Meta:
        verbose_name = 'Produtos do Pedido'

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=False, null=False,
        verbose_name='Produto')
    quantity = models.IntegerField(verbose_name='Quantidade')

    def __str__(self) -> str:
        return self.product.name


class Order(models.Model):
    class Meta:
        verbose_name = 'Pedido'

    choices = (
        ['pendente', 'Pendente'],
        ['finalizado', 'Finalizado']
    )

    client = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Cliente')
    products = models.ManyToManyField(
        ProductOrder, verbose_name='Produtos', blank=True
    )
    total_value = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True,
        verbose_name='Valor Total')
    status = models.CharField(
        max_length=255, choices=choices, default='pendente')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.client


@receiver(pre_save, sender=Order)
def set_default_value(sender, *args, **kwargs):
    instance = kwargs.get('instance')
    if not instance.client:
        instance.client = 'Sem nome'
    price = 0
    for obj in instance.products.all():
        price += (obj.product.price * obj.quantity)

    instance.total_value = price
