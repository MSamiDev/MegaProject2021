from django.contrib import admin

# Register your models here.
from .models import *


class AdminProduct(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'category']



admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
