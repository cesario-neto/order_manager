# Generated by Django 4.2.6 on 2023-10-21 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço')),
            ],
            options={
                'verbose_name': 'Produto',
            },
        ),
    ]