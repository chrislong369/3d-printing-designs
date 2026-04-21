import os
import json

BASE = 'library/public'
OUTPUT = 'website/data/site-products.json'

products = []

for root, dirs, files in os.walk(BASE):
    for file in files:
        if file.endswith('.stl') or file.endswith('.3mf'):
            rel_path = os.path.join(root, file)
            parts = rel_path.split(os.sep)

            try:
                category = parts[2]
            except:
                category = 'Other'

            name = os.path.splitext(file)[0]

            products.append({
                'name': name,
                'category': category,
                'file': rel_path.replace('\\','/'),
                'image': ''
            })

with open(OUTPUT, 'w') as f:
    json.dump(products, f, indent=2)

print(f"Generated {len(products)} products")
