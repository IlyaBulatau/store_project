# Generated by Django 4.1.5 on 2023-01-15 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
