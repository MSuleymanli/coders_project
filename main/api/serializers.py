from rest_framework import serializers
from ..models import Product, ProductImage,Wishlist

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductSerializers(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id','product_image','product_name', 'product_status', 'product_location',
            'product_type', 'product_about', 'product_price', 'product_bath_count',
            'product_bed_count', 'product_ft', 'product_build_year', 'product_property_type',
            'product_amenities', 'product_price_range', 'product_beth_patch','images'
        ]


class WishlistSerializers(serializers.ModelSerializer):
    class Meta:
        model=Wishlist        
        fields=[
            'id','wish_image','wish_name','wish_price','product_id'
        ]
        
        


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
    
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    




class AddProductSerializers(serializers.ModelSerializer):
    product_price=serializers.DecimalField(max_digits=10, decimal_places=2, default=0)
    class Meta:
        model = Product
        fields = '__all__'
        
    def create(self, validated_data):
        return Product.objects.create(**validated_data)