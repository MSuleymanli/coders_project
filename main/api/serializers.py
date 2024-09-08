from rest_framework import serializers
from ..models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductSerializers(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)  # İlgili görüntüleri ekliyoruz

    class Meta:
        model = Product
        fields = [
            'id','product_image','product_name', 'product_status', 'product_location',
            'product_type', 'product_about', 'product_price', 'product_bath_count',
            'product_bed_count', 'product_ft', 'product_build_year', 'product_property_type',
            'product_amenities', 'product_price_range', 'product_beth_patch','images'
        ]
