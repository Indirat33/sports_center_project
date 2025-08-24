import os
import django
from datetime import time
import sys

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sports_center.settings')
try:
    django.setup()
except Exception as e:
    print(f"Error setting up Django: {e}")
    sys.exit(1)

from booking.models import Venue, TimeSlot

def main():
    print("=== Venue and Time Slot Verification ===\n")
    
    # Check if there are any venues
    venues = Venue.objects.all()
    if not venues.exists():
        print("No venues found in the database!")
        return
    
    print(f"Found {len(venues)} venues in the database:")
    for venue in venues:
        print(f"- {venue.name} (ID: {venue.id}, Type: {venue.venue_type}, Active: {venue.is_active})")
    
    # Check time slots for each venue
    print("\n=== Time Slots ===")
    for venue in venues:
        print(f"\nVenue: {venue.name} (ID: {venue.id})")
        time_slots = TimeSlot.objects.filter(venue=venue).order_by('start_time')
        
        if not time_slots.exists():
            print("  No time slots found for this venue!")
            
            # Create default time slots for this venue
            print("  Creating default time slots...")
            create_default_slots(venue)
        else:
            print(f"  Found {time_slots.count()} time slots:")
            for slot in time_slots:
                print(f"  - {slot.start_time} to {slot.end_time} (ID: {slot.id})")
    
    print("\n=== Verification Complete ===")

def create_default_slots(venue):
    """Create default time slots for a venue based on its type"""
    if venue.venue_type == 'basketball':
        # Basketball court hours: 6 AM - 10 PM
        start_hour = 6
        end_hour = 22
    elif venue.venue_type == 'futsal':
        # Futsal court hours: 8 AM - 11 PM
        start_hour = 8
        end_hour = 23
    else:
        # Default hours for other venues: 7 AM - 10 PM
        start_hour = 7
        end_hour = 22
    
    # Create time slots
    slots_created = 0
    for hour in range(start_hour, end_hour):
        TimeSlot.objects.create(
            venue=venue,
            start_time=time(hour, 0),
            end_time=time(hour + 1, 0),
            is_active=True
        )
        slots_created += 1
    
    print(f"  Created {slots_created} time slots ({start_hour:02d}:00 - {end_hour:02d}:00)")

if __name__ == "__main__":
    main()
