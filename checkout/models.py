from django.db import models


class Order(models.Model):
    order_number = models.CharField(max_length=30, null=False, editable=False)
    full_name = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    postcode = models.CharField(max_length=10, null=False, blank=False)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    street_adress1 = models.CharField(max_length=50, null=False, blank=False)
    street_adress2 = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=15, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=15, decimal_places=2, null=False, default=0)
    
