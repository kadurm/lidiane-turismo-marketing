from PIL import Image

def make_transparent(img_path, output_path, tolerance=50):
    try:
        img = Image.open(img_path).convert("RGBA")
        data = img.getdata()
        
        new_data = []
        for item in data:
            # Check if the pixel is close to white (background)
            if item[0] > 255 - tolerance and item[1] > 255 - tolerance and item[2] > 255 - tolerance:
                # Fully transparent
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)
                
        img.putdata(new_data)
        img.save(output_path, "PNG")
        print(f"Success: Saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

make_transparent("brand/logo.png", "brand/logo_transparent.png", tolerance=70)
