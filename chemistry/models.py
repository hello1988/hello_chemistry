from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Basis(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Customer(Basis):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=32, null=True, blank=True)
    fax = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    EIN_number = models.CharField(max_length=32, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)

class Product(Basis):
    name = models.CharField(max_length=64)
    weight = models.FloatField(default=0)
    price = models.FloatField(default=0)
    desc = models.TextField(null=True, blank=True)

class Order(Basis):
    discount = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)
    desc = models.TextField(null=True, blank=True)

class Cart(Basis):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    desc = models.TextField(null=True, blank=True)


