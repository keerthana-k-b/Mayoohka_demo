import re

pages = ['index.html', 'collections.html', 'about.html', 'contact.html', 'reels.html', 'product-detail.html', '404.html']
for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'<a href="index\.html" class="brand-link"[\s\S]*?</a>', content)
    if match:
        print(f"=== {p} ===")
        print(match.group(0))
    else:
        print(f"=== {p}: NOT FOUND ===")
