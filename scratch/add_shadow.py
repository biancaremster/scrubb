from PIL import Image

def add_drop_shadow():
    input_path = '/Users/biancaremster/.gemini/antigravity/brain/839a0a48-0db5-40a0-8026-e033fa4d1e37/media__1778437736364.png'
    output_path = '/Users/biancaremster/antigravity projects/logo_with_shadow.png'
    artifact_path = '/Users/biancaremster/.gemini/antigravity/brain/839a0a48-0db5-40a0-8026-e033fa4d1e37/logo_with_shadow.png'
    
    img = Image.open(input_path).convert("RGBA")
    
    # Tighter offset: 2px by 2px to be closer to the design
    offset_x, offset_y = 2, 2
    
    new_width = img.width + offset_x
    new_height = img.height + offset_y
    
    # Create the shadow image
    shadow = Image.new("RGBA", img.size, (44, 44, 44, 255))
    shadow.putalpha(img.split()[3])
    
    # Use alpha_composite for perfect anti-aliasing instead of .paste()
    canvas = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))
    
    shadow_layer = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))
    shadow_layer.paste(shadow, (offset_x, offset_y))
    
    img_layer = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))
    img_layer.paste(img, (0, 0))
    
    # Composite!
    final = Image.alpha_composite(canvas, shadow_layer)
    final = Image.alpha_composite(final, img_layer)
    
    final.save(output_path)
    final.save(artifact_path)
    print("Shadow generation complete.")

if __name__ == '__main__':
    add_drop_shadow()
