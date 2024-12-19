from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
import random

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')
        
        # Create sample listings
        for i in range(5):
            listing = Listing.objects.create(
                title=f"Listing {i+1}",
                description=f"This is a description for Listing {i+1}",
                price_per_night=random.randint(50, 500),
                location=f"Location {i+1}"
            )
            # Create bookings for each listing
            for j in range(2):
                Booking.objects.create(
                    listing=listing,
                    guest_name=f"Guest {j+1}",
                    check_in="2024-12-20",
                    check_out="2024-12-25",
                    total_price=random.randint(200, 1000)
                )
            # Create reviews for each listing
            for k in range(3):
                Review.objects.create(
                    listing=listing,
                    guest_name=f"Reviewer {k+1}",
                    rating=random.randint(1, 5),
                    comment=f"This is a comment for Listing {i+1} by Reviewer {k+1}"
                )
        
        self.stdout.write('Database seeding completed.')

