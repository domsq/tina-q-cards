from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Admin view for Category """
    list_display = (
        'name',
        'description',
    )

    search_fields = (
        'name',
        'description',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Admin view for Product """
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

    search_fields = (
        'name',
        'category__name',
    )

    ordering = ('name',)
