from django.contrib import admin

# Register your models here.

from .models import Products
class Products_Admin(admin.ModelAdmin):
    list_display=('name','price','quantity','image','customer_id')

admin.site.register(Products,Products_Admin)