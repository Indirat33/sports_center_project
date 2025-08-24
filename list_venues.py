import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sports_center.settings')
django.setup()

from booking.models import Venue, TimeSlot

def list_venues_and_slots():
    print("=== Venues and Time Slots ===")
    
    # Get all venues
    venues = Venue.objects.all()
    
    if not venues.exists():
        print("No venues found in the database!")
        return
    
    for venue in venues:
        print(f"\nVenue: {venue.name} (ID: {venue.id}, Type: {venue.venue_type}, Active: {venue.is_active})")
        
        # Get all time slots for this venue
        time_slots = TimeSlot.objects.filter(venue=venue).order_by('start_time')
        
        if not time_slots.exists():
            print("  No time slots defined for this venue!")
            continue
            
        print(f"  Time Slots ({time_slots.count()}):")
        for slot in time_slots:
            print(f"    - ID: {slot.id}, Time: {slot.start_time} to {slot.end_time}, Active: {slot.is_active}")

if __name__ == "__main__":
    list_venues_and_slots()
