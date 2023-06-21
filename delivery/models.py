from django.db import models

# Create your models here.

class Delivery(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    address = models.TextField()
    deliver_status = models.ImageField()
    customer_id = models.PositiveIntegerField()