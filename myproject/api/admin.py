from django.contrib import admin
from api.models import Product



Product.objects.create(
    name="Laptop",
    description="High-performance laptop",
    price=999.99
)
Product.objects.create(
    name="Smartphone",
    description="Latest model smartphone",
    price=699.99
)