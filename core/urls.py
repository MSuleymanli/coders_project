"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkout/', checkout, name='checkout'),
    path('google_map/', google_map, name='google_map'),
    path('our_portfolio/', our_portfolio, name='our_portfolio'),
    path('portfolio_details/<int:id>/', portfolio_details, name='portfolio_details'),
    path('product_details/<int:id>/', product_details, name='product_details'),
    path('shop/', shop, name='shop'),
    path('',home,name='homepage'),
    path('about/', about, name='about'),
    path('agent/',agent,name='agent'),
    path('agent_details/', agent_details, name='agent_details'),
    path('news/',news,name='news'),
    path('news_details/', news_details, name='news_details'),
    path('my_cart/', my_cart, name='my_cart'),
    path('add_to_cart/<int:wishlist_id>/', add_to_cart, name='add_to_cart'),
    path('services/',services,name='services'),    
    path('update_quantity/<int:item_id>/<str:action>/', update_quantity, name='update_quantity'),
    path('my_cart/del/<int:cart_item_id>/', del_cart, name='del-cart'),
    path('services/',services,name='services'),
    path('wishlist/', wishlist, name='wishlist'),
    path('services_details/', services_details, name='services_details'),
    path('pro-api/',include('main.api.urls')),
    path('register/', register__view, name='register'),
    path('login/',login__view, name='login'), 
    path('logout/',logout__view,name='logout'),
    path('logout/', logout__view, name='logout'),
    path('faq/', faq, name='faq'),
    path('contact_us/', contact_us, name='contact_us'),
    path('contact/',contact,name='contact'),
    path('wishlist/add/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/del/<int:id>/', del_wish, name='del-wish'), 
    # path('checkout/', billing_view, name='billing_view'),



]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)