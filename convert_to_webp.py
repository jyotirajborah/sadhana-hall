import os
from PIL import Image

base_dir = r"c:\Users\bgsmi\OneDrive\Documents\sadhana hall\pics"
extensions = ('.jpg', '.jpeg', '.png')
converted = []
failed = []

for root, dirs, files in os.walk(base_dir):
    for fname in files:
        ext = os.path.splitext(fname)[1].lower()
        if ext in extensions:
            src = os.path.join(root, fname)
            dst = os.path.join(root, os.path.splitext(fname)[0] + '.webp')
            try:
                with Image.open(src) as img:
                    img.save(dst, 'WEBP', quality=85)
                converted.append((src, dst))
                print(f"Converted: {src}")
            except Exception as e:
                failed.append((src, str(e)))
                print(f"FAILED: {src} -> {e}")

print(f"\nDone. {len(converted)} converted, {len(failed)} failed.")
for src, dst in converted:
    print(f"  {os.path.basename(src)} -> {os.path.basename(dst)}")
