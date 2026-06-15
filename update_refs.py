import os
import re

html_files = [
    r"c:\Users\bgsmi\OneDrive\Documents\sadhana hall\index.html",
    r"c:\Users\bgsmi\OneDrive\Documents\sadhana hall\meditation-hall.html",
    r"c:\Users\bgsmi\OneDrive\Documents\sadhana hall\community-kitchen.html",
    r"c:\Users\bgsmi\OneDrive\Documents\sadhana hall\music-academy.html",
    r"c:\Users\bgsmi\OneDrive\Documents\sadhana hall\yoga-centre.html",
    r"c:\Users\bgsmi\OneDrive\Documents\sadhana hall\spiritual-library.html",
    r"c:\Users\bgsmi\OneDrive\Documents\sadhana hall\residential-facilities.html",
    r"c:\Users\bgsmi\OneDrive\Documents\sadhana hall\youth-development.html",
]

def replace_ext(content):
    # Replace .jpg, .jpeg, .png (case-insensitive) with .webp in image src paths
    content = re.sub(r'(pics/[^"\']+?)\.(jpg|jpeg|png|JPG|JPEG|PNG)', lambda m: m.group(1) + '.webp', content)
    return content

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        original = f.read()
    updated = replace_ext(original)
    if updated != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"Updated: {os.path.basename(fpath)}")
    else:
        print(f"No changes: {os.path.basename(fpath)}")

print("Done.")
