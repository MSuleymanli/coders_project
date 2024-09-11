
# Generated by Django 5.1 on 2024-08-27 16:21


import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_image', models.FileField(blank=True, null=True, upload_to='product_image', verbose_name='Product Image')),
                ('agent_name', models.CharField(blank=True, max_length=30, null=True)),
                ('agent_surname', models.CharField(blank=True, max_length=30, null=True)),
                ('agent_job_title', models.CharField(blank=True, max_length=30, null=True)),
                ('agent_about', models.TextField(blank=True, null=True)),
                ('agent_details', models.TextField(blank=True, null=True)),
                ('agent_img_detail', models.TextField(blank=True, null=True)),
            ],
        ),
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
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_surname', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_email', models.EmailField(max_length=40)),
                ('customer_coupon', models.IntegerField(default=0)),
                ('customer_phone', models.IntegerField(default=0)),
                ('customer_service', models.CharField(blank=True, max_length=30, null=True)),
                ('customer_country', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_street', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_apartment', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_state', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_zip', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_cash', models.DecimalField(decimal_places=3, default=0, max_digits=10)),
                ('customer_note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
<<<<<<< HEAD
=======
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_images/', verbose_name='Product Image')),
                ('product_name', models.CharField(blank=True, max_length=30, null=True)),
                ('product_location', models.CharField(blank=True, max_length=30, null=True)),
                ('product_type', models.CharField(blank=True, max_length=10, null=True)),
                ('product_about', models.TextField(blank=True, null=True)),
                ('product_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('product_bath_count', models.IntegerField(default=0)),
                ('product_bed_count', models.IntegerField(default=0)),
                ('product_ft', models.IntegerField(default=0)),
                ('product_build_year', models.IntegerField(default=0)),
                ('product_property_type', models.CharField(blank=True, max_length=20, null=True)),
                ('product_amenities', models.CharField(blank=True, max_length=20, null=True)),
                ('product_price_range', models.CharField(blank=True, max_length=20, null=True)),
                ('product_beth_patch', models.CharField(blank=True, max_length=20, null=True)),
                ('product_status', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
>>>>>>> e695735 (new branch)
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(blank=True, max_length=30, null=True)),
                ('service_about', models.TextField(blank=True, null=True)),
                ('svg_code', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_image', models.ImageField(blank=True, null=True, upload_to='portfolio_images/', verbose_name='Portfolio Image')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('portfolio_name', models.CharField(blank=True, max_length=30, null=True)),
                ('portfolio_image_detail', models.TextField(blank=True, null=True)),
                ('portfolio_detail', models.TextField(blank=True, null=True)),
                ('portfolio_about', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='portfolio_images/')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.portfolio')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_images/', verbose_name='Product Image')),
                ('product_name', models.CharField(blank=True, max_length=30, null=True)),
                ('product_location', models.CharField(blank=True, max_length=30, null=True)),
                ('product_type', models.CharField(blank=True, max_length=10, null=True)),
                ('product_about', models.TextField(blank=True, null=True)),
                ('product_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('product_bath_count', models.IntegerField(default=0)),
                ('product_bed_count', models.IntegerField(default=0)),
                ('product_ft', models.IntegerField(default=0)),
                ('product_build_year', models.IntegerField(default=0)),
                ('product_property_type', models.CharField(blank=True, max_length=20, null=True)),
                ('product_amenities', models.CharField(blank=True, max_length=20, null=True)),
                ('product_price_range', models.CharField(blank=True, max_length=20, null=True)),
                ('product_beth_patch', models.CharField(blank=True, max_length=20, null=True)),
                ('product_status', models.CharField(blank=True, max_length=10, null=True)),
                ('likes', models.ManyToManyField(related_name='product_like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_name', models.CharField(max_length=20)),
                ('com_email', models.EmailField(max_length=40)),
                ('com_message', models.CharField(max_length=300)),
                ('com_created', models.DateField(auto_now_add=True)),
                ('com_rate', models.CharField(blank=True, default=0, max_length=2, null=True)),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(to='main.product')),
            ],
        ),
        migrations.CreateModel(
=======
>>>>>>> e695735 (new branch)
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.product')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
<<<<<<< HEAD
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wish_image', models.FileField(blank=True, null=True, upload_to='wish_image', verbose_name='Wish Image')),
                ('wish_name', models.CharField(blank=True, max_length=20, verbose_name='Wish Name')),
                ('wish_price', models.CharField(blank=True, max_length=20, null=True, verbose_name='Wish Price')),
                ('wish_status', models.CharField(choices=[('in_stock', 'In Stock'), ('coming_soon', 'Coming Soon')], default='coming_soon', max_length=20, verbose_name='Wish Status')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
=======
>>>>>>> e695735 (new branch)
    ]
