# Generated by Django 4.2.6 on 2023-10-21 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_order_created_alter_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]