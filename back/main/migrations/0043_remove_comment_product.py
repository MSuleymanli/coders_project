# Generated by Django 5.1 on 2024-08-20 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_comment_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='product',
        ),
    ]
