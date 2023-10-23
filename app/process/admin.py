from django.contrib import admin
from .models import Product, File, Customer


admin.site.register(Product)
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    filter_horizontal = ['item']