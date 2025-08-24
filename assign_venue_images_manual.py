import os
from pathlib import Path
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sports_center.settings')
django.setup()

from booking.models import Venue

def list_venues():
    print("\n=== Venues ===")
    for venue in Venue.objects.all():
        status = "Has image" if venue.image else "No image"
        print(f"ID: {venue.id}, Name: {venue.name}, Status: {status}")

def assign_image(venue_id, image_path):
    try:
        venue = Venue.objects.get(id=venue_id)
        
        # Check if file exists
        if not os.path.exists(image_path):
            print(f"Error: File not found: {image_path}")
            return False
            
        # Open and assign the image
        with open(image_path, 'rb') as f:
            venue.image.save(os.path.basename(image_path), django.core.files.File(f), save=True)
            print(f"Assigned {image_path} to {venue.name}")
            return True
            
    except Venue.DoesNotExist:
        print(f"Error: Venue with ID {venue_id} not found")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    import django.core.files
    
    print("Venue Image Assignment Tool")
    print("==========================")
    
    while True:
        print("\nOptions:")
        print("1. List all venues")
        print("2. Assign image to venue")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            list_venues()
            
        elif choice == '2':
            list_venues()
            venue_id = input("\nEnter venue ID: ")
            image_path = input("Enter full path to image: ")
            
            try:
                venue_id = int(venue_id)
                if assign_image(venue_id, image_path):
                    print("Image assigned successfully!")
                else:
                    print("Failed to assign image.")
            except ValueError:
                print("Error: Please enter a valid venue ID (number).")
                
        elif choice == '3':
            print("Exiting...")
            break
            
        else:
            print("Invalid choice. Please try again.")
