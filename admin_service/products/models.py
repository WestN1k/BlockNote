from django.db import models


class Product(models.Model):
    title = models.CharField(verbose_name='Title', max_length=200)
    image = models.CharField(verbose_name='Image url', max_length=200)
    likes = models.PositiveIntegerField(verbose_name='likes count', default=0)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


class User(models.Model):
    id = models.UUIDField(verbose_name='UUID', primary_key=True, auto_created=True)
