import os
import glob

search_dir = '/Users/biancaremster/antigravity projects'

html_files = []
html_files.extend(glob.glob(os.path.join(search_dir, '*.html')))
html_files.extend(glob.glob(os.path.join(search_dir, 'areas', '*.html')))

target_string = '                    <p class="footer-tagline">Immaculate spaces.<br>Playful spirit.</p>\n'
target_string_alt = '<p class="footer-tagline">Immaculate spaces.<br>Playful spirit.</p>'

processed_count = 0

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    content = content.replace(target_string, '')
    content = content.replace(target_string_alt, '')

    if content != original_content:
        processed_count += 1
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Successfully removed tagline from {processed_count} HTML files.")
