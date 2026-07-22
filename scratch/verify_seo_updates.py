import os
import re
import json
import xml.etree.ElementTree as ET

BASE_DIR = '/Users/macbookprom42025/Paddock/Scrubb'

def verify():
    errors = []

    # 1. Sitemap verification
    sitemap_path = os.path.join(BASE_DIR, 'sitemap.xml')
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    locs = [url.find('s:loc', ns).text for url in root.findall('s:url', ns)]

    for loc in locs:
        if loc.endswith('.html'):
            errors.append(f"Sitemap contains .html extension: {loc}")
        if loc != 'https://scrubbatx.com/' and loc.endswith('/'):
            errors.append(f"Sitemap contains trailing slash on non-root URL: {loc}")

    required_urls = [
        'https://scrubbatx.com/',
        'https://scrubbatx.com/services',
        'https://scrubbatx.com/standard-house-cleaning',
        'https://scrubbatx.com/signature-deep-cleaning',
        'https://scrubbatx.com/faq',
        'https://scrubbatx.com/referrals',
        'https://scrubbatx.com/apartment-move-out-cleaning'
    ]
    for req in required_urls:
        if req not in locs:
            errors.append(f"Required URL missing from sitemap: {req}")

    # 2. Check html files for canonical tags, JSON-LD validity, and 555 phone numbers
    html_files = []
    for r, d, files in os.walk(BASE_DIR):
        if 'scratch' in r or '.git' in r:
            continue
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(r, f))

    for path in html_files:
        rel_path = os.path.relpath(path, BASE_DIR)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        if '555-0123' in content:
            errors.append(f"Found dummy phone number 555-0123 in {rel_path}")

        # Check canonical tag
        canonical_match = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', content)
        if canonical_match:
            c_url = canonical_match.group(1)
            if c_url.endswith('.html'):
                errors.append(f"Canonical URL has .html in {rel_path}: {c_url}")
            if c_url != 'https://scrubbatx.com/' and c_url.endswith('/'):
                errors.append(f"Canonical URL has trailing slash in {rel_path}: {c_url}")
        else:
            errors.append(f"Missing canonical tag in {rel_path}")

        # Check JSON-LD scripts
        ld_scripts = re.findall(r'<script\s+type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
        for idx, script_body in enumerate(ld_scripts):
            try:
                data = json.loads(script_body)
                # Verify FAQPage has mainEntity if FAQPage
                if data.get('@type') == 'FAQPage':
                    if 'mainEntity' not in data or len(data['mainEntity']) == 0:
                        errors.append(f"FAQPage schema in {rel_path} has empty mainEntity")
            except Exception as e:
                errors.append(f"Invalid JSON-LD in {rel_path} (script #{idx+1}): {e}")

    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for err in errors:
            print(" -", err)
    else:
        print(f"PASSED verification! Checked {len(locs)} sitemap URLs and {len(html_files)} HTML files successfully.")

if __name__ == '__main__':
    verify()
