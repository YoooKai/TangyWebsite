from django.contrib import admin
from .models import Category, Product, ProductImage, ProductOption

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductOptionInline(admin.TabularInline):
    model = ProductOption
    extra = 1
    fields = ('name', 'additional_price', 'additional_weight')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'weight', 'date_added']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ProductOptionInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']
