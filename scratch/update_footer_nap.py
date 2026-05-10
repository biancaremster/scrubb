import os
import re

base_dir = "/Users/biancaremster/antigravity projects"
areas_dir = os.path.join(base_dir, "areas")

nap_html = """
                    <address class="footer-nap">
                        <strong>Scrubb ATX</strong><br>
                        Austin, TX<br>
                        <a href="tel:+15125550123">(512) 555-0123</a><br>
                        <a href="mailto:hello@scrubbatx.com">hello@scrubbatx.com</a>
                    </address>"""

def update_footer_nap(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    if 'footer-nap' in content:
        return

    # Find the footer tagline and insert after it
    pattern = r'(<p class="footer-tagline">.*?</p>)'
    content = re.sub(pattern, rf'\1{nap_html}', content)

    with open(filepath, 'w') as f:
        f.write(content)

for filename in os.listdir(areas_dir):
    if filename.endswith(".html"):
        update_footer_nap(os.path.join(areas_dir, filename))

print("Footer NAP consistency applied to all area pages.")
