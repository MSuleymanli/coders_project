from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Portfolio(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    portfolio_image = models.ImageField(
        upload_to="portfolio_images/",
        blank=True,
        null=True,
        verbose_name="Portfolio Image",
    )
    created_date = models.DateTimeField(auto_now_add=True)
    portfolio_name = models.CharField(max_length=30, blank=True, null=True)
    portfolio_image_detail = models.TextField(blank=True, null=True)
    portfolio_detail = models.TextField(blank=True, null=True)
    portfolio_about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.portfolio_name


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(
        Portfolio, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="portfolio_images/", blank=True, null=True)

    class Meta:
        ordering = ["id"]


class Product(models.Model):
    product_image = models.ImageField(
        upload_to="product_images/", blank=True, null=True, verbose_name="Product Image"
    )
    product_name = models.CharField(max_length=30, blank=True, null=True)
    product_location = models.CharField(max_length=30, blank=True, null=True)
    product_type = models.CharField(max_length=10, blank=True, null=True)
    product_about = models.TextField(blank=True, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    product_bath_count = models.IntegerField(default=0)
    product_bed_count = models.IntegerField(default=0)
    product_ft = models.IntegerField(default=0)
    product_build_year = models.IntegerField(default=0)
    product_property_type = models.CharField(max_length=20, blank=True, null=True)
    product_amenities = models.CharField(max_length=20, blank=True, null=True)
    product_price_range = models.CharField(max_length=20, blank=True, null=True)
    product_beth_patch = models.CharField(max_length=20, blank=True, null=True)
    product_status = models.CharField(max_length=10, blank=True, null=True)
    inWishlist=models.BooleanField(default=False)

    def update_wishlist_status(self, user):
        self.inWishlist = Wishlist.objects.filter(user=user, product=self).exists()
        self.save()

    def __str__(self):
        return self.product_name or ""


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="product_images/", blank=True, null=True)

    class Meta:
        ordering = ["id"]


class Agent(models.Model):
    agent_image = models.FileField(
        upload_to="product_image", blank=True, null=True, verbose_name="Product Image"
    )
    agent_name = models.CharField(max_length=30, blank=True, null=True)
    agent_surname = models.CharField(max_length=30, blank=True, null=True)
    agent_job_title = models.CharField(max_length=30, blank=True, null=True)
    agent_about = models.TextField(blank=True, null=True)
    agent_details = models.TextField(blank=True, null=True)
    agent_img_detail = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.agent_name


class Service(models.Model):
    service_name = models.CharField(max_length=30, blank=True, null=True)
    service_about = models.TextField(blank=True, null=True)
    svg_code = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.service_name


class Customer(models.Model):
    customer_name = models.CharField(max_length=20, blank=True, null=True)
    customer_surname = models.CharField(max_length=20, blank=True, null=True)
    customer_email = models.EmailField(max_length=40)
    customer_coupon = models.IntegerField(default=0)
    customer_phone = models.IntegerField(default=0)
    customer_service = models.CharField(max_length=30, blank=True, null=True)
    customer_country = models.CharField(max_length=20, blank=True, null=True)
    customer_street = models.CharField(max_length=20, blank=True, null=True)
    customer_apartment = models.CharField(max_length=20, blank=True, null=True)
    customer_state = models.CharField(max_length=20, blank=True, null=True)
    customer_zip = models.CharField(max_length=20, blank=True, null=True)
    customer_cash = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    customer_note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.customer_name


# Contact Form Model


class ContactSubmission(models.Model):
    class ServiceType(models.TextChoices):
        F = "F", "Freemium"
        P = "P", "Premium"

    name = models.CharField(max_length=100, verbose_name=("Name"))
    email = models.EmailField()
    service = models.CharField(
        max_length=1, verbose_name="Select Service Type", choices=ServiceType.choices
    )
    message = models.TextField(max_length=200, verbose_name=("Message"))
    phone = models.CharField(max_length=50, verbose_name=("Your Phone Number"))
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} --- {self.email}"


class Comment(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comments", default=1
    )
    com_name = models.CharField(max_length=20)
    com_email = models.EmailField(max_length=40)
    com_message = models.CharField(max_length=300)
    com_created = models.DateField(auto_now_add=True)
    com_rate = models.CharField(max_length=2, default=0, blank=True, null=True)

    def __str__(self):

        return self.com_name


class Wishlist(models.Model):

    STATUS_CHOICES = [
        ("in_stock", "In Stock"),
        ("coming_soon", "Coming Soon"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    wish_image = models.FileField(
        upload_to="wish_image", blank=True, null=True, verbose_name="Wish Image"
    )
    wish_name = models.CharField(max_length=20, blank=True, verbose_name="Wish Name")
    wish_price = models.DecimalField(max_digits=10, decimal_places=2)
    wish_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="coming_soon",
        verbose_name="Wish Status",
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.product.update_wishlist_status(self.user)

    def delete(self, *args, **kwargs):
        user = self.user
        product = self.product
        super().delete(*args, **kwargs)
        product.update_wishlist_status(user)
    
    def __str__(self):
        return f"{self.user} -- {self.wish_name}"


# class 
# 
# (models.Model):
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

    wishlist_products = models.ManyToManyField(
        Wishlist,
        through="CartItem",
        through_fields=("cart", "wishlist_item"),
        related_name="carts",
    )

    subtotal = models.PositiveBigIntegerField(default=0, blank=True, null=True)
    ship_hand = models.PositiveSmallIntegerField(default=5, blank=True, null=True)
    vat = models.PositiveIntegerField(default=10, blank=True, null=True)
    total_price = models.PositiveIntegerField(default=0, blank=True, null=True)

    def item_total(self):
        # Calculate the total price of all items in the cart
        total = sum(
            item.quantity * float(item.wishlist_item.wish_price)  # Use wishlist_item
            for item in self.cartitem_set.all()
        )
        self.total_price = total  # Save the total price in the cart's total_price field


        # Update subtotal with the sum of total_price, ship_hand, and vat
        self.subtotal = self.total_price + (self.ship_hand or 0) + (self.vat or 0)

        self.save()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    wishlist_item = models.ForeignKey(
        Wishlist, on_delete=models.CASCADE
    )  # Reference to Wishlist
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.PositiveIntegerField(default=0)

    def calculate_item_total(self):
        # Calculate the total for this cart item using wishlist_item
        self.item_total = self.quantity * float(self.wishlist_item.wish_price)
        return self.item_total



class Billing(models.Model):
    per_name=models.CharField(max_length=20,blank=True,null=True)
    per_email=models.EmailField(blank=True,null=True)
    per_number=models.IntegerField(default=0,blank=True,null=True)
    per_service_type=models.CharField(max_length=20,blank=True,null=True)
    per_country=models.CharField(max_length=20,blank=True,null=True)
    per_house_number=models.CharField(max_length=20,blank=True,null=True)
    per_apartment=models.CharField(max_length=20,blank=True,null=True)
    per_town=models.CharField(max_length=20,blank=True,null=True)
    per_city=models.CharField(max_length=20,blank=True,null=True)
    per_zip=models.CharField(max_length=20,blank=True,null=True)
    per_notes=models.TextField(blank=True,null=True)
    per_payment_method=models.CharField(max_length=20,blank=True,null=True)
    per_card_subtotal=models.PositiveIntegerField(default=0,blank=True,null=True)
    per_ship_hand=models.PositiveIntegerField(default=0,blank=True,null=True)
    per_vat=models.PositiveIntegerField(default=0,blank=True,null=True)
    per_order_total=models.PositiveIntegerField(default=0,blank=True,null=True)
    
    def __str__(self):
        return self.per_name
    
    
