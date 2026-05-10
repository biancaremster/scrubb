import os
import re

base_dir = "/Users/biancaremster/antigravity projects"
areas_dir = os.path.join(base_dir, "areas")

def optimize_area_page(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Extract area name from H1 - this is the most reliable source
    # <h1>Cleaning Services in<br><em>Zilker</em></h1>
    area_match = re.search(r'<h1>Cleaning Services in<br><em>(.*?)</em></h1>', content)
    if area_match:
        area_name = area_match.group(1).strip()
    else:
        # Fallback if H1 changed
        area_match = re.search(r'<span class="breadcrumb-current">(.*?)</span>', content)
        area_name = area_match.group(1).strip() if area_match else "Austin"

    # Extract City and Zip from the file
    zip_match = re.search(r'<p class="area-hero-zip[^>]*>(.*?) — Zip Code (.*?)</p>', content)
    city_name = zip_match.group(1).strip() if zip_match else "Austin"
    zip_code = zip_match.group(2).strip() if zip_match else ""

    if city_name == "Serving": 
         filename = os.path.basename(filepath).replace(".html", "").replace("-", " ").title()
         city_name = filename

    new_title = f"House Cleaning in {area_name} | Scrubb ATX — Austin, TX"
    new_desc = f"Top-rated house cleaning in {area_name}, {city_name} ({zip_code}). Scrubb ATX: bonded, insured, eco-friendly cleaners. Free quotes. Same-week availability."

    # Update Title
    content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content)
    
    # Update Meta Description
    content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{new_desc}">', content)

    # Update OG Tags
    content = re.sub(r'<meta property="og:title" content=".*?"\s*/>', f'<meta property="og:title" content="{new_title}" />', content)
    content = re.sub(r'<meta property="og:description" content=".*?"\s*/>', f'<meta property="og:description" content="{new_desc}" />', content)
    content = re.sub(r'<meta name="twitter:title" content=".*?"\s*/>', f'<meta name="twitter:title" content="{new_title}" />', content)
    content = re.sub(r'<meta name="twitter:description" content=".*?"\s*/>', f'<meta name="twitter:description" content="{new_desc}" />', content)

    with open(filepath, 'w') as f:
        f.write(content)

for filename in os.listdir(areas_dir):
    if filename.endswith(".html"):
        optimize_area_page(os.path.join(areas_dir, filename))

print("Area pages re-optimized correctly.")
