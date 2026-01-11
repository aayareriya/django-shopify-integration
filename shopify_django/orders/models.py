from django.db import models

# Create your models here.

class ShopifyOrder(models.Model):  

    order_id = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    total_price =  models.DecimalField(max_digits=10,decimal_places=2)
    currency = models.CharField(max_length=10)
    order_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.order_id
    


