from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=32)
    customer_id = models.PositiveIntegerField()
    quantity= models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField()


