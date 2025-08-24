from PIL import Image, ImageDraw, ImageFont
import os

# Create the output directory if it doesn't exist
output_dir = r"c:\Users\indira\sports_center_project\booking\static\booking\images\venues"
os.makedirs(output_dir, exist_ok=True)

# Define colors for different court types
colors = {
    'basketball': (70, 130, 180),  # Steel Blue
    'futsal': (34, 139, 34),      # Forest Green
    'badminton': (255, 165, 0),    # Orange
    'tennis': (255, 255, 255),     # White
    'default': (128, 128, 128)     # Gray
}

# Sizes for the placeholder images
width, height = 800, 600

# Create a placeholder image for each court type
for court_type, color in colors.items():
    # Create a new image with a light gray background
    image = Image.new('RGB', (width, height), color=(240, 240, 240))
    draw = ImageDraw.Draw(image)
    
    # Add a colored rectangle
    padding = 20
    draw.rectangle(
        [(padding, padding), (width - padding, height - padding)],
        fill=color,
        outline=(0, 0, 0),
        width=2
    )
    
    # Add text
    try:
        # Try to use a nice font if available
        font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        # Fall back to default font
        font = ImageFont.load_default()
    
    text = f"{court_type.capitalize()} Court"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    # Calculate text position (centered)
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Draw the text with a shadow effect
    shadow_color = (0, 0, 0)  # Black shadow
    draw.text((x+2, y+2), text, fill=shadow_color, font=font)
    draw.text((x, y), text, fill=(255, 255, 255), font=font)  # White text
    
    # Save the image
    image_path = os.path.join(output_dir, f"{court_type}.jpg")
    image.save(image_path, "JPEG", quality=95)
    print(f"Created: {image_path}")

print("\nPlaceholder images created successfully!")
