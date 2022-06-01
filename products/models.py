from django.db import models


class Category(models.Model):
    """ Schema for the Category model """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
