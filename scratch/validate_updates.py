import os
import re

main_dir = "/Users/biancaremster/Desktop/Scrubb ATX/scrubb"
areas_dir = os.path.join(main_dir, "areas")

# Target checks
forbidden_phrase = "within 2 hours"
als_phrase = "ALS Association"
hours_phrase = '<h4 class="footer-heading">Hours</h4>'

errors = []

# List of files to check
html_files = []
for f in os.listdir(main_dir):
    if f.endswith(".html"):
        html_files.append(os.path.join(main_dir, f))

for f in os.listdir(areas_dir):
    if f.endswith(".html"):
        html_files.append(os.path.join(areas_dir, f))

print(f"Checking {len(html_files)} HTML files for correctness...")

for filepath in html_files:
    rel_path = os.path.relpath(filepath, main_dir)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Check 1: Forbidden response time copy (case-insensitive)
    if forbidden_phrase.lower() in content.lower():
        # Make sure we ignore standard "24 hours" re-clean guarantee if applicable
        matches = [m.start() for m in re.finditer(forbidden_phrase, content, re.IGNORECASE)]
        if matches:
            errors.append(f"{rel_path}: Found forbidden phrase '{forbidden_phrase}'")

    # Check 2: ALS supporter info should be present
    if als_phrase not in content:
        errors.append(f"{rel_path}: Missing ALS supporter copy ('{als_phrase}')")

    # Check 3: Hours footer column should be removed
    if hours_phrase in content:
        errors.append(f"{rel_path}: Footer 'Hours' column is still present")

# Custom verification for Services Page
services_path = os.path.join(main_dir, "services.html")
if os.path.exists(services_path):
    with open(services_path, "r", encoding="utf-8") as f:
        content = f.read()
    if "Apartment & Condo" in content:
        errors.append("services.html: 'Apartment & Condo' service card was not removed")

if not errors:
    print("SUCCESS: All validation checks passed! Copy updates and layout adjustments are correct.")
else:
    print(f"FAILED: Found {len(errors)} validation errors:")
    for err in errors:
        print(f"  - {err}")
