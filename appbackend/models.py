from django.db import models
from datetime import date

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.email}"
    
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateField(default=date.today)
    expiry_date = models.DateField(default=date.today)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return (f"{self.name} | "
                f"kategoria: {self.category_id.name} | "
                f"użytkownik: {self.user_id.name} | "
                f"data zakupu: {self.purchase_date} | "
                f"termin przydatności: {self.expiry_date} | "
                f"aktualnie w lodówce: {'tak' if self.is_active else 'nie' }")
