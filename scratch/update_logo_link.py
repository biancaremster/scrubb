import os
import glob

search_dir = '/Users/biancaremster/antigravity projects'

html_files = []
html_files.extend(glob.glob(os.path.join(search_dir, '*.html')))
html_files.extend(glob.glob(os.path.join(search_dir, 'areas', '*.html')))

target_full_url = '"https://scrubbatx.com/logo.png"'
replacement_full_url = '"https://i.imgur.com/PSdNNW8.png"'

target_local = '"logo.png"'
replacement_local = '"https://i.imgur.com/PSdNNW8.png"'

processed_count = 0

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    content = content.replace(target_full_url, replacement_full_url)
    content = content.replace(target_local, replacement_local)

    if content != original_content:
        processed_count += 1
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Successfully replaced logo link in {processed_count} HTML files.")
