from django.contrib import admin

from products.models import Product, Category, Brand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.get_fields()]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.get_fields()]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Brand._meta.get_fields()]
