import glob
import re

replacements = {
    'Your Brand Studio Elegance': 'MAYOOKHA Bridal Studio Elegance',
    'Your Brand Handcrafted Detail': 'MAYOOKHA Handcrafted Detail',
    'Your Brand Curated Radiance': 'MAYOOKHA Curated Bridal Silks',
    'Your Brand Bespoke Silhouettes': 'MAYOOKHA Bespoke Silhouettes',
    'Your Brand Occasion Wear': 'MAYOOKHA Occasion & Wedding Wear',
    'The Your Brand Gallery': 'The MAYOOKHA Bridal Gallery',
    'Styled by Your Brand': 'Styled by MAYOOKHA',
    'Why Choose Your Brand': 'Why Choose MAYOOKHA',
    'Handcrafted bespoke designer apparel by Your Brand.': 'Handcrafted bespoke bridal couture and designer apparel by MAYOOKHA.',
    'aria-label="Follow Your Brand on Instagram"': 'aria-label="Follow MAYOOKHA on Instagram"',
    'aria-label="Message Your Brand on WhatsApp"': 'aria-label="Message MAYOOKHA on WhatsApp"',
    '<div class="mobile-brand-title">Your Brand</div>': '<div class="mobile-brand-title">MAYOOKHA</div>',
    '<div class="footer-brand-title">Your Brand</div>': '<div class="footer-brand-title">MAYOOKHA</div>',
    '<div class="footer-brand-sub">Fashion & Apparel': '<div class="footer-brand-sub">The Bridal Studio · Celebrity Costume Designer',
    '<div class="footer-brand-sub">Fashion &amp; Apparel': '<div class="footer-brand-sub">The Bridal Studio · Celebrity Costume Designer',
    "subscribing to Your Brand updates": "subscribing to MAYOOKHA updates",
    "subscribing to the Your Brand": "subscribing to the MAYOOKHA",
    "&copy; 2026 Your Brand. All rights reserved.": "&copy; 2026 MAYOOKHA – The Bridal Studio. All rights reserved.",
    "&copy; 2026 Your Brand. All Rights Reserved.": "&copy; 2026 MAYOOKHA – The Bridal Studio. All rights reserved.",
    "Hello Your Brand, I would like to book a styling consultation": "Hello Mayookha, I would like to book a bridal styling consultation",
    "document.title = `${activeProduct.name} | Your Brand`;": "document.title = `${activeProduct.name} | MAYOOKHA – The Bridal Studio`;",
    "handcrafted with love by Your Brand": "handcrafted with love by MAYOOKHA",
    "handcrafted by Your Brand": "handcrafted by MAYOOKHA",
    "Your Brand": "MAYOOKHA",
}

for f in sorted(glob.glob('*.html')) + ['js/main.js', 'js/products.js', 'css/style.css']:
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    orig = text
    for k, v in replacements.items():
        text = text.replace(k, v)
    if text != orig:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(text)
        print(f"Cleaned {f}")
