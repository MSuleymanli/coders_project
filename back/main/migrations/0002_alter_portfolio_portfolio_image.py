# Generated by Django 5.0.8 on 2024-08-08 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio_image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio_images', verbose_name='Photo'),
        ),
    ]