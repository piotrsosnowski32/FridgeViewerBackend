from django.db import models
from datetime import date

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateField(default=date.today)
    expiry_date = models.DateField(default=date.today)

