# Generated by Django 5.0.8 on 2024-08-09 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_remove_product_product_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_status',
            field=models.TextField(blank=True, null=True),
        ),
    ]