import os
import re

base_dir = "/Users/biancaremster/antigravity projects"
areas_dir = os.path.join(base_dir, "areas")
domain = "https://scrubbatx.com"

def add_breadcrumb_schema(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    if 'BreadcrumbList' in content:
        return

    # Extract area name
    area_match = re.search(r'Cleaning Services in<br><em>(.*?)</em></h1>', content)
    area_name = area_match.group(1).strip() if area_match else "Austin"
    filename = os.path.basename(filepath)

    schema_html = f"""
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{domain}/"}},
        {{"@type": "ListItem", "position": 2, "name": "Service Areas", "item": "{domain}/#service-areas"}},
        {{"@type": "ListItem", "position": 3, "name": "{area_name}", "item": "{domain}/areas/{filename}"}}
      ]
    }}
    </script>"""

    content = content.replace('</head>', f'{schema_html}\n</head>')

    with open(filepath, 'w') as f:
        f.write(content)

for filename in os.listdir(areas_dir):
    if filename.endswith(".html"):
        add_breadcrumb_schema(os.path.join(areas_dir, filename))

print("Breadcrumb schema added to all area pages.")
