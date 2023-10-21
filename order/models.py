from django.db import models
from product.models import Product


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
        ['Pendente', 'pendente'],
        ['Finalizado', 'finalizado']
    )

    client = models.CharField(max_length=255, verbose_name='Cliente')
    products = models.ManyToManyField(
        ProductOrder, verbose_name='Produtos'
    )
    total_value = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name='Valor Total')
    status = models.CharField(
        max_length=255, choices=choices, default='pendente')

    def __str__(self) -> str:
        return self.client
