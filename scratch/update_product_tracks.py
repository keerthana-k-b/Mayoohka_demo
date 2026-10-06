import json
import re
import urllib.parse

with open('scratch/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

print(f"Loaded {len(products)} products from scratch/products.json")
prod_map = {p['id']: p for p in products}

def make_card(prod, prefix, idx, is_reveal=False):
    reveal_class = ' reveal-on-scroll' if is_reveal else ''
    pid = f"prod-{prefix}-{idx}"
    wa_msg = urllib.parse.quote(f"Hello Mayookha, I am enquiring about the {prod['name']} ({prod['price']}). Please share details.")
    wa_url = f"https://wa.me/918089101784?text={wa_msg}"
    
    badge_span = f'<span class="product-badge">{prod["badge"]}</span>' if prod.get('badge') else ''
    badge_tag = f'<span class="product-badge-tag">{prod["badge"]}</span>' if prod.get('badge') else '<span class="product-badge-tag">Bespoke Fit</span>'
    
    img = prod['images'][0]
    fabric_prefix = prod.get('fabric', 'Handcrafted').split('&')[0].strip()
    category_meta = f"{prod['categoryName']} / {fabric_prefix}"
    
    return f"""                <!-- Product {idx} -->
                <div class="product-card{reveal_class}" data-product-id="{pid}" data-name="{prod['name']}" data-category="{category_meta}" data-price="{prod['price']}" data-img="{img}" data-badge="{prod['badge']}" data-desc="{prod['description']}">
                  <div class="product-img-wrap">
                    <img src="{img}" alt="{prod['name']}" class="product-img" width="295" height="380" loading="lazy">
                    {badge_span}
                    <button class="product-wishlist-btn" aria-label="Save to Wishlist" onclick="toggleWishlist('{pid}', this)">
                      <svg viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
                    </button>
                    <div class="product-hover-actions">
                      <button class="btn-quick-view" onclick="openQuickView('{pid}')">
                        <svg viewBox="0 0 24 24"><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg>
                        <span>Quick View</span>
                      </button>
                    </div>
                  </div>
                  <div class="product-info">
                    <div class="product-meta">{category_meta}</div>
                    <h3 class="product-title">{prod['name']}</h3>
                    <div class="product-pricing">
                      <span class="product-price">{prod['price']}</span>
                      {badge_tag}
                    </div>
                    <a href="{wa_url}" target="_blank" rel="noopener" class="btn-product-enquire">
                      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18" fill="#fff" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>
                      <span>Enquire on WhatsApp</span>
                    </a>
                  </div>
                </div>"""

na_ids = ['prod-01', 'prod-02', 'prod-15', 'prod-23', 'prod-28', 'prod-30', 'prod-32', 'prod-06', 'prod-25']
bs_ids = ['prod-09', 'prod-10', 'prod-11', 'prod-16', 'prod-19', 'prod-20', 'prod-05', 'prod-13', 'prod-03']
ft_ids = ['prod-04', 'prod-14', 'prod-17', 'prod-18', 'prod-21', 'prod-22', 'prod-24', 'prod-33', 'prod-34']

na_cards = "\n\n".join([make_card(prod_map[pid], 'na', i+1, is_reveal=(i>=5)) for i, pid in enumerate(na_ids)])
bs_cards = "\n\n".join([make_card(prod_map[pid], 'bs', i+1, is_reveal=(i>=5)) for i, pid in enumerate(bs_ids)])
ft_cards = "\n\n".join([make_card(prod_map[pid], 'ft', i+1, is_reveal=(i>=5)) for i, pid in enumerate(ft_ids)])

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Tab 1 Track
p1 = r'(<div class="product-tab-panel active" id="tab-new-arrivals" role="tabpanel">\s*<div class="product-carousel" data-carousel="new-arrivals">\s*<div class="product-track">).*?(</div>\s*</div>\s*</div>\s*<!-- Tab 2)'
repl1 = r'\g<1>\n' + na_cards + r'\n              \g<2>'
html = re.sub(p1, repl1, html, flags=re.DOTALL)

# Replace Tab 2 Track
p2 = r'(<div class="product-tab-panel" id="tab-best-sellers" role="tabpanel">\s*<div class="product-carousel" data-carousel="best-sellers">\s*<div class="product-track">).*?(</div>\s*</div>\s*</div>\s*<!-- Tab 3)'
repl2 = r'\g<1>\n' + bs_cards + r'\n              \g<2>'
html = re.sub(p2, repl2, html, flags=re.DOTALL)

# Replace Tab 3 Track
p3 = r'(<div class="product-tab-panel" id="tab-featured" role="tabpanel">\s*<div class="product-carousel" data-carousel="featured">\s*<div class="product-track">).*?(</div>\s*</div>\s*</div>\s*</div>\s*<!-- /product-carousel-wrapper -->)'
repl3 = r'\g<1>\n' + ft_cards + r'\n              \g<2>'
html = re.sub(p3, repl3, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html product tracks successfully!")
