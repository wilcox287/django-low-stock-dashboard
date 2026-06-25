from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    reorder_quantity = models.IntegerField(default=10)

    def __str__(self):
        return self.name


class InventorySetting(models.Model):
    low_stock_threshold = models.IntegerField(default=10)

    def __str__(self):
        return f"Threshold: {self.low_stock_threshold}"