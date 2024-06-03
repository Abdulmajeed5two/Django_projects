# shop/admin.py
from django.contrib import admin
from .models import Cart, CartItem, Product
from django.contrib import admin
from .models import Order, OrderItem

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)



class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'email', 'total', 'created_at']
    list_filter = ['created_at']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
