import re
import os

pages = ['index.html', 'collections.html', 'about.html', 'contact.html', 'reels.html', 'product-detail.html', '404.html']

collections_html_block = '''        <div>
          <h3 class="footer-col-title">Collections</h3>
          <ul class="footer-links-list">
            <li><a href="collections.html?c=sarees" class="footer-link">Sarees</a></li>
            <li><a href="collections.html?c=bridal-sarees" class="footer-link">Bridal Sarees</a></li>
            <li><a href="collections.html?c=lehengas" class="footer-link">Lehengas</a></li>
            <li><a href="collections.html?c=bridal-blouses" class="footer-link">Bridal Blouses</a></li>
            <li><a href="collections.html?c=custom-dresses" class="footer-link">Custom Dresses</a></li>
            <li><a href="collections.html?c=ready-mades" class="footer-link">Ready-mades</a></li>
            <li><a href="collections.html?c=kids-wear" class="footer-link">Kids Wear</a></li>
            <li><a href="collections.html?c=gents-wear" class="footer-link">Gents Wear</a></li>
          </ul>
        </div>'''

for p in pages:
    path = os.path.join('D:/Mayoohka_demo', p)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Favicon links
    content = re.sub(
        r'<link rel="icon" type="image/png" sizes="32x32" href="[^"]+">',
        '<link rel="icon" type="image/png" sizes="32x32" href="assets/images/favicon.png">',
        content
    )
    content = re.sub(
        r'<link rel="icon" type="image/png" sizes="16x16" href="[^"]+">',
        '<link rel="icon" type="image/png" sizes="16x16" href="assets/images/favicon.png">',
        content
    )
    content = re.sub(
        r'<link rel="apple-touch-icon"[^>]*>',
        '<link rel="apple-touch-icon" sizes="180x180" href="assets/images/favicon.png">',
        content
    )
    if 'favicon.ico' not in content:
        content = content.replace(
            '<link rel="apple-touch-icon" sizes="180x180" href="assets/images/favicon.png">',
            '<link rel="apple-touch-icon" sizes="180x180" href="assets/images/favicon.png">\n  <link rel="shortcut icon" href="favicon.ico">'
        )

    # 2. Update Header Brand Link:
    # Look for <a href="index.html" class="brand-link" ...> ... </a>
    # Replace logo-badge.png with logo-header.png
    content = re.sub(
        r'<img\s+src="assets/images/logo-badge\.png"\s+alt="MAYOOKHA Emblem"\s+class="brand-badge-img"[^>]*>',
        '<img src="assets/images/logo-header.png" alt="MAYOOKHA – The Bridal Studio" class="brand-logo-img" width="160" height="48">',
        content
    )
    content = re.sub(
        r'<img\s+src="assets/images/logo-badge\.png"\s+alt="MAYOOKHA Logo"\s+class="brand-badge-img"[^>]*>',
        '<img src="assets/images/logo-header.png" alt="MAYOOKHA – The Bridal Studio" class="brand-logo-img" width="160" height="48">',
        content
    )
    content = re.sub(
        r'<img\s+src="assets/images/logo-badge\.png"\s+alt="[^"]*"\s+class="brand-badge-img"[^>]*>',
        '<img src="assets/images/logo-header.png" alt="MAYOOKHA – The Bridal Studio" class="brand-logo-img" width="160" height="48">',
        content
    )

    # 3. Update Footer Brand:
    # Replace footer-brand-wrap content with logo-footer.png
    content = re.sub(
        r'<div class="footer-brand-wrap">\s*<img src="assets/images/logo-badge\.png"[^>]*>[\s\S]*?</div>\s*</div>',
        '<div class="footer-brand-wrap">\n            <img src="assets/images/logo-footer.png" alt="MAYOOKHA – The Bridal Studio" class="footer-logo-img" width="160" height="54" loading="lazy">\n          </div>',
        content
    )

    # 4. Remove fake email from footer
    # Remove block:
    # <p class="footer-contact-item">\s*<strong>Email:</strong>[\s\S]*?</p>
    content = re.sub(
        r'<p class="footer-contact-item">\s*<strong>Email:</strong>\s*<br>\s*<a href="mailto:[^"]+">[^<]+</a>\s*</p>',
        '',
        content
    )
    content = re.sub(
        r'<a href="mailto:hello@mayoohka[^"]*">[^<]*</a>',
        '',
        content
    )

    # 5. Replace Footer Collections Block
    # Look for <div>\s*<h3 class="footer-col-title">Collections</h3>[\s\S]*?</ul>\s*</div>
    content = re.sub(
        r'<div>\s*<h3 class="footer-col-title">Collections</h3>\s*<ul class="(?:footer-links|footer-links-list)">[\s\S]*?</ul>\s*</div>',
        collections_html_block,
        content
    )

    # 6. Ensure footer SVGs have width="20" height="20"
    # Footer social SVGs in index.html
    content = content.replace(
        '<svg viewBox="0 0 24 24"><path d="M12 2.163c3.204',
        '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M12 2.163c3.204'
    )
    content = content.replace(
        '<svg viewBox="0 0 24 24"><path d="M12.04 2c-5.46',
        '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M12.04 2c-5.46'
    )

    # 7. Page specific fixes:
    if p == '404.html':
        content = content.replace('Ethnic Wear</a>', 'Sarees</a>')
        content = content.replace('Western Wear</a>', 'Bridal Sarees</a>')
        content = content.replace('Occasion Wear</a>', 'Lehengas</a>')
        content = content.replace('c=ethnic-wear', 'c=sarees')
        content = content.replace('c=western-wear', 'c=bridal-sarees')
        content = content.replace('c=occasion-wear', 'c=lehengas')

    if p == 'contact.html':
        content = content.replace('Kids Ethnic Wear &amp; Pattu Pavadai', 'Kids Wear &amp; Pattu Pavada')

    # Remove any corrupted character in footer-brand-sub
    content = content.replace('The Bridal Studio  Celebrity Costume Designer', 'The Bridal Studio · Celebrity Costume Designer')
    content = content.replace('MAYOOKHA  The Bridal Studio', 'MAYOOKHA – The Bridal Studio')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {p}")
