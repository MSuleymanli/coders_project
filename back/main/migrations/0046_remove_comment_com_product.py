# Generated by Django 5.1 on 2024-08-21 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_alter_comment_com_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='com_product',
        ),
    ]
