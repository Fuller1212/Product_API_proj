from django.db import models
from django.forms import CharField

from products.models import Product

# Create your models here.

class Review(models.Model):
    review = models.CharField(max_length=10000)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
