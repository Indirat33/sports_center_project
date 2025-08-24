import os
import sys
from pathlib import Path

# Set up Django environment
def setup_django():
    # Add the project directory to the Python path
    project_path = Path(__file__).resolve().parent
    sys.path.append(str(project_path))
    
    # Set the Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sports_center.settings')
    
    # Setup Django
    import django
    django.setup()

def assign_default_images():
    from django.core.files import File
    from booking.models import Venue
    
    # Get the base directory of the project
    BASE_DIR = Path(__file__).resolve().parent
    
    # Map venue types to their corresponding image filenames
    VENUE_IMAGES = {
        'basketball': 'basketball.jpg',
        'futsal': 'futsal.jpg',
        'badminton': 'badminton.jpg',
        'tennis': 'Tennis.jpg',  # Note the capital 'T' to match the filename
        'other': 'default.jpg'
    }
    
    # Get all venues
    venues = Venue.objects.all()
    
    for venue in venues:
        # Skip if venue already has an image
        if venue.image:
            print(f"Skipping {venue.name} - already has an image")
            continue
            
        # Get the appropriate image filename based on venue type
        image_filename = VENUE_IMAGES.get(venue.venue_type, 'default.jpg')
        image_path = BASE_DIR / 'booking' / 'static' / 'booking' / 'images' / 'venues' / image_filename
        
        # Check if the image file exists
        if not image_path.exists():
            print(f"Warning: Image not found for {venue.name} at {image_path}")
            continue
            
        # Open and assign the image
        with open(image_path, 'rb') as img_file:
            django_file = File(img_file, name=image_path.name)
            venue.image.save(image_filename, django_file, save=True)
            print(f"Assigned {image_filename} to {venue.name}")

if __name__ == "__main__":
    setup_django()
    assign_default_images()
