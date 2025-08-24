import os
import django
from datetime import time

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sports_center.settings')
django.setup()

from booking.models import Venue, TimeSlot

def create_sample_venues():
    # Create Basketball Court
    basketball, created = Venue.objects.get_or_create(
        name="Main Basketball Court",
        defaults={
            'venue_type': 'basketball',
            'description': 'Indoor basketball court with wooden flooring',
            'location': 'Building A, First Floor',
            'price_per_hour': 50.00,
            'capacity': 20,
            'is_active': True
        }
    )
    
    if created:
        print(f"Created Basketball Court (ID: {basketball.id})")
        # Create time slots from 6 AM to 10 PM
        for hour in range(6, 22):
            TimeSlot.objects.create(
                venue=basketball,
                start_time=time(hour, 0),
                end_time=time(hour + 1, 0),
                is_active=True
            )
        print("Created time slots for Basketball Court (6:00 AM - 10:00 PM)")
    
    # Create Futsal Court
    futsal, created = Venue.objects.get_or_create(
        name="Futsal Court 1",
        defaults={
            'venue_type': 'futsal',
            'description': 'Indoor futsal court with artificial turf',
            'location': 'Building B, Ground Floor',
            'price_per_hour': 40.00,
            'capacity': 14,
            'is_active': True
        }
    )
    
    if created:
        print(f"\nCreated Futsal Court (ID: {futsal.id})")
        # Create time slots from 8 AM to 11 PM
        for hour in range(8, 23):
            TimeSlot.objects.create(
                venue=futsal,
                start_time=time(hour, 0),
                end_time=time(hour + 1, 0),
                is_active=True
            )
        print("Created time slots for Futsal Court (8:00 AM - 11:00 PM)")
    
    print("\nSample data creation complete!")

if __name__ == "__main__":
    create_sample_venues()
