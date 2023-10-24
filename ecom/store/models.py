from django.db import models
import datetime
# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length= 100)
    price= models.DecimalField(default=0,decimal_places=2,max_digits=7)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=250,default='',blank=True,null=True)
    image = models.ImageField(upload_to='uploads/product/')
    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=
    address= 
    phone =
    date = 
    status = 
    def __str__(self) -> str:
        return self.product