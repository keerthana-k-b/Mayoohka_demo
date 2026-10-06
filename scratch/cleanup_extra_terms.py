import os

pages = ['index.html', 'collections.html', 'about.html', 'contact.html', 'reels.html', 'product-detail.html', '404.html']

for p in pages:
    path = os.path.join('D:/Mayoohka_demo', p)
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # Search placeholder
    c = c.replace('Search Ethnic Wear, Gowns, Silks, Handlooms...', 'Search Sarees, Bridal Lehengas, Silks, Blouses...')
    c = c.replace('Search Ethnic Wear, Western Wear, Occasion Wear...', 'Search Sarees, Bridal Lehengas, Silks, Blouses...')
    c = c.replace('Search Ethnic, Western, Festive Wear...', 'Search Sarees, Bridal Lehengas, Silks, Blouses...')
    
    # Dropdown subtitle
    c = c.replace('Pattu pavadai &amp; custom kids ethnic wear', 'Pattu pavada &amp; bespoke kids wear')
    
    # Reel category default
    c = c.replace('>Artisanal Craft</span>', '>Master Craft</span>')
    
    # Badges
    c = c.replace('>Artisanal Craft<', '>Master Craft<')
    
    # Signature Series in New Launch section
    c = c.replace('Signature Series - Royal Crimson Ensemble', 'Signature Bridal Edit - Royal Crimson Ensemble')
    c = c.replace('Signature Series - Antique Gold Embellished Ensemble', 'Signature Bridal Edit - Antique Gold Embellished Ensemble')
    c = c.replace('The Signature Series &mdash;', 'The Bridal Signature Edit &mdash;')
    c = c.replace('The Signature Series showcases', 'The Signature Bridal Edit showcases')
    
    # Contact option
    c = c.replace('value="Kids Ethnic Wear & Pattu Pavadai"', 'value="Kids Wear & Pattu Pavada"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)

    print(f"Cleaned extra terms in {p}")
