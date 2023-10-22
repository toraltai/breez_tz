from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

class File(models.Model):
    file = models.FileField('File',upload_to='upload')


class Customer(models.Model):
    customer = models.CharField('Customer', max_length=50)
    item = models.ManyToManyField('Product', related_name='customers')

    def __str__(self):
        return f"{self.customer}"
    

class Product(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, max_length=50, related_name='products')
    item = models.CharField(verbose_name='Товар', max_length=50)
    total = models.IntegerField('Sum')
    quantity = models.PositiveIntegerField('Quantity')
    date = models.DateTimeField('Date')

    def __str__(self):
        return f'{self.item}'

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"