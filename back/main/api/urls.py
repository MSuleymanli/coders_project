from django.urls import path
from .views import ProductListApiView
urlpatterns = [
    path('list/',ProductListApiView.as_view(),name="api-list"),    
]