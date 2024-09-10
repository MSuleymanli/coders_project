from rest_framework.generics import ListAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login as auth_login,get_user_model
from rest_framework import status
from ..models import Product,Wishlist
from .serializers import ProductSerializers,LoginSerializer,RegisterSerializer,AddProductSerializers,WishlistSerializers
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ModulPagination(PageNumberPagination):
    page_size = 5
    
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data
        })

class ProductListApiView(ListAPIView):
    serializer_class = ProductSerializers
    pagination_class = ModulPagination

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('product_status', openapi.IN_QUERY, description="", type=openapi.TYPE_STRING),
            openapi.Parameter('product_property_type', openapi.IN_QUERY, description="", type=openapi.TYPE_STRING),
            openapi.Parameter('product_amenities', openapi.IN_QUERY, description="", type=openapi.TYPE_STRING),
            openapi.Parameter('product_price_range', openapi.IN_QUERY, description="", type=openapi.TYPE_STRING),
            openapi.Parameter('product_beth_patch', openapi.IN_QUERY, description="", type=openapi.TYPE_STRING),
        ],tags=['List']
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Product.objects.all()
        
        def apply_filter(param_name, field_name):
            param_value = self.request.query_params.get(param_name, None)
            if param_value:
                values = param_value.split(',')
                return Q(**{f"{field_name}__in": values})
            return None

        filters = [
            ('product_status', 'product_status'),
            ('product_property_type', 'product_property_type'),
            ('product_amenities', 'product_amenities'),
            ('product_price_range', 'product_price_range'),
            ('product_beth_patch', 'product_beth_patch')
        ]

        for param, field in filters:
            filter_query = apply_filter(param, field)
            if filter_query:
                queryset = queryset.filter(filter_query)
        queryset=queryset.order_by("-id")
        return queryset

class ProductUpdateApiView(UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    lookup_field='pk'
    

    
class ProductDeleteApiView(DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    lookup_field='pk'
    
    

    
class ProductDetailApiView(RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    lookup_field='pk'
    
    @swagger_auto_schema(tags=['List'])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    
class LoginApiView(APIView):
    @swagger_auto_schema(request_body=LoginSerializer,tags=['Account'])
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is None:
                return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
            
            auth_login(request, user)
            return Response({"detail": "Login successful"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
User = get_user_model()

class RegisterApiView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer,tags=['Account'])
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            last_name = serializer.validated_data.get('last_name')
            email = serializer.validated_data.get('email')
            
            newUser = User(username=username, last_name=last_name, email=email)
            newUser.set_password(password)
            newUser.save()
            
            auth_login(request, newUser)
            return Response({"detail": "Registration successful"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class AddProductApiView(APIView):
    @swagger_auto_schema(request_body=AddProductSerializers)
    def post(self, request, *args, **kwargs):
        serializer = AddProductSerializers(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class WishlistApiView(ListAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializers

    @swagger_auto_schema(tags=['List'])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)