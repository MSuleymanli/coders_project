from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import (
    Portfolio,
    Product,
    Agent,
    Service,
    Comment,
    Wishlist,
    Cart,
    CartItem,
)
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
import stripe # type: ignore
from django.conf import settings
from django.shortcuts import redirect


# Create your views here.


def home(request):
    return render(request, "homepage.html")


def contact(request):
    return render(request, "contact_us.html")


def agent(request):
    return render(request, "agent.html")


# @login_required(login_url="login")
def agent_details(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your message.")
            return redirect(request.META.get("HTTP_REFERER", "/"))
    else:
        form = ContactForm()
    return render(request, "agent__details.html", {"form": form})


def news(request):
    return render(request, "news.html")


def news_details(request):
    return render(request, "news__details.html")


@login_required(login_url="login")
def wishlist(request):
    # Get the current user's wishlist items
    wishlist_items = Wishlist.objects.filter(user=request.user)

    # Pass the wishlist items to the template
    return render(request, "wishlist.html", {"wishlist_items": wishlist_items})


@login_required(login_url="login")
def add_to_wishlist(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user,
        wish_name=product.product_name,
        wish_price=str(product.product_price),
        wish_image=product.product_image,
        product_id=product.id,
    )

    return redirect(request.META.get("HTTP_REFERER", "/"))


def del_wish(request, id):
    wish = get_object_or_404(Wishlist, id=id)
    wish.delete()

    return redirect(request.META.get("HTTP_REFERER", "/"))


def add_to_cart(request, wishlist_id):
    # Get the Wishlist item
    wishlist_item = get_object_or_404(Wishlist, id=wishlist_id)

    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Get or create the CartItem with the correct field name 'wishlist_item'
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, wishlist_item=wishlist_item
    )

    if existing_cart_item := CartItem.objects.filter(
        cart=cart, wishlist_item=wishlist_item  # Corrected: use 'wishlist_item'
    ).first():
        # If it exists, increment its quantity
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    else:
        # If it doesn't exist, create a new CartItem instance
        cart_item = CartItem.objects.create(
            cart=cart, wishlist_item=wishlist_item, quantity=1
        )
        cart_item.save()

    # Update the cart total price
    cart.item_total()  # Use the method 'item_total' to update the cart's total

    return redirect("my_cart")


def my_cart(request):
    # Fetch the user's cart and related items
    cart = Cart.objects.filter(user=request.user).first()
    cart_items = cart.cartitem_set.all()

    # Initialize subtotal and other variables
    shipping_and_handling = 4  # Example value, adjust as needed
    vat_percentage = 1  # Example, you can set VAT as required
    subtotal = 0

    # Calculate subtotal and item totals for all items in the cart
    for item in cart_items:
        item_total = (
            item.calculate_item_total()
        )  # Call the method to calculate the total for each item

        subtotal += item_total

    # Calculate VAT and total price
    vat = (subtotal * vat_percentage) / 100
    total_price = subtotal + shipping_and_handling + vat

    context = {
        "cart": cart,
        "cart_items": cart_items,
        "subtotal": subtotal,
        "shipping_and_handling": shipping_and_handling,
        "vat": vat,
        "total_price": total_price,
    }

    return render(request, "my__cart.html", context)

#My cartdan prduct silende cartdaki melumatlar da sifirlanmalidi yenisi gelenecen de.Yenisi gelende sifirlanmis olur artiq))


def update_quantity(request, item_id, action):
    cart_item = get_object_or_404(CartItem, id=item_id)

    if action == "increase":
        cart_item.quantity += 1
    elif action == "decrease" and cart_item.quantity > 1:
        cart_item.quantity -= 1

    cart_item.save()

    # Update the cart total price
    cart_item.cart.item_total()

    return redirect("my_cart")


def del_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart = cart_item.cart  # Retrieve the associated Cart object
    cart_item.delete()
    return redirect(request.META.get("HTTP_REFERER", "/"))


def services(request):
    return render(request, "services.html")


def services_details(request):
    return render(request, "servicesdetails.html")


def faq(request):
    return render(request, "faq.html")


def contact_us(request):
    return render(request, "contactus.html")


def about(request):

    agents = Agent.objects.all().order_by("?")[:4]
    services = Service.objects.order_by("?")[:6]
    products = Product.objects.order_by("?")[:3]
    wishlist_items = Wishlist.objects.filter(user=request.user)
    wishlist_product_names = wishlist_items.values_list("wish_name", flat=True)

    wishlist_product_names_set = set(wishlist_product_names)

    context = {
        "agents": agents,
        "services": services,
        "products": products,
        "wishlist_product_names_set": wishlist_product_names_set,
    }
    return render(request, "about_us.html", context)


def checkout(request):

    prices=Cart.objects.all()
    context={
        "prices":prices
    }
    return render(request, "checkout.html",context)

# Set your Stripe API key
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def create_checkout_session(request):
    # Fetch the user's cart and calculate the subtotal
    cart = Cart.objects.filter(user=request.user).first()
    cart_items = cart.cartitem_set.all()
    subtotal = sum(item.calculate_item_total() for item in cart_items)

    # Create a new Checkout Session in Stripe
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Cart Subtotal',
                    },
                    'unit_amount': int(subtotal * 100),  # Convert subtotal to cents
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='http://127.0.0.1:8000/checkout-success/',
        cancel_url='http://127.0.0.1:8000/checkout-cancel/',
    )

    # Redirect to the Stripe Checkout page
    return redirect(session.url, code=303)


def checkout_success(request):
    return render(request, "checkout_success.html")

def checkout_cancel(request):
    return render(request, "checkout_cancel.html")




# Set your Stripe API key
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def create_checkout_session(request):
    # Fetch the user's cart and calculate the subtotal
    cart = Cart.objects.filter(user=request.user).first()
    cart_items = cart.cartitem_set.all()
    subtotal = sum(item.calculate_item_total() for item in cart_items)

    # Create a new Checkout Session in Stripe
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Cart Subtotal',
                    },
                    'unit_amount': int(subtotal * 100),  # Convert subtotal to cents
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='http://127.0.0.1:8000/checkout-success/',
        cancel_url='http://127.0.0.1:8000/checkout-cancel/',
    )

    # Redirect to the Stripe Checkout page
    return redirect(session.url, code=303)


def checkout_success(request):
    return render(request, "checkout_success.html")

def checkout_cancel(request):
    return render(request, "checkout_cancel.html")





def google_map(request):
    return render(request, "google_map_location.html")


def our_portfolio(request):
    portfolio_list = Portfolio.objects.all().order_by("-id")
    paginator = Paginator(portfolio_list, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}
    return render(request, "our_portfolio.html", context)


def portfolio_details(request, id):
    portfolio_details = get_object_or_404(Portfolio, id=id)
    portfolios = Portfolio.objects.order_by("?")[:3]

    context = {"portfolio_details": portfolio_details, "portfolios": portfolios}

    return render(request, "portfolio_details.html", context)


def product_details(request, id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product_id = id
            comment.save()
            return redirect(request.META.get("HTTP_REFERER", "/"))

    promo_product = Product.objects.order_by("?")[:2]
    product = get_object_or_404(Product, id=id)
    portfolios = Portfolio.objects.order_by("?")[:3]
    comments = Comment.objects.filter(product_id=id).order_by("-id")

    user = request.user

    if request.GET.get("like"):
        if product.likes.filter(id=user.id).exists():
            # User already liked the product, do nothing
            pass
        else:
            # User hasn't liked the product, create a new Wishlist item
            Wishlist.objects.create(user=user, product=product)
            product.likes.add(user)
            return HttpResponse("Liked!")

    property_types = ["House", "Apartment", "Single Family", "Studio"]
    property_counts = {
        clean_key(p_type): Product.objects.filter(product_property_type=p_type).count()
        for p_type in property_types
    }

    wishlist_items = Wishlist.objects.filter(user=request.user)
    wishlist_product_names = wishlist_items.values_list("wish_name", flat=True)

    wishlist_product_names_set = set(wishlist_product_names)

    for comment in comments:
        try:
            com_rate = int(comment.com_rate)
        except ValueError:
            com_rate = 0

        comment.full_star_range = range(com_rate)
        comment.empty_star_range = range(5 - com_rate)

    context = {
        "product": product,
        "promo_product": promo_product,
        "portfolios": portfolios,
        "comments": comments,
        "property_counts": property_counts,
        "wishlist_product_names_set": wishlist_product_names_set,
    }
    return render(request, "product_details.html", context)


def clean_key(key):
    return key.replace(" ", "_")


def shop(request):
    property_types = ["House", "Apartment", "Single Family", "Studio"]
    statuses = ["Buy", "Rent", "Sale"]
    amenities = [
        "Dishwasger",
        "Floor Coverings",
        "Internet",
        "Build Wardrobes",
        "Supermarket",
        "Kids Zone",
    ]
    range = ["Low Budget", "Medium", "High Budget"]
    beth = ["Single", "Double", "Up to 3", "Up to 5"]

    property_counts = {
        clean_key(p_type): Product.objects.filter(product_property_type=p_type).count()
        for p_type in property_types
    }
    status_counts = {
        clean_key(status): Product.objects.filter(product_status=status).count()
        for status in statuses
    }
    amenities_counts = {
        clean_key(amen): Product.objects.filter(product_amenities=amen).count()
        for amen in amenities
    }
    range_counts = {
        clean_key(range): Product.objects.filter(product_price_range=range).count()
        for range in range
    }
    beth_patch_counts = {
        clean_key(beth): Product.objects.filter(product_beth_patch=beth).count()
        for beth in beth
    }

    context = {
        "property_counts": property_counts,
        "status_counts": status_counts,
        "amenities_counts": amenities_counts,
        "range_counts": range_counts,
        "beth_patch_counts": beth_patch_counts,
    }

    return render(request, "shop.html", context)


# Register
def register__view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        last_name = form.cleaned_data.get("last_name")
        email = form.cleaned_data.get("email")

        # Create new User object and set all fields
        newUser = User(
            username=username,
            last_name=last_name,
            email=email,
        )
        newUser.set_password(password)
        newUser.save()

        login(request, newUser)
        messages.success(request, "Siz uÄŸurla qeydiyyatdan keÃ§diniz...")
        return redirect("about")

    context = {"form": form}
    return render(request, "register.html", context)


def login__view(request):
    form = LoginForm(request.POST or None)

    context = {"form": form}

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            return render(request, "login.html", context)

        login(request, user)
        messages.success(request, "Siz uğurla daxil oldunuz...")
        return redirect("homepage")
    return render(request, "login.html", context)


def logout__view(request):
    logout(request)
    return redirect("shop")


def billing_view(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = BillingForm()

    return render(request, 'billing_form.html', {'form': form})
    
