from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    customer_nick = models.CharField(max_length=30)
    customer_name = models.CharField(max_length=30)
    customer_surname = models.CharField(max_length=30)
    customer_password = models.CharField(max_length=30)
    customer_email = models.EmailField(max_lenght =50)
    customer_adress_country = varchar(20)
    customer_address_city = varchar(20)
    customer_address_postcode = varchar(6)
    customer_address_street = varchar(20)
    customer_address_street_number = varchar(3)
    customer_phone_number = models.CharField(max_lenght=12)

class Product(models.Model):
        product_name = models.CharField(max_length=200, null=True)
        product_category = models.CharField(max_length=200)
        product_company = models.CharField(max_length=200)
        product_price = models.FloatField(null=True)
        product_description = models.TextField()
        photo = models.ImageField(upload_to='product_photo',
                                  blank=True)
        date_created = models.DateTimeField(auto_now_add=True, null=True)

class Category(models.Model):
    category_name = models.ManyToManyField('Category', related_name = ???)
    category_description = description = models.TextField()

class Product_Shopping_Cart(models.Model)
    shopping_cart_id = models.ManyToManyField(Products,null=True,blank=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

class Shopping_cart(models.Model):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    shoopping_cart_quantity = models.IntegerField(default=1)

class Order(models.Model)
    order_shipment_date = models.DateTimeField(auto_now_add=False,auto_now=True)
    products = models.OnetoOneField(Shopping_cart, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)






