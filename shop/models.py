from django.db import models

# Create your models here.
from django.utils import timezone


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=200)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    userId = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10, default="")
    serve_time=models.TimeField(null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.update_desc