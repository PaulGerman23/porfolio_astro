from PIL import Image, ImageOps

def process_image():
    target_width = 1365
    target_height = 767
    
    # Open the source image
    source_path = 'src/image/charades_mobile.jpg'
    output_path = 'src/image/charades.png'
    public_output_path = 'public/images/charades.png'
    
    try:
        img = Image.open(source_path)
        
        # Calculate aspect ratios
        target_ratio = target_width / target_height
        img_ratio = img.width / img.height
        
        # Create a new black image
        new_img = Image.new('RGB', (target_width, target_height), (0, 0, 0))
        
        if img_ratio > target_ratio:
            # Image is wider than target, resize by width
            new_width = target_width
            new_height = int(target_width / img_ratio)
        else:
            # Image is taller than target, resize by height
            new_height = target_height
            new_width = int(target_height * img_ratio)
            
        # Resize the source image
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Paste centered
        x = (target_width - new_width) // 2
        y = (target_height - new_height) // 2
        new_img.paste(img, (x, y))
        
        # Save
        new_img.save(output_path)
        new_img.save(public_output_path)
        print(f"Image processed and saved to {output_path} and {public_output_path}")
        
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    process_image()
