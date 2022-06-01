from django.db import models


class Category(models.Model):
    """ Schema for the Category model """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Schema for the Product model """

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
