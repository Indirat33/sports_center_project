import os
import django
from datetime import time, timedelta

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sports_center.settings')
django.setup()

from booking.models import Venue, TimeSlot

def create_sample_data():
    print("Creating sample data...")
    
    # Create a basketball court
    basketball_court, created = Venue.objects.get_or_create(
        name="Main Basketball Court",
        venue_type='basketball',
        defaults={
            'description': 'Indoor basketball court with wooden flooring',
            'location': 'Building A, First Floor',
            'price_per_hour': 50.00,
            'capacity': 20,
            'is_active': True
        }
    )
    
    if created:
        print(f"Created venue: {basketball_court.name}")
        
        # Create time slots for the basketball court (6 AM to 10 PM)
        start_hour = 6
        end_hour = 22  # 10 PM
        
        for hour in range(start_hour, end_hour):
            start_time = time(hour, 0)
            end_time = time(hour + 1, 0)
            
            TimeSlot.objects.create(
                venue=basketball_court,
                start_time=start_time,
                end_time=end_time,
                is_active=True
            )
        
        print(f"Created time slots for {basketball_court.name} from 6:00 AM to 10:00 PM")
    else:
        print(f"Venue '{basketball_court.name}' already exists")

if __name__ == "__main__":
    create_sample_data()
    print("Sample data population complete!")
