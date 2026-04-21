# 3D Printing Designs

This repo is structured to separate **private design work** from **public, sellable products** and automatically power a website.

---

## Core System

### Private (default)
All work goes here unless approved:

```
library/private/
```

Includes:
- In progress designs
- Personal prints
- Downloads
- Experiments
- Anything not ready for public

---

### Public (approved only)
Only items you WANT on your site:

```
library/public/
```

Rule:
> If it is not in public, it does not exist to the website.

---

## Website

```
website/
```

The site pulls from:

```
website/data/site-products.json
```

This file is AUTO-generated from:

```
library/public/
```

---

## Automation

On every push:

1. Script scans `library/public/`
2. Generates product list
3. Updates website data
4. Site deploys automatically

---

## How to Add a Product to the Site

1. Move product into:
```
library/public/<Category>/<ProductFolder>/
```

2. Push changes

Done. It will appear on the site.

---

## Important

- Nothing is public by default
- You control visibility by folder placement
- No manual website updates needed

---

## Future Improvements

- Product images
- Pricing + Etsy links
- Product descriptions
- Filtering + categories

---

## Goal

Keep everything clean, automated, and scalable while minimizing manual work.
