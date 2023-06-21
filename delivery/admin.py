from django.contrib import admin

# Register your models here.
from .models import Delivery 

class Delivery_Admin(admin.ModelAdmin):
    list_display = ('name', 'price', 'address', 'deliver_status', 'customer_id')

admin.site.register(Delivery, Delivery_Admin)