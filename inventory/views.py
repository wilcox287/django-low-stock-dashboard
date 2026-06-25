from django.shortcuts import render
from .models import Product, InventorySetting


def dashboard(request):

    settings = InventorySetting.objects.first()

    threshold = (
        settings.low_stock_threshold
        if settings
        else 10
    )

    products = Product.objects.all()

    low_stock_products = products.filter(
        stock__lt=threshold
    )

    context = {
        "products": products,
        "low_stock_products": low_stock_products,
        "threshold": threshold
    }

    return render(
        request,
        "inventory/dashboard.html",
        context
    )