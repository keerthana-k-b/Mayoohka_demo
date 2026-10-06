import re
import os

from rebrand_pages import update_common_elements
from rebrand_nav import apply_nav_and_footer

# ==========================================
# 1. 404.html
# ==========================================
print("Processing 404.html...")
with open('404.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = update_common_elements(c)
c = apply_nav_and_footer(c)
with open('404.html', 'w', encoding='utf-8') as f:
    f.write(c)

# ==========================================
# 2. product-detail.html
# ==========================================
print("Processing product-detail.html...")
with open('product-detail.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = update_common_elements(c)
c = apply_nav_and_footer(c)
c = c.replace('placeholder="Search Ethnic Wear, Western Wear, Dresses..."', 'placeholder="Search Sarees, Bridal Silks, Lehengas, Custom Gowns..."')
c = c.replace('Hello Your Brand, I would like to enquire about the', 'Hello Mayookha, I would like to enquire about the')
c = c.replace('Personalized styling &amp; sizing assistance by Your Brand', 'Personalized bridal styling &amp; sizing assistance by MAYOOKHA')
c = c.replace('Bespoke &amp; Contemporary Collections', 'Bespoke Bridal Couture &amp; Collections')
with open('product-detail.html', 'w', encoding='utf-8') as f:
    f.write(c)

# ==========================================
# 3. reels.html
# ==========================================
print("Processing reels.html...")
with open('reels.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = update_common_elements(c)
c = apply_nav_and_footer(c)
c = c.replace('placeholder="Search Ethnic Wear, Western Wear, Dresses..."', 'placeholder="Search Sarees, Bridal Silks, Lehengas, Custom Gowns..."')

# Update reel cards in reels.html
reel_updates = [
    ('data-title="Aurelia Royal Zari Ensemble" data-price="₹48,500" data-category="Artisanal Craft"',
     'data-title="Samvrutha Crimson Bridal Kanchipuram" data-price="₹58,000" data-category="Bridal Sarees"'),
    ('alt="Aurelia Silk Ensemble"', 'alt="Samvrutha Crimson Bridal Kanchipuram"'),
    ('aria-label="Play reel: Aurelia Royal Zari Ensemble"', 'aria-label="Play reel: Samvrutha Crimson Bridal Kanchipuram"'),
    ('<h3 class="reel-card-title">Aurelia Royal Zari Ensemble</h3>', '<h3 class="reel-card-title">Samvrutha Crimson Bridal Kanchipuram</h3>'),

    ('data-title="Celeste Scalloped Cathedral Gown" data-price="₹65,000" data-category="Western Wear"',
     'data-title="Seraphina Blush Pink Mermaid Bridal Gown" data-price="₹42,000" data-category="Custom Dresses"'),
    ('alt="Celeste Satin Evening Gown"', 'alt="Seraphina Blush Pink Mermaid Bridal Gown"'),
    ('aria-label="Play reel: Celeste Scalloped Cathedral Gown"', 'aria-label="Play reel: Seraphina Blush Pink Mermaid Bridal Gown"'),
    ('<h3 class="reel-card-title">Celeste Scalloped Cathedral Gown</h3>', '<h3 class="reel-card-title">Seraphina Blush Pink Mermaid Bridal Gown</h3>'),

    ('data-title="Vrinda Handwoven Gold Drape" data-price="₹42,000" data-category="Casual Wear"',
     'data-title="Charulata Kasavu Weave Saree" data-price="₹8,500" data-category="Sarees"'),
    ('alt="Vrinda Handwoven Linen Set"', 'alt="Charulata Kasavu Weave Saree"'),
    ('aria-label="Play reel: Vrinda Handwoven Gold Drape"', 'aria-label="Play reel: Charulata Kasavu Weave Saree"'),
    ('<h3 class="reel-card-title">Vrinda Handwoven Gold Drape</h3>', '<h3 class="reel-card-title">Charulata Kasavu Weave Saree</h3>'),

    ('data-title="Samira Fuchsia Zardozi Flared Set" data-price="₹72,000" data-category="Engagement & Reception"',
     'data-title="Aiswarya Signature Zardozi Bridal Blouse" data-price="₹14,500" data-category="Bridal Blouses"'),
    ('alt="Samira Fuchsia Flared Set"', 'alt="Aiswarya Signature Zardozi Bridal Blouse"'),
    ('aria-label="Play reel: Samira Fuchsia Zardozi Flared Set"', 'aria-label="Play reel: Aiswarya Signature Zardozi Bridal Blouse"'),
    ('<h3 class="reel-card-title">Samira Fuchsia Zardozi Flared Set</h3>', '<h3 class="reel-card-title">Aiswarya Signature Zardozi Bridal Blouse</h3>'),

    ('data-title="Charulata Crimson Silk Saree" data-price="₹54,000" data-category="Festive Collection"',
     'data-title="Nila Ivory Chevron Zari Lehenga Set" data-price="₹36,000" data-category="Lehengas"'),
    ('alt="Charulata Crimson Drape"', 'alt="Nila Ivory Chevron Zari Lehenga Set"'),
    ('aria-label="Play reel: Charulata Crimson Silk Saree"', 'aria-label="Play reel: Nila Ivory Chevron Zari Lehenga Set"'),
    ('<h3 class="reel-card-title">Charulata Crimson Silk Saree</h3>', '<h3 class="reel-card-title">Nila Ivory Chevron Zari Lehenga Set</h3>'),

    ('data-title="Giselle Beaded Tulle Evening Gown" data-price="₹68,000" data-category="Western Wear"',
     'data-title="Aadya Handloom Rust Silk Saree" data-price="₹14,500" data-category="Sarees"'),
    ('alt="Giselle Pleated Evening Gown"', 'alt="Aadya Handloom Rust Silk Saree"'),
    ('aria-label="Play reel: Giselle Beaded Tulle Evening Gown"', 'aria-label="Play reel: Aadya Handloom Rust Silk Saree"'),
    ('<h3 class="reel-card-title">Giselle Beaded Tulle Evening Gown</h3>', '<h3 class="reel-card-title">Aadya Handloom Rust Silk Saree</h3>'),

    ('data-title="Artisanal Embroidered Statement Jacket" data-price="₹32,000" data-category="Signature Series"',
     'data-title="Aravind Black Shirt & Kasavu Mundu Set" data-price="₹5,400" data-category="Gents Wear"'),
    ('alt="Artisanal Hand-Embroidered Vest"', 'alt="Aravind Black Shirt & Kasavu Mundu Set"'),
    ('aria-label="Play reel: Artisanal Embroidered Statement Jacket"', 'aria-label="Play reel: Aravind Black Shirt & Kasavu Mundu Set"'),
    ('<h3 class="reel-card-title">Artisanal Embroidered Statement Jacket</h3>', '<h3 class="reel-card-title">Aravind Black Shirt & Kasavu Mundu Set</h3>'),
]

for old, new in reel_updates:
    c = c.replace(old, new)

with open('reels.html', 'w', encoding='utf-8') as f:
    f.write(c)

# ==========================================
# 4. contact.html
# ==========================================
print("Processing contact.html...")
with open('contact.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = update_common_elements(c)
c = apply_nav_and_footer(c)
c = c.replace('placeholder="Search Ethnic Wear, Western Wear, Dresses..."', 'placeholder="Search Sarees, Bridal Silks, Lehengas, Custom Gowns..."')

# Update contact specifics
c = c.replace('<strong>Your Brand Flagship Store</strong>', '<strong>MAYOOKHA – The Bridal Studio</strong><br><span style="font-size:0.85rem;color:var(--text-muted);">Celebrity Costume Designer Aiswarya Baiju</span>')
c = c.replace(
    '<a href="tel:+918089101784">+91 8089101784</a>',
    '<a href="tel:+918089101784">+91 8089101784</a> &bull; <a href="tel:+918921001784">+91 8921001784</a>'
)
c = c.replace('Chat on WhatsApp: +91 8089101784 &rarr;', 'WhatsApp: +91 8089101784 &bull; +91 8921001784 &rarr;')

# Replace opening hours box
old_hours = """            <!-- Clearly Marked Sample Opening Hours Box -->
            <div class="sample-story-box" style="margin-top: 28px; margin-bottom: 0;">
              <span class="sample-story-label">Sample Opening Hours</span>
              <div style="font-size: 0.88rem; line-height: 1.7; color: var(--text-body);">
                <strong>[Sample Schedule:</strong><br>
                Monday – Saturday: 10:00 AM – 7:30 PM<br>
                Sunday: By Prior Appointment Only<br>
                <em>Personal styling sessions available by appointment]</em>
              </div>
            </div>"""

new_hours = """            <!-- Studio Visiting Hours -->
            <div class="sample-story-box" style="margin-top: 28px; margin-bottom: 0; border-left: 3px solid var(--accent-gold);">
              <span class="sample-story-label" style="background: var(--accent-gold); color: #000; font-weight: 600;">Store Hours &amp; Appointments</span>
              <div style="font-size: 0.88rem; line-height: 1.7; color: var(--text-body); margin-top: 6px;">
                <strong>Monday – Saturday:</strong> 10:00 AM – 8:00 PM<br>
                <strong>Sunday:</strong> By Prior Appointment Only<br>
                <em style="color: var(--text-muted); font-size: 0.82rem;">[Verified Store Hours Placeholder &bull; Walk-ins welcome &bull; Dedicated bridal styling by appointment]</em>
              </div>
            </div>"""

c = c.replace(old_hours, new_hours)

# Update form options
c = re.sub(
    r'<select id="consultEvent" class="form-select" required>.*?</select>',
    '''<select id="consultEvent" class="form-select" required>
                    <option value="" disabled selected>Select Category / Service Needed</option>
                    <option value="Bridal Sarees & Muhurtham Silks">Bridal Sarees &amp; Muhurtham Silks</option>
                    <option value="Bridal Lehengas & Dhavani Sets">Bridal Lehengas &amp; Dhavani Sets</option>
                    <option value="Bridal Blouses & Hand Maggam Work">Bridal Blouses &amp; Hand Maggam Work</option>
                    <option value="Custom Bridal Reception Gowns">Custom Bridal Reception Gowns</option>
                    <option value="Handcrafted Sarees (Kasavu, Organza, Silk)">Handcrafted Sarees (Kasavu, Organza, Silk)</option>
                    <option value="Ready-mades & Festive Coordinates">Ready-mades &amp; Festive Coordinates</option>
                    <option value="Kids Ethnic Wear & Pattu Pavadai">Kids Ethnic Wear &amp; Pattu Pavadai</option>
                    <option value="Gents Groomswear & Kasavu Mundu">Gents Groomswear &amp; Kasavu Mundu</option>
                    <option value="Celebrity & Bespoke Costume Designing">Celebrity &amp; Bespoke Costume Designing</option>
                  </select>''',
    c,
    flags=re.DOTALL
)

c = c.replace('We look forward to welcoming you to Your Brand.', 'We look forward to welcoming you to MAYOOKHA – The Bridal Studio, Cherthala.')

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(c)

# ==========================================
# 5. about.html
# ==========================================
print("Processing about.html...")
with open('about.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = update_common_elements(c)
c = apply_nav_and_footer(c)
c = c.replace('placeholder="Search Ethnic Wear, Western Wear, Dresses..."', 'placeholder="Search Sarees, Bridal Silks, Lehengas, Custom Gowns..."')

# Update story section
old_story_box = """            <!-- Clearly Marked Sample Story Box -->
            <div class="sample-story-box">
              <span class="sample-story-label">Our Story</span>
              <p class="about-story-text">
                [Sample Text: Founded with a vision for enduring elegance, Your Brand is a contemporary clothing studio offering bespoke tailoring and ready-to-wear collections. Driven by a deep respect for artisanal textile heritage and modern silhouettes, we bring clients a refined, personalized apparel experience.]
              </p>
              <p class="about-story-text">
                [Sample Text: Every garment is conceptualized through attentive design exploration, uniting authentic natural fabrics—from breathable organic linens to rich Mulberry silks—with hand embellishment and structured tailoring.]
              </p>
              <p class="about-story-text" style="margin-bottom: 0;">
                [Sample Text: Your Brand continues to serve clients seeking distinctive, versatile pieces that balance relaxed comfort with elevated sophistication.]
              </p>
            </div>"""

new_story_box = """            <div class="sample-story-box" style="border-left: 3px solid var(--accent-gold);">
              <span class="sample-story-label" style="background: var(--accent-gold); color: #000; font-weight: 600;">The Studio Story</span>
              <p class="about-story-text">
                Founded in Cherthala, Kerala by Celebrity Costume Designer <strong>Aiswarya Baiju</strong>, <strong>MAYOOKHA – The Bridal Studio</strong> is a premier bridal atelier and luxury destination dedicated to bespoke wedding couture, heirloom South Indian weaves, and master craftsmanship.
              </p>
              <p class="about-story-text">
                Specializing in pure Kanchipuram bridal silks, artisanal Kerala Kasavu drapes, intricately embellished bridal blouses, bespoke reception gowns, and celebratory family ensembles, every garment is thoughtfully conceptualized through one-on-one design consultations. We unite authentic heritage textiles with traditional adda frame zardozi, hand aari work, and flawless made-to-measure tailoring.
              </p>
              <p class="about-story-text" style="margin-bottom: 0;">
                From styling acclaimed cinema personalities and high-profile wedding parties to creating cherished bridal trousseaus for brides across the world, MAYOOKHA turns your bridal dreams into timeless heirlooms.
              </p>
            </div>"""

c = c.replace(old_story_box, new_story_box)

c = c.replace('<div class="about-story-badge-name">Atelier Design Studio</div>', '<div class="about-story-badge-name">Aiswarya Baiju</div>')
c = c.replace('<div class="about-story-badge-role">Dedicated to Artisanal Tailoring</div>', '<div class="about-story-badge-role">Celebrity Costume Designer &amp; Founder</div>')
c = c.replace('alt="Your Brand Design Studio Process"', 'alt="MAYOOKHA Bridal Studio Design Process"')
c = c.replace('define Your Brand apparel', 'define MAYOOKHA bridal creations')
c = c.replace('The art of thoughtful design, natural textiles, and artisanal tailoring crafted for timeless elegance.', 'Bespoke bridal styling, heirloom South Indian weaves, and celebrity costume design in Cherthala, Kerala.')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(c)

# ==========================================
# 6. collections.html
# ==========================================
print("Processing collections.html...")
with open('collections.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = update_common_elements(c)
c = apply_nav_and_footer(c)
c = c.replace('placeholder="Search Ethnic Wear, Western Wear, Dresses..."', 'placeholder="Search Sarees, Bridal Silks, Lehengas, Custom Gowns..."')

# Update filter pills
old_pills = """        <!-- Category Filter Pills -->
        <nav class="collections-filters-wrap" id="collectionsFilters" aria-label="Filter Collections">
          <button class="filter-pill active" data-slug="all" onclick="setCategoryFilter('all')">
            <span>All Collections</span>
            <span class="pill-count" id="count-all"></span>
          </button>
          <button class="filter-pill" data-slug="ethnic-wear" onclick="setCategoryFilter('ethnic-wear')">
            <span>Ethnic Wear</span>
            <span class="pill-count" id="count-ethnic-wear"></span>
          </button>
          <button class="filter-pill" data-slug="western-wear" onclick="setCategoryFilter('western-wear')">
            <span>Western Wear</span>
            <span class="pill-count" id="count-western-wear"></span>
          </button>
          <button class="filter-pill" data-slug="occasion-wear" onclick="setCategoryFilter('occasion-wear')">
            <span>Occasion Wear</span>
            <span class="pill-count" id="count-occasion-wear"></span>
          </button>
          <button class="filter-pill" data-slug="festive-collection" onclick="setCategoryFilter('festive-collection')">
            <span>Festive Collection</span>
            <span class="pill-count" id="count-festive-collection"></span>
          </button>
          <button class="filter-pill" data-slug="casual-wear" onclick="setCategoryFilter('casual-wear')">
            <span>Casual Wear</span>
            <span class="pill-count" id="count-casual-wear"></span>
          </button>
          <button class="filter-pill" data-slug="new-arrivals" onclick="setCategoryFilter('new-arrivals')">
            <span>New Arrivals</span>
            <span class="pill-count" id="count-new-arrivals"></span>
          </button>
          <button class="filter-pill" data-slug="artisanal-craft" onclick="setCategoryFilter('artisanal-craft')">
            <span>Artisanal Craft</span>
            <span class="pill-count" id="count-artisanal-craft"></span>
          </button>
          <button class="filter-pill" data-slug="signature-series" onclick="setCategoryFilter('signature-series')">
            <span>Signature Series</span>
            <span class="pill-count" id="count-signature-series"></span>
          </button>
        </nav>"""

new_pills = """        <!-- Category Filter Pills -->
        <nav class="collections-filters-wrap" id="collectionsFilters" aria-label="Filter Collections">
          <button class="filter-pill active" data-slug="all" onclick="setCategoryFilter('all')">
            <span>All Collections</span>
            <span class="pill-count" id="count-all"></span>
          </button>
          <button class="filter-pill" data-slug="sarees" onclick="setCategoryFilter('sarees')">
            <span>Sarees</span>
            <span class="pill-count" id="count-sarees"></span>
          </button>
          <button class="filter-pill" data-slug="bridal-sarees" onclick="setCategoryFilter('bridal-sarees')">
            <span>Bridal Sarees</span>
            <span class="pill-count" id="count-bridal-sarees"></span>
          </button>
          <button class="filter-pill" data-slug="lehengas" onclick="setCategoryFilter('lehengas')">
            <span>Lehengas</span>
            <span class="pill-count" id="count-lehengas"></span>
          </button>
          <button class="filter-pill" data-slug="bridal-blouses" onclick="setCategoryFilter('bridal-blouses')">
            <span>Bridal Blouses</span>
            <span class="pill-count" id="count-bridal-blouses"></span>
          </button>
          <button class="filter-pill" data-slug="custom-dresses" onclick="setCategoryFilter('custom-dresses')">
            <span>Custom Dresses</span>
            <span class="pill-count" id="count-custom-dresses"></span>
          </button>
          <button class="filter-pill" data-slug="ready-mades" onclick="setCategoryFilter('ready-mades')">
            <span>Ready-mades</span>
            <span class="pill-count" id="count-ready-mades"></span>
          </button>
          <button class="filter-pill" data-slug="kids-wear" onclick="setCategoryFilter('kids-wear')">
            <span>Kids Wear</span>
            <span class="pill-count" id="count-kids-wear"></span>
          </button>
          <button class="filter-pill" data-slug="gents-wear" onclick="setCategoryFilter('gents-wear')">
            <span>Gents Wear</span>
            <span class="pill-count" id="count-gents-wear"></span>
          </button>
        </nav>"""

c = c.replace(old_pills, new_pills)

c = c.replace('Bespoke &amp; Contemporary Collections', 'Bespoke Bridal Couture &amp; Designer Collections')
c = c.replace(
    'Curated traditional handloom textiles, tailored contemporary silhouettes, celebratory occasion wear, and timeless daily essentials.',
    'Pure Kanchipuram bridal silks, handloom Kerala Kasavu drapes, intricate designer blouses, made-to-measure reception gowns, and celebratory ethnic ensembles.'
)
c = c.replace('Hello Your Brand, I would like to enquire about the', 'Hello Mayookha, I would like to enquire about the')

with open('collections.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Pages 404, product-detail, reels, contact, about, collections updated successfully!")
