# Generated by Django 5.0.8 on 2024-08-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_product_product_sale_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_sale_type',
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.TextField(blank=True),
        ),
    ]