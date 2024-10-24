# Generated by Django 5.1 on 2024-09-18 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_cart_ship_hand_cart_subtotal_cart_vat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='ship_hand',
            field=models.PositiveSmallIntegerField(blank=True, default=5, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='vat',
            field=models.PositiveIntegerField(blank=True, default=10, null=True),
        ),
    ]