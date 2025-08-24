import os
import django
from datetime import time

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sports_center.settings')
django.setup()

from booking.models import Venue, TimeSlot

def check_and_populate():
    print("=== Checking Database ===")
    
    # Check venues
    venues = Venue.objects.all()
    print(f"Found {venues.count()} venues in the database")
    
    if venues.count() == 0:
        print("\n=== No venues found. Creating sample data... ===")
        # Create Basketball Court
        basketball = Venue.objects.create(
            name="Main Basketball Court",
            venue_type='basketball',
            description='Indoor basketball court with wooden flooring',
            location='Building A, First Floor',
            price_per_hour=50.00,
            capacity=20,
            is_active=True
        )
        print(f"Created Basketball Court (ID: {basketball.id})")
        
        # Create time slots for basketball (6 AM to 10 PM)
        for hour in range(6, 22):
            TimeSlot.objects.create(
                venue=basketball,
                start_time=time(hour, 0),
                end_time=time(hour + 1, 0),
                is_active=True
            )
        print(f"Created time slots for Basketball Court (6:00 AM - 10:00 PM)")
        
        # Create Futsal Court
        futsal = Venue.objects.create(
            name="Futsal Court 1",
            venue_type='futsal',
            description='Indoor futsal court with artificial turf',
            location='Building B, Ground Floor',
            price_per_hour=40.00,
            capacity=14,
            is_active=True
        )
        print(f"\nCreated Futsal Court (ID: {futsal.id})")
        
        # Create time slots for futsal (8 AM to 11 PM)
        for hour in range(8, 23):
            TimeSlot.objects.create(
                venue=futsal,
                start_time=time(hour, 0),
                end_time=time(hour + 1, 0),
                is_active=True
            )
        print("Created time slots for Futsal Court (8:00 AM - 11:00 PM)")
    
    # Display current data
    print("\n=== Current Database State ===")
    for venue in Venue.objects.all():
        print(f"\nVenue: {venue.name} (ID: {venue.id})")
        print(f"Type: {venue.venue_type}, Active: {venue.is_active}")
        print(f"Time slots: {venue.timeslot_set.count()}")
        
        # Show first 3 time slots as sample
        for slot in venue.timeslot_set.order_by('start_time')[:3]:
            print(f"  - {slot.start_time} to {slot.end_time}")
        if venue.timeslot_set.count() > 3:
            print(f"  ... and {venue.timeslot_set.count() - 3} more")

if __name__ == "__main__":
    check_and_populate()
