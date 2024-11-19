from django.db import models

# Create your models here.
class User(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    class Meta:
        db_table = 'users'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='products/')