from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Portfolio(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    portfolio_image = models.ImageField(upload_to="portfolio_images/", blank=True, null=True, verbose_name="Portfolio Image")
    created_date = models.DateTimeField(auto_now_add=True)
    portfolio_name = models.CharField(max_length=30, blank=True, null=True)
    portfolio_image_detail = models.TextField(blank=True,null=True)
    portfolio_detail = models.TextField(blank=True,null=True)
    portfolio_about = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.portfolio_name
    
class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)
    
    class Meta:
        ordering = ['id']
    
class Product(models.Model):
    product_image = models.ImageField(upload_to="product_images/", blank=True, null=True, verbose_name="Product Image")
    product_name = models.CharField(max_length=30,blank=True,null=True)
    product_location = models.CharField(max_length=30,blank=True,null=True)
    product_type = models.CharField(max_length=10,blank=True,null=True)
    product_about = models.TextField(blank=True, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    product_bath_count = models.IntegerField(default=0)
    product_bed_count = models.IntegerField(default=0)
    product_ft = models.IntegerField(default=0)
    product_build_year = models.IntegerField(default=0)
    product_property_type=models.CharField(max_length=20,blank=True,null=True)
    product_amenities=models.CharField(max_length=20,blank=True,null=True)
    product_price_range=models.CharField(max_length=20,blank=True,null=True)
    product_beth_patch=models.CharField(max_length=20,blank=True,null=True)
    product_status=models.CharField(max_length=10,blank=True,null=True)    

    def __str__(self):
        return self.product_name or ""
    



class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    
    class Meta:
        ordering = ['id']
        
        
   
class Agent(models.Model):
    agent_image=models.FileField(upload_to="product_image",blank=True,null=True,verbose_name="Product Image")   
    agent_name=models.CharField(max_length=30,blank=True,null=True)
    agent_surname=models.CharField(max_length=30,blank=True,null=True)
    agent_job_title=models.CharField(max_length=30,blank=True,null=True) 
    agent_about=models.TextField(blank=True,null=True)
    agent_details=models.TextField(blank=True,null=True)
    agent_img_detail=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.agent_name
    
       
class Service(models.Model):
    service_name=models.CharField(max_length=30,blank=True,null=True)
    service_about=models.TextField(blank=True,null=True)
    svg_code = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.service_name
    
class Customer(models.Model):
    customer_name=models.CharField( max_length=20,blank=True,null=True)
    customer_surname=models.CharField( max_length=20,blank=True,null=True)
    customer_email=models.EmailField(max_length=40)
    customer_coupon=models.IntegerField(default=0)
    customer_phone=models.IntegerField(default=0)
    customer_service=models.CharField(max_length=30,blank=True,null=True)
    customer_country=models.CharField(max_length=20,blank=True,null=True)
    customer_street=models.CharField(max_length=20,blank=True,null=True)
    customer_apartment=models.CharField(max_length=20,blank=True,null=True)
    customer_state=models.CharField(max_length=20,blank=True,null=True)
    customer_zip=models.CharField(max_length=20,blank=True,null=True)
    customer_cash=models.DecimalField(max_digits=10, decimal_places=3, default=0)
    customer_note=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.customer_name
    
    
# Contact Form Model

class ContactSubmission(models.Model):
    class ServiceType(models.TextChoices):
        F = 'F', 'Freemium'
        P = 'P',  'Premium'
        
    name = models.CharField(max_length=100, verbose_name=("Name"))
    email = models.EmailField()
    service = models.CharField(max_length=1, verbose_name="Select Service Type", choices=ServiceType.choices)
    message = models.TextField(max_length=200, verbose_name=("Message"))
    phone = models.CharField( max_length=50, verbose_name=("Your Phone Number"))
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} --- {self.email}"
    
    
class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', default=1)
    com_name=models.CharField(max_length=20)
    com_email=models.EmailField(max_length=40)
    com_message=models.CharField(max_length=300)
    com_created=models.DateField(auto_now_add=True)
    com_rate=models.CharField(max_length=2,default=0,blank=True,null=True)
    
    def __str__(self):

        return self.com_name   
    
    
class Wishlist(models.Model):

    STATUS_CHOICES = [
        ('in_stock', 'In Stock'),
        ('coming_soon', 'Coming Soon'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    wish_image = models.FileField(upload_to="wish_image", blank=True, null=True, verbose_name="Wish Image")
    wish_name = models.CharField(max_length=20, blank=True, verbose_name="Wish Name")
    wish_price = models.CharField(max_length=20, blank=True, null=True, verbose_name="Wish Price")
    wish_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='coming_soon', verbose_name="Wish Status")
    
    def __str__(self):
        return f"{self.user} -- {self.wish_name}"
    

# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Wishlist, through='CartItem')

#     def total_price(self):
#         return sum(item.product.wish_price * item.quantity for item in self.cartitem_set.all())
    
#     def __str__(self):
#         return f"Cart of {self.user}"



# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return f"{self.product.wish_name} in cart"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wishlist_products = models.ManyToManyField(Wishlist, through="CartItem")
    total_price = models.PositiveIntegerField(default=0)

    def item_total(self):
        self.item_total = sum(item.quantity * float(item.wishlist_item.wish_price) for item in self.cartitem_set.all())
        self.save()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    wishlist_item = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.PositiveIntegerField(default=0)



    def calculate_item_total(self):
        self.item_total = self.quantity * float(self.wishlist_item.wish_price)
        return self.item_total   

    