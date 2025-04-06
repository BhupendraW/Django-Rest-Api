from django.contrib import admin

# Register your models here.
from .models import Product, Category, Tag 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available', 'stock', 'category', 'created_at')
    list_filter = ('available', 'category', 'is_featured')
    search_fields = ('name', 'description', 'sku')
    prepopulated_fields = {'slug': ('name',)}  


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)