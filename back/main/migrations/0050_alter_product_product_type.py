# Generated by Django 5.1 on 2024-08-22 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0049_comment_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
