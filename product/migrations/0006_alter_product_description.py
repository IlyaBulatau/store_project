# Generated by Django 4.1.5 on 2023-01-14 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.description'),
        ),
    ]
