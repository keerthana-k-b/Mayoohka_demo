import re

def update_common_elements(html):
    # Brand Name and Title replacements
    html = re.sub(r'<title>.*?Your Brand.*?</title>', lambda m: m.group(0).replace('Your Brand', 'MAYOOKHA – The Bridal Studio'), html)
    html = html.replace('Your Brand | Contemporary Fashion &amp; Apparel', 'MAYOOKHA – The Bridal Studio | Premium Store &amp; Celebrity Costume Designer')
    html = html.replace('Your Brand | Contemporary Fashion & Apparel', 'MAYOOKHA – The Bridal Studio | Premium Store & Celebrity Costume Designer')
    html = html.replace('Your Brand — Bespoke &amp; Contemporary Collections', 'MAYOOKHA — Bespoke Bridal Couture &amp; Designer Collections')
    html = html.replace('About Our Brand &amp; Heritage | Your Brand', 'About Us &amp; Designer Story | MAYOOKHA – The Bridal Studio')
    html = html.replace('Contact &amp; Atelier Consultation | Your Brand', 'Contact Our Studio &amp; Appointments | MAYOOKHA – The Bridal Studio')
    html = html.replace('Watch &amp; Shop — Video Reels | Your Brand', 'Watch &amp; Shop Video Reels | MAYOOKHA – The Bridal Studio')
    html = html.replace('Product Details | Your Brand', 'Product Details | MAYOOKHA – The Bridal Studio')
    html = html.replace('Page Not Found | Your Brand', 'Page Not Found | MAYOOKHA – The Bridal Studio')

    # Meta descriptions
    html = re.sub(
        r'<meta name="description" content="[^"]*">',
        '<meta name="description" content="MAYOOKHA – The Bridal Studio by Celebrity Costume Designer Aiswarya Baiju in Cherthala, Kerala. Bespoke bridal sarees, Kanchipuram silks, lehengas, designer bridal blouses, and custom couture.">',
        html,
        count=1
    )
    html = re.sub(
        r'<meta property="og:description" content="[^"]*">',
        '<meta property="og:description" content="MAYOOKHA – The Bridal Studio by Celebrity Costume Designer Aiswarya Baiju in Cherthala, Kerala. Bespoke bridal sarees, Kanchipuram silks, lehengas, designer bridal blouses, and custom couture.">',
        html,
        count=1
    )
    html = re.sub(
        r'<meta property="og:title" content="[^"]*">',
        '<meta property="og:title" content="MAYOOKHA – The Bridal Studio | Celebrity Costume Designer">',
        html,
        count=1
    )

    # Wordmark in header and drawers
    html = re.sub(
        r'<div class="brand-text-wrap">\s*<span class="brand-main-text">Your Brand</span>\s*<span class="brand-sub-text">Fashion &amp; Apparel</span>\s*</div>',
        '<div class="brand-text-wrap">\n          <span class="brand-main-text">MAYOOKHA</span>\n          <span class="brand-sub-text">The Bridal Studio</span>\n        </div>',
        html
    )
    html = re.sub(
        r'<div class="brand-text-wrap">\s*<span class="brand-main-text">Your Brand</span>\s*<span class="brand-sub-text">Fashion & Apparel</span>\s*</div>',
        '<div class="brand-text-wrap">\n          <span class="brand-main-text">MAYOOKHA</span>\n          <span class="brand-sub-text">The Bridal Studio</span>\n        </div>',
        html
    )

    # Links, phone and WhatsApp
    html = html.replace('https://instagram.com/yourbrand', 'https://www.instagram.com/mayoohka_by_aiswarya_/')
    html = html.replace('@yourbrand', '@mayoohka_by_aiswarya_')
    html = html.replace('https://wa.me/919000000000', 'https://wa.me/918089101784')
    html = html.replace('wa.me/919000000000', 'wa.me/918089101784')
    html = html.replace('919000000000', '918089101784')
    html = html.replace('+91 90000 00000', '+91 8089101784')
    html = html.replace('+919000000000', '+918089101784')
    html = html.replace('tel:+919000000000', 'tel:+918089101784')
    html = html.replace('hello@yourbrand.com', 'contact@mayookha.com')
    html = html.replace('123 Main Street, Your City, Your State 000000', 'JohnThomas Memorial Building, Manorama Junction, Cherthala, Kerala 688524')
    html = html.replace('123 Main Street,<br>\n            Your City, Your State 000000', 'JohnThomas Memorial Building,<br>\n            Manorama Junction, Cherthala, Kerala 688524')
    html = html.replace('123 Main Street,<br> Your City, Your State 000000', 'JohnThomas Memorial Building,<br> Manorama Junction, Cherthala, Kerala 688524')
    html = html.replace('https://maps.google.com/?q=123+Main+Street+Your+City', 'https://maps.google.com/?q=JohnThomas+Memorial+Building,+Manorama+Junction,+Cherthala,+Kerala+688524')

    # Logo alt texts
    html = html.replace('alt="Your Brand Emblem"', 'alt="MAYOOKHA Emblem"')
    html = html.replace('alt="Your Brand Insignia"', 'alt="MAYOOKHA Emblem"')
    html = html.replace('aria-label="Your Brand - Home"', 'aria-label="MAYOOKHA - Home"')

    # Footer branding
    html = html.replace('<div class="footer-brand">Your Brand</div>', '<div class="footer-brand">MAYOOKHA</div>')
    html = html.replace('<div class="footer-tagline">Fashion &amp; Apparel</div>', '<div class="footer-tagline">The Bridal Studio · Celebrity Costume Designer</div>')
    html = html.replace(
        'A contemporary design studio celebrating fine craftsmanship, pure natural textiles, and bespoke tailoring for modern wardrobes.',
        'Cherthala’s premier bridal destination founded by Celebrity Costume Designer Aiswarya Baiju. Specializing in bespoke bridal sarees, Kanchipuram silks, lehengas, bridal blouses, and custom couture.'
    )
    html = html.replace('&copy; 2026 Your Brand. All Rights Reserved.', '&copy; 2026 MAYOOKHA – The Bridal Studio. All Rights Reserved.')

    return html

print("Helper ready")
