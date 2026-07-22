import os

BASE_DIR = '/Users/macbookprom42025/Paddock/Scrubb'

# 1. Create site.webmanifest
manifest_path = os.path.join(BASE_DIR, 'site.webmanifest')
manifest_content = """{
  "name": "Scrubb ATX",
  "short_name": "Scrubb ATX",
  "icons": [
    {
      "src": "/logo.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/logo.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "theme_color": "#2c2c2c",
  "background_color": "#fbf9f4",
  "display": "standalone"
}
"""
with open(manifest_path, 'w', encoding='utf-8') as f:
    f.write(manifest_content)
print("Created site.webmanifest")

# 2. Inject favicon & manifest links into HTML files
for r, d, files in os.walk(BASE_DIR):
    if 'scratch' in r or '.git' in r:
        continue
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(r, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()

            if 'rel="icon"' in content:
                continue

            rel_logo = '../logo.png' if 'areas' in r or 'referrals' in r else 'logo.png'
            rel_manifest = '../site.webmanifest' if 'areas' in r or 'referrals' in r else 'site.webmanifest'

            favicon_tags = f"""
    <!-- Favicon & Web Manifest -->
    <link rel="icon" type="image/png" href="{rel_logo}">
    <link rel="manifest" href="{rel_manifest}">"""

            content = content.replace('</head>', favicon_tags + '\n</head>')
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

print("Injected favicon and manifest into all HTML files")
