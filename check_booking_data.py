import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sports_center.settings')
django.setup()

from booking.models import Venue, TimeSlot

def check_booking_data():
    # Check all venues
    print("\n=== Venues ===")
    venues = Venue.objects.all()
    if not venues.exists():
        print("No venues found in the database!")
    else:
        for venue in venues:
            print(f"\nVenue: {venue.name} (ID: {venue.id}, Active: {venue.is_active})")
            print(f"Type: {venue.venue_type}")
            print(f"Price per hour: ${venue.price_per_hour}")
            
            # Check time slots for this venue
            time_slots = TimeSlot.objects.filter(venue=venue).order_by('start_time')
            print(f"Time slots: {time_slots.count()}")
            
            if time_slots.exists():
                print("Available time slots:")
                for slot in time_slots[:5]:  # Show first 5 slots
                    print(f"  - {slot.formatted_time} (ID: {slot.id}, Active: {slot.is_active})")
                if time_slots.count() > 5:
                    print(f"  ... and {time_slots.count() - 5} more")
            else:
                print("  No time slots defined for this venue!")

if __name__ == "__main__":
    check_booking_data()
