from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('product', 'price', 'quantity', 'selected_option')
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'user', 
        'first_name', 
        'last_name', 
        'paid_amount', 
        'shipping_cost', 
        'created_at',
        'status', 
        'tracking_number' 
    ]
    list_editable = ['status', 'tracking_number'] 
    inlines = [OrderItemInline]