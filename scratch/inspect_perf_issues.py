import os
import re

pages = ['index.html', 'collections.html', 'about.html', 'contact.html', 'reels.html', 'product-detail.html', '404.html']

print("=== IMAGE AUDIT (width, height, loading, decoding) ===")
for p in pages:
    path = os.path.join('D:/Mayoohka_demo', p)
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # find all <img> tags
    imgs = re.findall(r'<img[^>]+>', c)
    no_w = [img for img in imgs if 'width=' not in img]
    no_h = [img for img in imgs if 'height=' not in img]
    no_lazy = [img for img in imgs if 'loading=' not in img]
    no_async = [img for img in imgs if 'decoding=' not in img]
    has_owner_png = 'owner.png' in c
    print(f"{p}: total {len(imgs)} imgs | missing width: {len(no_w)} | missing height: {len(no_h)} | missing loading: {len(no_lazy)} | missing decoding: {len(no_async)} | has owner.png: {has_owner_png}")

print("\n=== CSS 100vh AUDIT ===")
with open('D:/Mayoohka_demo/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()
vh_matches = [(i+1, line.strip()) for i, line in enumerate(css.splitlines()) if '100vh' in line]
print(f"Total 100vh occurrences in style.css: {len(vh_matches)}")
for lnum, line in vh_matches[:10]:
    print(f"  Line {lnum}: {line[:80]}")

print("\n=== SCRIPTS IN <HEAD> AUDIT ===")
for p in pages:
    path = os.path.join('D:/Mayoohka_demo', p)
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    head = c[c.find('<head>'):c.find('</head>')] if '<head>' in c else ''
    scripts = re.findall(r'<script[^>]*>', head)
    print(f"{p}: {len(scripts)} scripts in <head> -> {scripts}")
