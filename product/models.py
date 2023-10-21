from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name = 'Produto'

    name = models.CharField(max_length=255, null=False,
                            blank=False, verbose_name='Nome')
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False,
                                blank=False, verbose_name='Preço')
