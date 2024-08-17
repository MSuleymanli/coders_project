from rest_framework import serializers
from ..models import Product

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['product_image','product_name','product_status','product_location','product_type','product_about','product_price','product_bath_count','product_bed_count','product_ft','product_build_year']