import os
import json

BASE = 'Final_Products'
OUTPUT = 'website/data/site-products.json'

products = []

for root, dirs, files in os.walk(BASE):
    for file in files:
        if file.lower().endswith(('.stl', '.3mf')):
            rel_path = os.path.join(root, file)
            parts = rel_path.split(os.sep)
            category = parts[1] if len(parts) > 2 else 'Other'
            name = os.path.splitext(file)[0]
            products.append({
                'name': name,
                'category': category,
                'file': rel_path.replace('\\', '/'),
                'extension': os.path.splitext(file)[1].lower(),
                'size_mb': round(os.path.getsize(rel_path) / (1024 * 1024), 3),
                'image': ''
            })

products.sort(key=lambda p: (p['category'].lower(), p['name'].lower()))

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
with open(OUTPUT, 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2)

print(f"Generated {len(products)} products")
