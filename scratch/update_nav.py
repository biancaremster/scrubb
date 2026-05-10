import os
import re

base_dir = "/Users/biancaremster/antigravity projects"
areas_dir = os.path.join(base_dir, "areas")

def update_nav(filepath, is_homepage=False):
    with open(filepath, 'r') as f:
        content = f.read()

    # Determine paths
    services_link = "services.html" if is_homepage else "../services.html"
    faq_link = "faq.html" if is_homepage else "../faq.html"

    # Update Main Nav
    if 'href="services.html"' not in content and 'href="../services.html"' not in content:
        pattern = r'(<li><a href="[^"]*about" class="nav-link">About</a></li>)'
        content = re.sub(pattern, rf'\1\n                    <li><a href="{services_link}" class="nav-link">Services</a></li>', content)

    # Update Mobile Nav
    if 'href="services.html"' not in content and 'href="../services.html"' not in content:
        pattern = r'(<li><a href="[^"]*about" class="mobile-nav-link">About</a></li>)'
        content = re.sub(pattern, rf'\1\n            <li><a href="{services_link}" class="mobile-nav-link">Services</a></li>', content)

    # Update Footer Links
    if 'href="faq.html"' not in content and 'href="../faq.html"' not in content:
        pattern = r'(<li><a href="[^"]*contact">Contact</a></li>)'
        content = re.sub(pattern, rf'\1\n                            <li><a href="{faq_link}">FAQ</a></li>', content)

    with open(filepath, 'w') as f:
        f.write(content)

# Update index.html
update_nav(os.path.join(base_dir, "index.html"), is_homepage=True)

# Update all area pages
for filename in os.listdir(areas_dir):
    if filename.endswith(".html"):
        update_nav(os.path.join(areas_dir, filename), is_homepage=False)

print("Navigation updated across all pages.")
