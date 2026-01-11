from django.contrib import admin
from .models import ShopifyOrder

# Register your models here.

@admin.register(ShopifyOrder)
class ShopifyOrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer_name', 'total_price', 'currency')