import os
from PIL import Image
from pillow_heif import register_heif_opener

# Register HEIC opener
register_heif_opener()

# Define paths
script_dir = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(script_dir, 'files2convert')
output_folder = os.path.join(script_dir, 'converted')

# Ensure output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def convert_heic_to_jpg(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            # Convert to RGB (in case of RGBA images) and save as JPEG
            img.convert('RGB').save(output_path, 'JPEG', quality=95)
        print(f"Converted: {os.path.basename(input_path)}")
    except Exception as e:
        print(f"Error converting {os.path.basename(input_path)}: {str(e)}")

# Iterate through files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith('.heic'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpg")
        convert_heic_to_jpg(input_path, output_path)

print("Conversion complete!")
