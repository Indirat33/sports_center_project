import os
import django
from datetime import time

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sports_center.settings')
django.setup()

from booking.models import Venue, TimeSlot

def fix_time_slots():
    # Get all active venues
    active_venues = Venue.objects.filter(is_active=True)
    
    for venue in active_venues:
        print(f"\nProcessing venue: {venue.name} (ID: {venue.id})")
        
        # Delete existing time slots for this venue
        deleted_count, _ = TimeSlot.objects.filter(venue=venue).delete()
        print(f"  - Deleted {deleted_count} existing time slots")
        
        # Create new time slots based on venue type
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
        
        print(f"  - Created {slots_created} new time slots ({start_hour:02d}:00 - {end_hour:02d}:00)")
    
    print("\nTime slots have been fixed for all active venues!")

if __name__ == "__main__":
    fix_time_slots()
