# Generated by Django 3.2.15 on 2022-09-03 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShippingAdress',
            new_name='ShippingAddress',
        ),
    ]
