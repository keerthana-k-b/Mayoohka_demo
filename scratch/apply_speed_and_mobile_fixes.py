import os
import re

pages = ['index.html', 'collections.html', 'about.html', 'contact.html', 'reels.html', 'product-detail.html', '404.html']

for p in pages:
    path = os.path.join('D:/Mayoohka_demo', p)
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Font optimization: load only required weights (reduces font request size)
    c = c.replace(
        'family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Montserrat:wght@300;400;500;600;700&display=swap',
        'family=Cormorant+Garamond:ital,wght@0,600;0,700;1,400&family=Montserrat:wght@400;500;600&display=swap'
    )

    # 2. Defer all scripts
    c = re.sub(r'<script src="([^"]+)"(?!\s+defer)>', r'<script src="\1" defer>', c)

    # 3. Add decoding="async" to all <img> tags that don't have it
    def add_decoding(match):
        img_tag = match.group(0)
        if 'decoding=' not in img_tag:
            return img_tag[:-1] + ' decoding="async">'
        return img_tag

    c = re.sub(r'<img[^>]+>', add_decoding, c)

    # 4. Page specific fixes:
    if p == 'index.html':
        # Add hero image preload in <head>
        preload_tag = '  <link rel="preload" as="image" href="assets/images/hero-01.webp" type="image/webp" fetchpriority="high">\n'
        if 'rel="preload" as="image"' not in c:
            c = c.replace('  <!-- Master Stylesheet', preload_tag + '  <!-- Master Stylesheet')

        # First hero image: fetchpriority="high" eager
        # Desktop hero panel 1:
        c = c.replace(
            '<img src="assets/images/hero-01.webp" alt="Contemporary Collection Look 1" width="360" height="570" loading="eager" decoding="async">',
            '<img src="assets/images/hero-01.webp" alt="Signature Celebrity Bridal Kasavu Saree Edit" width="360" height="570" loading="eager" fetchpriority="high" decoding="async">'
        )
        # Desktop hero panels 2-5: make lazy
        for num in ['02', '03', '04', '05']:
            c = c.replace(
                f'<img src="assets/images/hero-{num}.webp" alt="Contemporary Collection Look {int(num)}" width="360" height="570" loading="eager" decoding="async">',
                f'<img src="assets/images/hero-{num}.webp" alt="Bridal Couture Look {int(num)}" width="360" height="570" loading="lazy" decoding="async">'
            )
            c = c.replace(
                f'<img src="assets/images/hero-{num}.webp" alt="Contemporary Collection Look {int(num)}" width="360" height="570" loading="eager">',
                f'<img src="assets/images/hero-{num}.webp" alt="Bridal Couture Look {int(num)}" width="360" height="570" loading="lazy" decoding="async">'
            )

        # Mobile hero first slide:
        c = c.replace(
            '<img src="assets/images/hero-01.webp" alt="MAYOOKHA Bridal Studio Elegance" width="768" height="480" decoding="async">',
            '<img src="assets/images/hero-01.webp" alt="MAYOOKHA Bridal Studio Elegance" width="768" height="480" fetchpriority="high" loading="eager" decoding="async">'
        )

    if p == 'about.html':
        # Replace 916KB owner.png with 79KB owner.webp
        c = c.replace('assets/images/owner.png', 'assets/images/owner.webp')

    if p == 'collections.html':
        # Prepopulate pill counts to avoid CLS shift
        counts = {
            'count-all': '(34)',
            'count-sarees': '(8)',
            'count-bridal-sarees': '(6)',
            'count-lehengas': '(4)',
            'count-bridal-blouses': '(4)',
            'count-custom-dresses': '(4)',
            'count-ready-mades': '(3)',
            'count-kids-wear': '(2)',
            'count-gents-wear': '(3)'
        }
        for cid, val in counts.items():
            c = c.replace(f'<span class="pill-count" id="{cid}"></span>', f'<span class="pill-count" id="{cid}">{val}</span>')

        # Prepopulate results bar count
        c = c.replace(
            'Showing <strong class="collections-count-strong">0</strong> bespoke creations',
            'Showing <strong class="collections-count-strong">34</strong> bespoke creations'
        )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)

    print(f"Applied speed & mobile optimizations to {p}")
