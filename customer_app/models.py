from django.db import models
from django.utils import timezone


class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    date_created = models.DateTimeField(default=timezone.now)
    
    # returns name of the customer
    def __str__(self):
        return self.name
    
    
    
class Tag(models.Model):
    tag = models.CharField(max_length=500, blank=True)
    
    # returns name of the tag
    def __str__(self):
        return self.tag
    


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(max_length=200, choices=CATEGORY)
    description = models.CharField(max_length=200)
    tag = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(default=timezone.now)
    
    # returns name of the product
    def __str__(self):
        return self.name
    


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, default=None, on_delete=models.CASCADE) # cascade deletes the whole order when a customer is deleted
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL) # set_null does not delete the whole order if a product is deleted
    date_created = models.DateTimeField(default=timezone.now) 
    status = models.CharField(max_length=200, choices=STATUS)
    
