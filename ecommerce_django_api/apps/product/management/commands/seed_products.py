from django.core.management.base import BaseCommand
from apps.product.models import Product, Brand, Category

PRODUCTS = [
    {
        "name": "MacBook Pro",
        "category": "Electronics",
        "brand": "Apple",
        "description": "Powerful and sleek laptop for professionals.",
    },
    {
        "name": "Air Jordan 1",
        "category": "Fashion",
        "brand": "Nike",
        "description": "Iconic basketball shoes loved by sneakerheads.",
    },
    {
        "name": "Galaxy S21",
        "category": "Electronics",
        "brand": "Samsung",
        "description": "Feature-packed smartphone with stunning display.",
    },
    {
        "name": "Ultraboost",
        "category": "Sporting Goods",
        "brand": "Adidas",
        "description": "High-performance running shoes for athletes.",
    },
    {
        "name": "PlayStation 5",
        "category": "Electronics",
        "brand": "Sony",
        "description": "Next-generation gaming console with cutting-edge graphics.",
    },
    {
        "name": "iPhone 13",
        "category": "Electronics",
        "brand": "Apple",
        "description": "Latest flagship smartphone with advanced camera capabilities.",
    },
    {
        "name": "Air Max 90",
        "category": "Fashion",
        "brand": "Nike",
        "description": "Iconic retro sneakers known for their comfort and style.",
    },
    {
        "name": "QLED TV",
        "category": "Electronics",
        "brand": "Samsung",
        "description": "Immersive television experience with vibrant colors.",
    },
    {
        "name": "Superstar",
        "category": "Fashion",
        "brand": "Adidas",
        "description": "Classic sneakers loved for their timeless design.",
    },
    {
        "name": "PlayStation 5 Digital Edition",
        "category": "Electronics",
        "brand": "Sony",
        "description": "Digital-only version of the popular gaming console.",
    },
]


class Command(BaseCommand):
    help = "Seed the database with real-like data"

    BRAND_NAMES = ["Apple", "Nike", "Samsung", "Adidas", "Sony"]
    PRODUCT_CATEGORIES = ["Electronics", "Fashion", "Sporting Goods"]

    def handle(self, *args, **options):
        # Create brands
        brands = []
        for brand_name in self.BRAND_NAMES:
            brand = Brand(name=brand_name)
            brand.save()
            brands.append(brand)

        for product_data in PRODUCTS:
            brand_name = product_data["brand"]
            brand = next((b for b in brands if b.name == brand_name), None)
            if brand:
                category = Category(name=product_data["category"])
                category.save()
                product = Product(
                    name=product_data["name"],
                    category=category,
                    brand=brand,
                    description=product_data["description"],
                )
                product.save()

        self.stdout.write(
            self.style.SUCCESS("Successfully seeded the database with real-like data.")
        )
