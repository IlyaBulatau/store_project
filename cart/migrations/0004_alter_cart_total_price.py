# Generated by Django 4.1.5 on 2023-01-15 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cart_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]