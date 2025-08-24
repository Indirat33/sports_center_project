import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sports_center.settings')
django.setup()

from booking.models import TimeSlot, Venue

def check_time_slots():
    print("\n=== Time Slots by Venue ===")
    
    # Get all active venues
    venues = Venue.objects.filter(is_active=True).order_by('id')
    
    if not venues.exists():
        print("No active venues found!")
        return
    
    for venue in venues:
        print(f"\nVenue: {venue.name} (ID: {venue.id}, Type: {venue.venue_type})")
        
        # Get all time slots for this venue
        time_slots = TimeSlot.objects.filter(venue=venue).order_by('start_time')
        
        if not time_slots.exists():
            print("  No time slots found for this venue!")
            continue
            
        print(f"  Time slots ({time_slots.count()}):")
        for slot in time_slots:
            print(f"    - {slot.start_time} to {slot.end_time} (ID: {slot.id})")

if __name__ == "__main__":
    check_time_slots()
