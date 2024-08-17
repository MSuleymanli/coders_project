from rest_framework.generics import ListAPIView
from ..models import Product
from .serializers import ProductSerializers

class ProductListApiView(ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers