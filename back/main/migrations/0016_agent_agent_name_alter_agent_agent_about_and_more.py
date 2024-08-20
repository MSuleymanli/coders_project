# Generated by Django 5.0.8 on 2024-08-09 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='agent_name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='agent_about',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='agent_details',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='agent_img_detail',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]