import os
import glob

search_dir = '/Users/biancaremster/antigravity projects'

html_files = []
html_files.extend(glob.glob(os.path.join(search_dir, '*.html')))
html_files.extend(glob.glob(os.path.join(search_dir, 'areas', '*.html')))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacing variations of plant-derived
    content = content.replace('plant-derived', 'eco-friendly')
    content = content.replace('Plant-derived', 'Eco-friendly')
    content = content.replace('Plant-Derived', 'Eco-Friendly')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully processed {len(html_files)} HTML files for eco-friendly update.")
