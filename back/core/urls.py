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
    path('about', about, name='about'),
    path('checkout/', checkout, name='checkout'),
    path('google_map/', google_map, name='google_map'),
    path('our_portfolio/', our_portfolio, name='our_portfolio'),
    path('portfolio_details/<int:id>/', portfolio_details, name='portfolio_details'),
    path('product_details/<int:id>/', product_details, name='product_details'),
    path('shop/', shop, name='shop'),
    path('',home,name='homepage'),
    path('agent',agent,name='agent'),
    path('news',news,name='news'),
    path('wishlist',wishlist,name='wishlist'),
    path('services',services,name='services'),
    path('pro-api/',include('main.api.urls')) 
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)