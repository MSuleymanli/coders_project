from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404, redirect
from .models import Portfolio,Product,Agent,Service,Comment
from django.contrib import messages
from .forms import ContactForm,CommentForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request,"homepage.html")

def contact(request):
    return render(request,"contact_us.html")

def agent(request):
    return render(request,"agent.html")

# @login_required(login_url="login")
def agent_details(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Thank you for your message.')
            return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = ContactForm()
    return render(request, 'agent__details.html', {'form': form})

def news(request):
    return render(request,"news.html")

def news_details(request):
    return render(request, "news__details.html")

def wishlist(request):
    return render(request,"wishlist.html")

def my_cart(request):
    return render(request, "my__cart.html")

def services(request):
    return render(request,"services.html")

def about(request):
    agents=Agent.objects.all().order_by('-id')
    services=Service.objects.all()
    products = Product.objects.order_by('?')[:3]
    context={
        "agents":agents,
        "services":services,
        "products":products
    }
    return render(request,"about_us.html",context)

def checkout(request):
    return render (request,"checkout.html")

def google_map(request):
    return render(request,"google_map_location.html")

def our_portfolio(request):
    portfolio_list = Portfolio.objects.all().order_by('-id')
    paginator = Paginator(portfolio_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        "page_obj": page_obj
    }
    return render(request, "our_portfolio.html", context)

def portfolio_details(request, id):
    portfolio_details = get_object_or_404(Portfolio, id=id)
    portfolios = Portfolio.objects.order_by('?')[:3]

    context = {
        "portfolio_details": portfolio_details,
        "portfolios": portfolios
    }

    return render(request, "portfolio_details.html", context)

def product_details(request, id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product_id = id
            comment.save()
            return redirect(request.META.get('HTTP_REFERER', '/'))
    
    promo_product = Product.objects.order_by('?')[:2]
    product = get_object_or_404(Product, id=id)
    portfolios = Portfolio.objects.order_by('?')[:3]
    comments = Comment.objects.filter(product_id=id).order_by('-id')

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
        'portfolios': portfolios,
        'comments': comments
    }
    return render(request, "product_details.html", context)




def clean_key(key):
    return key.replace(' ', '_')

def shop(request):
    property_types = ['House', 'Apartment', 'Single Family', 'Studio']
    statuses = ['Buy', 'Rent', 'Sale']
    amenities = ['Dishwasger', 'Floor Coverings', 'Internet', 'Build Wardrobes', 'Supermarket', 'Kids Zone']
    range=['Low Budget', 'Medium', 'High Budget']
    beth=['Single', 'Double', 'Up to 3', 'Up to 5']

    property_counts = {clean_key(p_type): Product.objects.filter(product_property_type=p_type).count() for p_type in property_types}
    status_counts = {clean_key(status): Product.objects.filter(product_status=status).count() for status in statuses}
    amenities_counts = {clean_key(amen): Product.objects.filter(product_amenities=amen).count() for amen in amenities}
    range_counts = {clean_key(range): Product.objects.filter(product_price_range=range).count() for range in range}
    beth_patch_counts={clean_key(beth): Product.objects.filter(product_beth_patch=beth).count() for beth in beth}
    

    context = {
        'property_counts': property_counts,
        'status_counts': status_counts,
        'amenities_counts': amenities_counts,
        'range_counts':range_counts,
        'beth_patch_counts':beth_patch_counts
    }

    return render(request, 'shop.html', context)


# Contact Form


