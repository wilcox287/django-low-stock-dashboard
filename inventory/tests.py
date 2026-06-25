from django.test import TestCase
from .models import Product, InventorySetting


class InventoryTest(TestCase):

    def setUp(self):

        InventorySetting.objects.create(
            low_stock_threshold=10
        )

        Product.objects.create(
            name="Laptop",
            stock=5
        )

        Product.objects.create(
            name="Mouse",
            stock=20
        )

    def test_threshold_filter(self):

        threshold = InventorySetting.objects.first().low_stock_threshold

        low_stock = Product.objects.filter(
            stock__lt=threshold
        )

        self.assertEqual(
            low_stock.count(),
            1
        )