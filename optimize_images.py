import os
from PIL import Image

def optimize_image(input_path, output_path, max_size=(800, 800)):
    try:
        print(f"Processing {input_path}...")
        with Image.open(input_path) as img:
            # Convert to RGB if necessary (e.g. for PNG to JPG)
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # Resize
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # Save as JPEG
            img.save(output_path, 'JPEG', quality=85, optimize=True)
            print(f"Saved optimized image to {output_path}")

    except Exception as e:
        print(f"Error processing {input_path}: {e}")

# Optimize perfil_3 (currently renamed to .png)
optimize_image('src/image/perfil_3.png', 'src/image/perfil_3.jpg')

# Optimize perfil_4 (currently .jpg but actually png)
optimize_image('src/image/perfil_4.jpg', 'src/image/perfil_4.jpg')

# Clean up the source png for perfil_3 if successful
if os.path.exists('src/image/perfil_3.jpg') and os.path.exists('src/image/perfil_3.png'):
    os.remove('src/image/perfil_3.png')
    print("Removed source file src/image/perfil_3.png")
