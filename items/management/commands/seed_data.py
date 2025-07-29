from django.core.management.base import BaseCommand
from items.models import Item
import random
from decimal import Decimal

class Command(BaseCommand):
    help = 'Seed the database with sample items'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Number of items to create (default: 10)'
        )

    def handle(self, *args, **options):
        count = options['count']
        
        sample_items = [
            {'name': 'MacBook Pro', 'description': 'Apple laptop with M2 chip'},
            {'name': 'iPhone 15', 'description': 'Latest iPhone model'},
            {'name': 'Django Book', 'description': 'Learn Django development'},
            {'name': 'Python Guide', 'description': 'Complete Python programming guide'},
            {'name': 'T-Shirt', 'description': 'Comfortable cotton t-shirt'},
            {'name': 'Jeans', 'description': 'Blue denim jeans'},
            {'name': 'Coffee Maker', 'description': 'Automatic coffee brewing machine'},
            {'name': 'Basketball', 'description': 'Professional basketball'},
            {'name': 'Tennis Racket', 'description': 'Professional tennis racket'},
            {'name': 'LEGO Set', 'description': 'Building blocks for creativity'},
            {'name': 'Wireless Headphones', 'description': 'Noise-cancelling headphones'},
            {'name': 'Gaming Mouse', 'description': 'High-precision gaming mouse'},
            {'name': 'Mechanical Keyboard', 'description': 'RGB mechanical keyboard'},
            {'name': 'Monitor Stand', 'description': 'Adjustable monitor stand'},
            {'name': 'Desk Lamp', 'description': 'LED desk lamp with dimmer'},
        ]

        created_items = []
        for i in range(count):
            base_item = sample_items[i % len(sample_items)]

            price = Decimal(random.uniform(10.00, 999.99)).quantize(Decimal('0.01'))
            
            item = Item.objects.create(
                name=f"{base_item['name']} {i+1}",
                description=f"{base_item['description']} - Item #{i+1}",
                price=price
            )
            created_items.append(item)

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {count} items')
        )
        
        # for item in created_items[:5]:
        #     self.stdout.write(f'  - {item.name}: ${item.price}')
        
        # if count > 5:
        #     self.stdout.write(f'  ... and {count - 5} more items')

        # total_value = sum(item.price for item in created_items)
        # avg_price = total_value / len(created_items) if created_items else 0
        
        # self.stdout.write(
        #     self.style.WARNING(f'\nStatistics:')
        # )
        # self.stdout.write(f'  Total items: {count}')
        # self.stdout.write(f'  Total value: ${total_value}')
        # self.stdout.write(f'  Average price: ${avg_price:.2f}')
        # self.stdout.write(f'  Price range: ${min(item.price for item in created_items)} - ${max(item.price for item in created_items)}')