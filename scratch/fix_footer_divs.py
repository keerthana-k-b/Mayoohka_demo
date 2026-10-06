pages = ['index.html', 'collections.html', 'about.html', 'contact.html', 'reels.html', 'product-detail.html', '404.html']

for p in pages:
    path = f'D:/Mayoohka_demo/{p}'
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # Look for:
    #           <div class="footer-brand-wrap">
    #             <img src="assets/images/logo-footer.png" alt="MAYOOKHA – The Bridal Studio" class="footer-logo-img" width="160" height="54" loading="lazy">
    #           </div>
    #           </div>
    bad = '''          <div class="footer-brand-wrap">
            <img src="assets/images/logo-footer.png" alt="MAYOOKHA – The Bridal Studio" class="footer-logo-img" width="160" height="54" loading="lazy">
          </div>
          </div>'''
    good = '''          <div class="footer-brand-wrap">
            <img src="assets/images/logo-footer.png" alt="MAYOOKHA – The Bridal Studio" class="footer-logo-img" width="160" height="54" loading="lazy">
          </div>'''

    if bad in c:
        c = c.replace(bad, good)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Fixed extra div in {p}")
    else:
        print(f"No extra div in {p}")
