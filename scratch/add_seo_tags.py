import os
import re

base_dir = "/Users/biancaremster/antigravity projects"
areas_dir = os.path.join(base_dir, "areas")
domain = "https://scrubbatx.com"

def process_file(filepath, is_homepage=False):
    with open(filepath, 'r') as f:
        content = f.read()

    # Task 1.5: Fix lang attribute
    content = re.sub(r'<html([^>]*)>', r'<html\1 lang="en">', content)
    # Avoid duplicate lang="en"
    content = re.sub(r'lang="en"\s+lang="en"', 'lang="en"', content)

    # Get title and description for OG tags
    title_match = re.search(r'<title>(.*?)</title>', content)
    desc_match = re.search(r'<meta name="description" content="(.*?)">', content)
    
    title = title_match.group(1) if title_match else "Scrubb ATX"
    description = desc_match.group(1) if desc_match else ""
    
    filename = os.path.basename(filepath)
    if is_homepage:
        canonical_url = f"{domain}/"
    else:
        canonical_url = f"{domain}/areas/{filename}"

    og_tags = f"""
    <!-- Canonical -->
    <link rel="canonical" href="{canonical_url}" />

    <!-- Open Graph -->
    <meta property="og:type" content="website" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{description}" />
    <meta property="og:url" content="{canonical_url}" />
    <meta property="og:image" content="{domain}/logo.png" />
    <meta property="og:site_name" content="Scrubb ATX" />

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{title}" />
    <meta name="twitter:description" content="{description}" />
    <meta name="twitter:image" content="{domain}/logo.png" />"""

    # Insert after description or before </head>
    if '<meta name="description"' in content:
        content = re.sub(r'(<meta name="description" content="[^"]*">)', rf'\1{og_tags}', content)
    else:
        content = content.replace('</head>', f'{og_tags}\n</head>')

    with open(filepath, 'w') as f:
        f.write(content)

# Process index.html
process_file(os.path.join(base_dir, "index.html"), is_homepage=True)

# Process all files in areas/
for filename in os.listdir(areas_dir):
    if filename.endswith(".html"):
        process_file(os.path.join(areas_dir, filename))

print("SEO tags added to all pages.")
