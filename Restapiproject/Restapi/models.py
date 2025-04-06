from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    available = models.BooleanField(default=True)
    stock = models.IntegerField()
    sku = models.CharField(max_length=50, unique=True)
    rating = models.FloatField(default=0.0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.name
