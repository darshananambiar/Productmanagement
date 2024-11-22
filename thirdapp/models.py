from django.db import models

# Create your models here.
class User(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    class Meta:
        db_table = 'users'

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name





class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', default=1)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='products/')



