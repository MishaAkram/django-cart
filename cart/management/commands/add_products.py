# cart/management/commands/add_products.py
from django.core.management.base import BaseCommand
from cart.models import Product

class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Adding products to the database...'))

        # Add your product creation logic here
        Product.objects.create(name='Product 1', description='Description 1', price=20.00)
        Product.objects.create(name='Product 2', description='Description 2', price=30.00)
        # Add more products as needed

        self.stdout.write(self.style.SUCCESS('Products added successfully'))
