import os
import re

areas_dir = "/Users/biancaremster/Desktop/Scrubb ATX/scrubb/areas"

# Regex patterns
hours_pattern = re.compile(
    r'\s*<div class="footer-col">\s*<h4 class="footer-heading">Hours</h4>\s*<ul class="footer-list">\s*<li>Mon - Fri</li>\s*<li>8:00 am - 7:00 pm</li>\s*</ul>\s*</div>',
    re.MULTILINE | re.DOTALL
)

response_pattern = re.compile(
    r"We'll respond within 2 hours during business hours\.",
    re.IGNORECASE
)

footer_bottom_pattern = re.compile(
    r'<div class="footer-bottom">\s*<p>&copy; 2026 Scrubb ATX\. All rights reserved\.</p>',
    re.MULTILINE | re.DOTALL
)

print("Starting automation updates for area files...")

updated_count = 0
for filename in os.listdir(areas_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(areas_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # 1. Update response copy
        content = response_pattern.sub("We'll respond promptly during business hours.", content)

        # 2. Remove footer hours
        content = hours_pattern.sub("", content)

        # 3. Add ALS supporter info in footer bottom
        new_footer = (
            '<div class="footer-bottom">\n'
            '                <div class="footer-bottom-left">\n'
            '                    <p>&copy; 2026 Scrubb ATX. All rights reserved.</p>\n'
            '                    <p class="footer-als">Scrubb ATX is a proud supporter of the ALS Association — $2 of every clean is donated to the cause.</p>\n'
            '                </div>'
        )
        content = footer_bottom_pattern.sub(new_footer, content)

        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            updated_count += 1
            print(f"Updated: {filename}")

print(f"Done! Updated {updated_count} area HTML files.")
