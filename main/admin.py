from django.contrib import admin

from .models import Portfolio, Product, Agent, Service, ProductImage,Customer,PortfolioImage, ContactSubmission,Comment,Wishlist, Cart, CartItem

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
    

    
    
    

admin.site.register(Portfolio, PortfolioAdmin) 
admin.site.register(Product, ProductAdmin)
admin.site.register(Agent,AgentAdmin)
admin.site.register(Service)
admin.site.register(Customer)
admin.site.register(ContactSubmission)
admin.site.register(Comment)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(CartItem)


