# Generated by Django 5.1 on 2024-08-29 10:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wish_image', models.FileField(blank=True, null=True, upload_to='wish_image', verbose_name='Wish Image')),
                ('wish_name', models.CharField(blank=True, max_length=20, verbose_name='Wish Name')),
                ('wish_price', models.CharField(blank=True, max_length=20, null=True, verbose_name='Wish Price')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
