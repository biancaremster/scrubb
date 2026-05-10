import os
import re

base_dir = "/Users/biancaremster/antigravity projects"
areas_dir = os.path.join(base_dir, "areas")

def add_preloads(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    if 'rel="preload"' in content:
        return

    preload_html = """
    <!-- Preloads -->
    <link rel="preload" href="../logo.png" as="image">
    <link rel="preload" href="../styles.css" as="style">
"""
    # Insert before Google Fonts
    pattern = r'(<!-- Google Fonts -->|<link rel="preconnect")'
    if re.search(pattern, content):
        content = re.sub(pattern, rf'{preload_html}\n\1', content)
    else:
        content = content.replace('</head>', f'{preload_html}\n</head>')

    with open(filepath, 'w') as f:
        f.write(content)

for filename in os.listdir(areas_dir):
    if filename.endswith(".html"):
        add_preloads(os.path.join(areas_dir, filename))

print("Preloads added to all area pages.")
