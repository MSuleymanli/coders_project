from django.contrib import admin

from .models import *

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('product_name', 'product_price', 'product_location')
    
class AgentAdmin(admin.ModelAdmin):
    list_display=('get_full_name','agent_job_title')  
    
    def get_full_name(self, obj):
        return f"{obj.agent_name} {obj.agent_surname}"
    get_full_name.short_description = 'Full Name'  
    
    
    
class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1

class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PortfolioImageInline]
    list_display = ('portfolio_name', 'created_date')
    

    
class WishlistAdmin(admin.ModelAdmin):
    model=Wishlist
    list_display=('user','wish_name')
    
    
class BillignAdmin(admin.ModelAdmin):
    model=Billing
    list_display=('per_name','per_email','per_number','per_country','per_order_total','per_payment_method')

admin.site.register(Portfolio, PortfolioAdmin) 
admin.site.register(Product, ProductAdmin)
admin.site.register(Agent,AgentAdmin)
admin.site.register(Service)
admin.site.register(Customer)
admin.site.register(ContactSubmission)
admin.site.register(Comment)
admin.site.register(Wishlist,WishlistAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Billing,BillignAdmin)


