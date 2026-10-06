import re
from rebrand_pages import update_common_elements
from rebrand_nav import apply_nav_and_footer

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Apply common updates (brand name, meta, phone, address, maps, WhatsApp, footer)
c = update_common_elements(c)
c = apply_nav_and_footer(c)
c = c.replace('placeholder="Search Ethnic Wear, Western Wear, Dresses..."', 'placeholder="Search Sarees, Bridal Silks, Lehengas, Custom Gowns..."')

# 1. Hero text overlay
old_hero_overlay = """        <!-- Centered Text Overlay with Soft Dark Gradient -->
        <div class="hero-overlay">
          <div class="hero-content">
            <span class="hero-eyebrow">Curated Fashion &amp; Bespoke Atelier</span>
            <h1 class="hero-headline">Crafted for Distinction, Tailored for Grace</h1>
            <p class="hero-subtitle">Handcrafted Silhouettes &amp; Made-to-Measure Elegance</p>
            <div class="hero-actions">
              <a href="collections.html" class="btn-hero-primary">Explore Collections</a>
              <a href="https://wa.me/918089101784?text=Hello%20Your%20Brand%2C%20I%20would%20like%20to%20book%20a%20styling%20consultation." target="_blank" rel="noopener" class="btn-hero-secondary">Book a Consultation</a>
            </div>
          </div>
        </div>"""

new_hero_overlay = """        <!-- Centered Text Overlay with Soft Dark Gradient -->
        <div class="hero-overlay">
          <div class="hero-content">
            <span class="hero-eyebrow">Bespoke Bridal Couture &bull; Celebrity Costume Designer</span>
            <h1 class="hero-headline">MAYOOKHA &ndash; The Bridal Studio</h1>
            <p class="hero-subtitle">Heirloom South Indian Silks, Bespoke Bridal Gowns &amp; Handcrafted Blouses</p>
            <div class="hero-actions">
              <a href="collections.html" class="btn-hero-primary">Explore Collections</a>
              <a href="https://wa.me/918089101784?text=Hello%20Mayookha%2C%20I%20would%20like%20to%20book%20a%20bridal%20styling%20consultation." target="_blank" rel="noopener" class="btn-hero-secondary">Book a Consultation</a>
            </div>
          </div>
        </div>"""

c = c.replace(old_hero_overlay, new_hero_overlay)

# 2. Announcement strip
old_announce = """    <div class="announcement-strip" id="announcement">
      <div class="container announcement-inner">
        <span class="announcement-text">
          Custom styling &amp; bespoke tailoring &nbsp;|&nbsp; Enquire on WhatsApp +91 8089101784
        </span>
        <a href="https://wa.me/918089101784?text=Hello%20Your%20Brand%2C%20I%20would%20like%20to%20enquire%20about%20custom%20designs." target="_blank" rel="noopener" class="announcement-btn">
          <span>Enquire Now</span>
          <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M5 13h11.86l-5.43 5.43 1.42 1.42L21.14 12l-8.29-8.29-1.42 1.42L16.86 11H5v2z"/></svg>
        </a>
      </div>
    </div>"""

new_announce = """    <div class="announcement-strip" id="announcement">
      <div class="container announcement-inner">
        <span class="announcement-text">
          Bespoke bridal styling &amp; celebrity costume design &nbsp;|&nbsp; WhatsApp: +91 8089101784 &bull; +91 8921001784
        </span>
        <a href="https://wa.me/918089101784?text=Hello%20Mayookha%2C%20I%20would%20like%20to%20enquire%20about%20bridal%20and%20custom%20designs." target="_blank" rel="noopener" class="announcement-btn">
          <span>Enquire Now</span>
          <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M5 13h11.86l-5.43 5.43 1.42 1.42L21.14 12l-8.29-8.29-1.42 1.42L16.86 11H5v2z"/></svg>
        </a>
      </div>
    </div>"""

c = c.replace(old_announce, new_announce)

# 3. Collections Grid with Primary & Hover images
old_coll_grid = re.search(r'<div class="collections-grid">.*?</div>\s*</div>\s*</section>', c, re.DOTALL)
if old_coll_grid:
    new_coll_grid = """<div class="collections-grid">
          <!-- Card 1: Sarees -->
          <a href="collections.html?c=sarees" class="collection-card reveal-on-scroll">
            <div class="collection-card-img-wrap">
              <img src="assets/images/collection-01.webp" alt="Sarees" class="collection-card-img primary-img" width="300" height="420" loading="lazy">
              <img src="assets/images/collection-01-hover.webp" alt="Sarees Detail" class="collection-card-img hover-img" width="300" height="420" loading="lazy">
              <div class="collection-card-overlay">
                <span class="collection-card-count">Explore Collection</span>
                <h3 class="collection-card-title">Sarees</h3>
                <span class="collection-card-link">View Collection &rarr;</span>
              </div>
            </div>
          </a>

          <!-- Card 2: Bridal Sarees -->
          <a href="collections.html?c=bridal-sarees" class="collection-card reveal-on-scroll">
            <div class="collection-card-img-wrap">
              <img src="assets/images/collection-02.webp" alt="Bridal Sarees" class="collection-card-img primary-img" width="300" height="420" loading="lazy">
              <img src="assets/images/collection-02-hover.webp" alt="Bridal Sarees Detail" class="collection-card-img hover-img" width="300" height="420" loading="lazy">
              <div class="collection-card-overlay">
                <span class="collection-card-count">Explore Collection</span>
                <h3 class="collection-card-title">Bridal Sarees</h3>
                <span class="collection-card-link">View Collection &rarr;</span>
              </div>
            </div>
          </a>

          <!-- Card 3: Lehengas -->
          <a href="collections.html?c=lehengas" class="collection-card reveal-on-scroll">
            <div class="collection-card-img-wrap">
              <img src="assets/images/collection-03.webp" alt="Lehengas" class="collection-card-img primary-img" width="300" height="420" loading="lazy">
              <img src="assets/images/collection-03-hover.webp" alt="Lehengas Detail" class="collection-card-img hover-img" width="300" height="420" loading="lazy">
              <div class="collection-card-overlay">
                <span class="collection-card-count">Explore Collection</span>
                <h3 class="collection-card-title">Lehengas</h3>
                <span class="collection-card-link">View Collection &rarr;</span>
              </div>
            </div>
          </a>

          <!-- Card 4: Bridal Blouses -->
          <a href="collections.html?c=bridal-blouses" class="collection-card reveal-on-scroll">
            <div class="collection-card-img-wrap">
              <img src="assets/images/collection-04.webp" alt="Bridal Blouses" class="collection-card-img primary-img" width="300" height="420" loading="lazy">
              <img src="assets/images/collection-04-hover.webp" alt="Bridal Blouses Detail" class="collection-card-img hover-img" width="300" height="420" loading="lazy">
              <div class="collection-card-overlay">
                <span class="collection-card-count">Explore Collection</span>
                <h3 class="collection-card-title">Bridal Blouses</h3>
                <span class="collection-card-link">View Collection &rarr;</span>
              </div>
            </div>
          </a>

          <!-- Card 5: Custom Dresses -->
          <a href="collections.html?c=custom-dresses" class="collection-card reveal-on-scroll">
            <div class="collection-card-img-wrap">
              <img src="assets/images/collection-05.webp" alt="Custom Dresses" class="collection-card-img primary-img" width="300" height="420" loading="lazy">
              <img src="assets/images/collection-05-hover.webp" alt="Custom Dresses Detail" class="collection-card-img hover-img" width="300" height="420" loading="lazy">
              <div class="collection-card-overlay">
                <span class="collection-card-count">Explore Collection</span>
                <h3 class="collection-card-title">Custom Dresses</h3>
                <span class="collection-card-link">View Collection &rarr;</span>
              </div>
            </div>
          </a>

          <!-- Card 6: Ready-mades -->
          <a href="collections.html?c=ready-mades" class="collection-card reveal-on-scroll">
            <div class="collection-card-img-wrap">
              <img src="assets/images/collection-06.webp" alt="Ready-mades" class="collection-card-img primary-img" width="300" height="420" loading="lazy">
              <img src="assets/images/collection-06-hover.webp" alt="Ready-mades Detail" class="collection-card-img hover-img" width="300" height="420" loading="lazy">
              <div class="collection-card-overlay">
                <span class="collection-card-count">Explore Collection</span>
                <h3 class="collection-card-title">Ready-mades</h3>
                <span class="collection-card-link">View Collection &rarr;</span>
              </div>
            </div>
          </a>

          <!-- Card 7: Kids Wear -->
          <a href="collections.html?c=kids-wear" class="collection-card reveal-on-scroll">
            <div class="collection-card-img-wrap">
              <img src="assets/images/collection-07.webp" alt="Kids Wear" class="collection-card-img primary-img" width="300" height="420" loading="lazy">
              <img src="assets/images/collection-07-hover.webp" alt="Kids Wear Detail" class="collection-card-img hover-img" width="300" height="420" loading="lazy">
              <div class="collection-card-overlay">
                <span class="collection-card-count">Explore Collection</span>
                <h3 class="collection-card-title">Kids Wear</h3>
                <span class="collection-card-link">View Collection &rarr;</span>
              </div>
            </div>
          </a>

          <!-- Card 8: Gents Wear -->
          <a href="collections.html?c=gents-wear" class="collection-card reveal-on-scroll">
            <div class="collection-card-img-wrap">
              <img src="assets/images/collection-08.webp" alt="Gents Wear" class="collection-card-img primary-img" width="300" height="420" loading="lazy">
              <img src="assets/images/collection-08-hover.webp" alt="Gents Wear Detail" class="collection-card-img hover-img" width="300" height="420" loading="lazy">
              <div class="collection-card-overlay">
                <span class="collection-card-count">Explore Collection</span>
                <h3 class="collection-card-title">Gents Wear</h3>
                <span class="collection-card-link">View Collection &rarr;</span>
              </div>
            </div>
          </a>
        </div>
      </div>
    </section>"""
    c = c[:old_coll_grid.start()] + new_coll_grid + c[old_coll_grid.end():]

# Collections header copy
c = c.replace(
    'From classic handcrafts to modern silhouettes, discover garments designed to make an enduring impression.',
    'From ceremonial South Indian bridal sarees and handloom Kasavu drapes to made-to-measure reception gowns and custom blouses.'
)

# 4. Mosaic Section
c = c.replace('alt="Our Community - Timeless Style &amp; Craft"', 'alt="Cherthala Flagship Bridal Studio"')
c = c.replace('alt="Artisanal Detailing in Every Stitch"', 'alt="Celebrity Costume Designer Aiswarya Baiju"')
c = c.replace('alt="Handcrafted Heritage Textiles"', 'alt="Intricate Maggam &amp; Zardozi Adda Needlework"')
c = c.replace('alt="Elegance in Motion - Studio Look"', 'alt="Bespoke Bridal Drapes &amp; Gowns"')

# 5. New Launch section
c = c.replace(
    'The Signature Series &mdash; Where ancestral craftsmanship meets contemporary silhouettes.',
    'The Muhurtham &amp; Reception Edit &mdash; Hand-painted organza and antique gold bridal silks.'
)
c = c.replace(
    'Discover our newest limited-edition capsule, featuring hand-woven heirloom silks, antique gold zardozi needlework, and meticulously structured bridal corsets designed for the modern bride.',
    'Curated by Celebrity Costume Designer Aiswarya Baiju, presenting painted tussar organza silks, pure antique gold Kanchipuram weaves, and sculptured evening gowns crafted for grand South Indian celebrations.'
)

# 6. Trust Strip
c = c.replace('Bespoke tailoring &amp; artisan handwork, stitched to your exact measurements and vision.', 'Bespoke bridal styling, hand maggam embroidery &amp; celebrity costume design stitched to perfection.')
c = c.replace('Quick replies for clients — consult, confirm, and customize without leaving your home.', 'Instant bridal assistance on WhatsApp — consult on sarees, share inspirations, and book fittings.')
c = c.replace('Premium silks, natural weaves, and fine embroidery — every stitch carries the Your Brand signature.', 'Pure Kanchipuram silks, Kerala Kasavu, and fine handloom weaves — every stitch carries the MAYOOKHA signature.')

# 7. Testimonials
c = c.replace(
    '"The craftsmanship and attention to detail on my custom ensemble were beyond expectations. The drape felt regal and effortless throughout the evening."',
    '"Aiswarya Baiju designed my Muhurtham Kanchipuram saree and custom blouse back work so flawlessly. The fitting needed zero adjustments!"'
)
c = c.replace('Elena R.', 'Ananya K.')
c = c.replace('Verified Buyer &middot; Gala Evening', 'Bride &middot; Muhurtham Wedding')

c = c.replace(
    '"My evening gown was tailored impeccably — not a single alteration needed. The styling team is remarkably responsive on WhatsApp and guided me through every choice."',
    '"For my wedding reception, Mayookha created a breathtaking blush pink mermaid gown. The team was extraordinarily responsive and guided every detail on WhatsApp."'
)
c = c.replace('Neethu M.', 'Dr. Divya M.')
c = c.replace('Verified Buyer &middot; Evening Couture', 'Bride &middot; Reception Couture')

c = c.replace(
    '"I wore a Your Brand handwoven ensemble for our annual gala and received endless compliments. The delicate hand-embroidery work is unmatched."',
    '"Our family ordered coordinating Kerala Kasavu sarees and mundu sets from Mayookha for Onam. The pure handloom quality is truly unmatched."'
)
c = c.replace('Meghna S.', 'Parvathy R.')
c = c.replace('Verified Buyer &middot; Festive Reception', 'Verified Client &middot; Traditional Festive')

# 8. Reels Carousel in index.html
reel_updates_home = [
    ('data-title="Aurelia Royal Zari Ensemble" data-price="₹48,500" data-category="Artisanal Craft"',
     'data-title="Samvrutha Crimson Bridal Kanchipuram" data-price="₹58,000" data-category="Bridal Sarees"'),
    ('alt="Aurelia Royal Zari Ensemble"', 'alt="Samvrutha Crimson Bridal Kanchipuram"'),
    ('<h3 class="reel-card-title">Aurelia Royal Zari Ensemble</h3>', '<h3 class="reel-card-title">Samvrutha Crimson Bridal Kanchipuram</h3>'),

    ('data-title="Celeste Scalloped Cathedral Gown" data-price="₹65,000" data-category="Western Wear"',
     'data-title="Seraphina Blush Pink Mermaid Bridal Gown" data-price="₹42,000" data-category="Custom Dresses"'),
    ('alt="Celeste Scalloped Cathedral Gown"', 'alt="Seraphina Blush Pink Mermaid Bridal Gown"'),
    ('<h3 class="reel-card-title">Celeste Scalloped Cathedral Gown</h3>', '<h3 class="reel-card-title">Seraphina Blush Pink Mermaid Bridal Gown</h3>'),

    ('data-title="Vrinda Handwoven Gold Drape" data-price="₹42,000" data-category="Casual Wear"',
     'data-title="Charulata Kasavu Weave Saree" data-price="₹8,500" data-category="Sarees"'),
    ('alt="Vrinda Handwoven Gold Drape"', 'alt="Charulata Kasavu Weave Saree"'),
    ('<h3 class="reel-card-title">Vrinda Handwoven Gold Drape</h3>', '<h3 class="reel-card-title">Charulata Kasavu Weave Saree</h3>'),

    ('data-title="Samira Fuchsia Zardozi Flared Set" data-price="₹72,000" data-category="Engagement & Reception"',
     'data-title="Aiswarya Signature Zardozi Bridal Blouse" data-price="₹14,500" data-category="Bridal Blouses"'),
    ('alt="Samira Fuchsia Zardozi Flared Set"', 'alt="Aiswarya Signature Zardozi Bridal Blouse"'),
    ('<h3 class="reel-card-title">Samira Fuchsia Zardozi Flared Set</h3>', '<h3 class="reel-card-title">Aiswarya Signature Zardozi Bridal Blouse</h3>'),

    ('data-title="Charulata Imperial Crimson Drape" data-price="₹54,000" data-category="Festive Collection"',
     'data-title="Nila Ivory Chevron Zari Lehenga Set" data-price="₹36,000" data-category="Lehengas"'),
    ('alt="Charulata Imperial Crimson Drape"', 'alt="Nila Ivory Chevron Zari Lehenga Set"'),
    ('<h3 class="reel-card-title">Charulata Imperial Crimson Drape</h3>', '<h3 class="reel-card-title">Nila Ivory Chevron Zari Lehenga Set</h3>'),

    ('data-title="Giselle Beaded Illusion Corset Gown" data-price="₹68,000" data-category="Western Wear"',
     'data-title="Aadya Handloom Rust Silk Saree" data-price="₹14,500" data-category="Sarees"'),
    ('alt="Giselle Beaded Illusion Corset Gown"', 'alt="Aadya Handloom Rust Silk Saree"'),
    ('<h3 class="reel-card-title">Giselle Beaded Illusion Corset Gown</h3>', '<h3 class="reel-card-title">Aadya Handloom Rust Silk Saree</h3>'),

    ('data-title="Atelier Gold Bullion Zardozi Blouse" data-price="₹32,000" data-category="Signature Series"',
     'data-title="Aravind Black Shirt & Kasavu Mundu Set" data-price="₹5,400" data-category="Gents Wear"'),
    ('alt="Atelier Gold Bullion Zardozi Blouse"', 'alt="Aravind Black Shirt & Kasavu Mundu Set"'),
    ('<h3 class="reel-card-title">Atelier Gold Bullion Zardozi Blouse</h3>', '<h3 class="reel-card-title">Aravind Black Shirt & Kasavu Mundu Set</h3>'),
]
for old, new in reel_updates_home:
    c = c.replace(old, new)

# 9. Clean up any remaining strings
c = c.replace('Hello Your Brand', 'Hello Mayookha')
c = c.replace('Your Brand studio', 'MAYOOKHA studio')
c = c.replace('Your Brand client look', 'MAYOOKHA client look')
c = c.replace('Your Brand Instagram story', 'MAYOOKHA Instagram story')
c = c.replace('Your Brand featured look', 'MAYOOKHA featured look')
c = c.replace('Enquire on WhatsApp: 918089101784', 'Enquire on WhatsApp: +91 8089101784')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("index.html updated successfully!")
