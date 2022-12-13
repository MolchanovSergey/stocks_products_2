from django.contrib import admin

# Register your models here.
from logistic.models import Product, Stock, StockProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # pass
    list_display = ['id', 'title',  'description']

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    # pass
    list_display = ['id', 'address']
    # inlines = [RelationshipInline]

@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    pass