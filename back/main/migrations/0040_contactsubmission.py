# Generated by Django 3.2.25 on 2024-08-19 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_alter_portfolio_portfolio_about_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=254)),
                ('service', models.CharField(choices=[('F', 'Freemium'), ('P', 'Premium')], max_length=1, verbose_name='Select Service Type')),
                ('message', models.TextField(max_length=200, verbose_name='Message')),
                ('phone', models.CharField(max_length=50, verbose_name='Your Phone Number')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
