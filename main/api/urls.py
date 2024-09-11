
from django.urls import path, re_path
from .views import ProductListApiView, ProductUpdateApiView, ProductDeleteApiView, ProductDetailApiView,LoginApiView,RegisterApiView,AddProductApiView,WishlistApiView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('list/', ProductListApiView.as_view(), name="api-list"),
    path('update/<int:pk>/', ProductUpdateApiView.as_view(), name="api-update"),
    path('delete/<int:pk>/', ProductDeleteApiView.as_view(), name="api-delete"),
    path('detail/<int:pk>/', ProductDetailApiView.as_view(), name="api-detail"),
    path('add-product/', AddProductApiView.as_view(), name='add-product'),
    path('login/', LoginApiView.as_view(), name='login-api'),
    path('register/', RegisterApiView.as_view(), name='register-api'),
    path('wishlist',WishlistApiView.as_view(),name="wishlist-api"),    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
