# Template Conversion Master Plan: "Your Brand" Clothing Store

> Comprehensive inventory of all brand-specific, bridal-specific, and demo-specific elements across the codebase (`D:\Clothing_Template`), along with proposed brand-neutral replacements for approval before implementation.

---

## 1. Brand, Owner, Tagline & Geographical Locations

### 1.1 Current Brand & Owner Items
* **Brand Name**: `M LOFT`, `M. LOFT`, `M LOFT by Joel Jacob Mathew`, `M. Loft Legacy`
* **Owner / Designer**: `Joel Jacob Mathew`, `by Joel Jacob Mathew`, `Joel Jacob Mathew Atelier`
* **Brand Subtext**: `by Joel Jacob Mathew` (in desktop header, mobile drawer, footer on all 7 HTML pages)
* **Taglines & Subtitles**:
  * "Bespoke Bridal Couture & Occasion Wear Boutique"
  * "Bespoke bridal couture and occasion wear boutique in Changanassery, Kerala."
  * "The art of bespoke bridal design, time-honored South Indian handloom traditions, and couture craftsmanship."
  * "Founded by designer Joel Jacob Mathew, M LOFT is a premier bespoke bridal couture boutique..."
  * "Inspired by royal Kerala ceremonial artistry, the M. Loft Legacy capsule..."
* **Locations**:
  * `Changanassery, Kerala 686101`
  * `Changanassery, Kottayam District, Kerala, India`
  * `Changanassery flagship atelier` / `Changanassery boutique`
  * `Kerala` / `Kottayam`

### 1.2 Proposed Replacements (Phase 1)
* **Brand Name**: `Your Brand` (exact logo styling and wordmark typography preserved)
* **Owner Name**: *Removed everywhere* (header sub-text, about page, footer, titles, alt text, JS defaults)
* **Brand Subtext**: `Fashion & Apparel`
* **Tagline & Description**:
  * Tagline: `Fashion & Apparel`
  * Description: `Contemporary fashion, signature silhouettes, and everyday apparel crafted with timeless elegance.`
  * About Page Story: Neutral clothing brand narrative focusing on textile quality, modern tailoring, artisanal finishing, and personalized customer care.
* **Address**: `123 Main Street, Your City, Your State 000000` (consistent across footer, contact page, metadata)
* **Locations**: All references to Changanassery, Kottayam, and Kerala replaced with generic store references ("our flagship store", "our studio atelier").

---

## 2. Contact Details & Social Links

| Field | Current Demo Value | Proposed Brand-Neutral Value | Notes & Files |
| :--- | :--- | :--- | :--- |
| **WhatsApp Raw** | `918075909720` | `919000000000` | Used in `wa.me/919000000000` URLs across all HTML pages & `js/main.js` |
| **Phone Display** | `8075909720` / `+91 80759 09720` | `+91 90000 00000` | Header, drawer, contact card, floating tooltips |
| **Phone Tel URI** | `tel:8075909720` / `tel:+918075909720` | `tel:+919000000000` | Click-to-call links across all HTML pages |
| **Instagram URL** | `https://www.instagram.com/mloft_by_joeljacobmathew/` | `https://instagram.com/yourbrand` | Header, drawer, footer, contact page |
| **Instagram Handle** | `@mloft_by_joeljacobmathew` | `@yourbrand` | Section headers, card tags |
| **Email** | None currently present | `hello@yourbrand.com` | Added to contact cards & footer |
| **Physical Address** | Changanassery, Kerala 686101 | `123 Main Street, Your City, Your State 000000` | Footer & contact page |
| **Google Maps Embed** | `https://maps.app.goo.gl/oqBwRcnb2jX92qv67` (in `contact.html`) | `https://maps.google.com/?q=123+Main+Street+Your+City` | Single easy-to-find link in `contact.html` |

*Note: These match the exact replacement keys expected by `make_client.py`.*

---

## 3. Categories, Slugs & Dependent Logic

### 3.1 Current vs Proposed Category Architecture
The template has 8 distinct catalog categories plus "all". To keep the exact structure, dropdowns, and count badges working seamlessly, we map all 8 to generic apparel collections:

| Slug | Current Name | Current Description | Proposed Slug | Proposed Name | Proposed Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `all` | All Collections | Complete bespoke bridal couture & occasion wear | `all` | All Collections | Complete contemporary fashion & apparel |
| `hindu-bride` | Hindu Bride | Kanchipuram & temple Korvai weaves | `ethnic-wear` | Ethnic Wear | Traditional silhouettes & handcrafted festive weaves |
| `christian-bride` | Christian Bride | Cathedral veils & corset gowns | `western-wear` | Western Wear | Tailored suits, evening dresses & modern silhouettes |
| `engagement` | Engagement Wear | Pastel lehengas & modern luxury | `occasion-wear` | Occasion Wear | Statement ensembles & celebratory evening wear |
| `white-gown` | White Gowns | Handcrafted bespoke western couture | `festive-collection`| Festive Collection | Rich textures, festive palettes & artisanal craft |
| `pavithrappattu` | Pavithrappattu | Heritage silk & metallic Kasavu zari | `casual-wear` | Casual Wear | Everyday luxury, breathable coordinates & essentials |
| `roja` | Roja Collection | Signature crimson silks & hand embroidery | `new-arrivals` | New Arrivals | Fresh seasonal drops & contemporary edits |
| `handwork` | Handwork Details | Artisanal zardozi, dabka & cutwork | `artisanal-craft` | Artisanal Craft | Hand embroidery, detailed beadwork & textures |
| `legacy` | M. Loft Legacy | Signature royal archives & festive silhouettes | `signature-series`| Signature Series | Exclusive house archives & tailored capsule pieces |

### 3.2 Dependent Code Requiring Coordinated Updates
1. **`js/products.js`**:
   - `CATEGORIES` array: update `slug`, `name`, `desc`.
   - `PRODUCTS` array: update `category` slug and `categoryName` on all 34 items.
2. **`collections.html`**:
   - Filter pill buttons: `data-slug="ethnic-wear"`, `onclick="setCategoryFilter('ethnic-wear')"`.
   - Count badge element IDs: `id="count-ethnic-wear"`, `id="count-western-wear"`, etc.
   - Dropdown links in header & mobile drawer: `collections.html?c=ethnic-wear`, etc.
   - Subtitle text & search placeholder: "Search Ethnic Wear, Western Wear, Dresses...".
3. **`index.html`**:
   - Header dropdown & mobile drawer collections list: updated to new slugs and names.
   - Collections Section (`#collections`): 8 collection cards updated with new titles, descriptions, and links.
   - Product Showcase Tabs (`#products`):
     - `data-tab="tab-new-arrivals"` (already generic tab ID)
     - `data-tab="tab-best-sellers"`
     - `data-tab="tab-featured"`
     - Product cards `data-category`: update values to match new category names (e.g. `Ethnic Wear`, `Western Wear`, `Occasion Wear`).
4. **All other HTML pages (`about.html`, `contact.html`, `reels.html`, `product-detail.html`, `404.html`)**:
   - Synchronize desktop dropdown cards and mobile drawer accordion links to the new category slugs and names.
5. **`reels.html` & `index.html` Reels Carousel**:
   - Update `data-category` on reel cards (e.g. `Ethnic Wear`, `Western Wear`, `Occasion Wear`, `Festive Collection`, `Casual Wear`).

---

## 4. Product Catalog (34 Master Items + 15 Homepage Cards)

### 4.1 Master Catalog (`js/products.js`)
All 34 products will be rewritten with generic apparel names, realistic prices, and clean fabric/work specifications without bridal/temple/religious/location terms:

| ID | Current Name & Price | Proposed Name | Proposed Price | Proposed Category |
| :--- | :--- | :--- | :--- | :--- |
| `hb-1` | Aurelia Royal Crimson Kanchipuram Saree (₹48,500) | Aurelia Crimson Silk Kurta Set | ₹18,500 | `ethnic-wear` |
| `hb-2` | Ananya Saffron Sheer Veil Bridal Ensemble (₹56,000) | Ananya Saffron Organza Anarkali | ₹22,000 | `ethnic-wear` |
| `hb-3` | Mayura Tangerine Korvai Silk Saree (₹51,000) | Mayura Tangerine Silk Ensemble | ₹19,500 | `ethnic-wear` |
| `hb-4` | Kalyani Temple Gold Silk Drape (₹53,000) | Kalyani Woven Gold Silk Suit | ₹21,000 | `ethnic-wear` |
| `hb-5` | Samriddhi Heirloom Sister Silk Drapes (₹44,000) | Samriddhi Festive Silk Coord Set | ₹16,500 | `ethnic-wear` |
| `hb-6` | Devika Crimson Veil & Polki Bridal Set (₹62,000) | Devika Crimson Velvet Jacket Suit | ₹24,000 | `ethnic-wear` |
| `cb-1` | Seraphina French Lace Cathedral Veil Gown (₹75,000) | Seraphina French Lace Evening Gown | ₹28,000 | `western-wear` |
| `cb-2` | Valerie Classic Duchess Satin Bridal Gown (₹46,000) | Valerie Architectural Satin Gown | ₹18,500 | `western-wear` |
| `cb-3` | Celeste Pearl-Work Organza Bridal Saree (₹54,000) | Celeste Pearl-Embroidered Cape Dress | ₹21,000 | `western-wear` |
| `cb-4` | Evangeline Antique Gold Tissue Bridal Saree (₹49,000) | Evangeline Tailored Shimmer Blazer Set | ₹19,000 | `western-wear` |
| `eng-1` | Noor Blush Pink Organza Bridal Lehenga (₹58,000) | Noor Blush Pink Pleated Skirt Set | ₹22,500 | `occasion-wear` |
| `eng-2` | Aurelia Floral Organza Balcony Lehenga (₹59,000) | Aurelia Floral Organza Maxi Ensemble | ₹23,000 | `occasion-wear` |
| `eng-3` | Samira Fuchsia Zari Chevron Lehenga (₹68,000) | Samira Fuchsia Georgette Gown | ₹26,000 | `occasion-wear` |
| `eng-4` | Althea Royal Emerald Velvet Lehenga (₹64,000) | Althea Emerald Velvet Evening Robe | ₹25,000 | `occasion-wear` |
| `eng-5` | Sitara Heirloom Ivory Silk Lehenga (₹62,000) | Sitara Ivory Embellished Tunic Set | ₹24,000 | `occasion-wear` |
| `eng-6` | Veda Antique Gold Twirling Lehenga (₹49,500) | Veda Metallic Tiered Flare Dress | ₹19,500 | `occasion-wear` |
| `eng-7` | Elysian Champagne Reception Couture Set (₹72,000) | Elysian Champagne Couture Slip & Cape | ₹27,500 | `occasion-wear` |
| `wg-1` | Ophelia Beaded Tulle Fit-and-Flare Gown (₹62,000) | Ophelia Beaded Tulle Party Gown | ₹24,000 | `festive-collection` |
| `wg-2` | Giselle Beaded Cathedral Cape Bridal Gown (₹78,000) | Giselle Embroidered Festive Anarkali | ₹29,000 | `festive-collection` |
| `wg-3` | Rosalind Pearl Tassel Champagne Silhouette Gown (₹58,000) | Rosalind Pearl Fringe Cocktail Dress | ₹22,500 | `festive-collection` |
| `wg-4` | Adeline Emerald Jewel Collar Reception Gown (₹52,000) | Adeline Jewel-Collar Satin Evening Gown | ₹20,000 | `festive-collection` |
| `pp-1` | Avani Metallic Kasavu Pavithrappattu Saree (₹36,000) | Avani Organic Linen Tunic & Trousers | ₹14,000 | `casual-wear` |
| `pp-2` | Vrinda Emerald & Maroon Heritage Pavithrappattu (₹46,500) | Vrinda Pure Cotton Handloom Coord | ₹17,500 | `casual-wear` |
| `pp-3` | Tharavadu Heritage Kasavu Wedding Ensemble (₹42,000) | Tharavadu Relaxed Woven Silk Shirt | ₹16,000 | `casual-wear` |
| `pp-4` | Souparnika Handwoven Kerala Kasavu Drapes (₹34,000) | Souparnika Handwoven Everyday Dress | ₹13,500 | `casual-wear` |
| `rj-1` | Imperial Crimson Roja Scalloped Zardozi Saree (₹42,500) | Imperial Crimson Embroidered Kurta | ₹16,500 | `new-arrivals` |
| `rj-2` | Charulata Chartreuse & Plum Zari Festive Silk Saree (₹45,000) | Charulata Duo-Tone Silk Slip Dress | ₹17,500 | `new-arrivals` |
| `rj-3` | Gulzar Deep Red Velvet Embroidered Lehenga (₹65,000) | Gulzar Deep Garnet Tailored Pantsuit | ₹25,000 | `new-arrivals` |
| `hw-1` | Dahlia Intricate Cutwork & Pearl Blouse Set (₹32,000) | Dahlia Cutwork & Pearl Embroidered Top | ₹12,500 | `artisanal-craft` |
| `hw-2` | Marquise Bullion Wire Gold Zardozi Blouse Set (₹28,500) | Marquise Hand-Embroidered Silk Top | ₹11,000 | `artisanal-craft` |
| `hw-3` | Atelier Adda Handcrafted Zardozi Artistry (₹34,500) | Artisanal Wire-Embroidered Vest | ₹13,500 | `artisanal-craft` |
| `hw-4` | Joel Jacob Mathew Atelier Bespoke Sketch & Drape (Price on Request) | Made-to-Measure Atelier Silhouette | Price on Request | `artisanal-craft` |
| `lg-1` | M. Loft Royal Heritage Crimson Embroidered Set (₹72,000) | Signature Heritage Crimson Ensemble | ₹28,000 | `signature-series` |
| `lg-2` | M. Loft Rajkanya Purple Silk & Antique Gold Saree (₹38,500) | Signature Royal Plum Silk Kurta | ₹15,000 | `signature-series` |

### 4.2 Homepage Showcase Product Cards (`index.html`)
The 15 cards across the 3 tabs (`tab-new-arrivals`, `tab-best-sellers`, `tab-featured`) mapped cleanly:
1. `prod-na-1`: Aurelia Crimson Silk Kurta Set (`Ethnic Wear`, ₹18,500, New Arrival)
2. `prod-na-2`: Zahara Tailored Blazer Dress (`Western Wear`, ₹20,000, New Arrival)
3. `prod-na-3`: Celeste Handcrafted Linen Set (`Casual Wear`, ₹17,000, New Arrival)
4. `prod-na-4`: Marquise Hand-Embroidered Top (`Artisanal Craft`, ₹11,000, New Arrival)
5. `prod-na-5`: Elysian Pastel Evening Dress (`Occasion Wear`, ₹25,000, New Arrival)
6. `prod-bs-1`: Miraya Pure Silk Ensemble (`Ethnic Wear`, ₹18,000, Best Seller)
7. `prod-bs-2`: Seraphina French Lace Gown (`Western Wear`, ₹28,000, Best Seller)
8. `prod-bs-3`: Noor Blush Pink Pleated Set (`Occasion Wear`, ₹22,500, Best Seller)
9. `prod-bs-4`: Imperial Crimson Silk Kurta (`New Arrivals`, ₹16,500, Best Seller)
10. `prod-bs-5`: Ophelia Beaded Cocktail Gown (`Festive Collection`, ₹24,000, Best Seller)
11. `prod-ft-1`: Signature Royal Silk Dress (`Signature Series`, ₹22,000, Featured)
12. `prod-ft-2`: Avani Linen Tunic & Trousers (`Casual Wear`, ₹14,000, Featured)
13. `prod-ft-3`: Veda Metallic Flare Dress (`Occasion Wear`, ₹19,500, Featured)
14. `prod-ft-4`: Dahlia Cutwork Embroidered Top (`Artisanal Craft`, ₹12,500, Featured)
15. `prod-ft-5`: Valerie Architectural Satin Gown (`Western Wear`, ₹18,500, Featured)

---

## 5. Reels & Watch-and-Shop

### 5.1 Reel Files & Posters
| Current Video | Current Poster | Proposed Video | Proposed Poster | Proposed Title | Proposed Category | Proposed Price |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `assets/reels/reel_1.mp4` | `assets/images/reel-posters/reel-01.webp` | `assets/reels/reel-01.mp4` | `assets/images/reel-poster-01.webp` | Aurelia Silk Ensemble Reel | Ethnic Wear | ₹18,500 |
| `assets/reels/reel_2.mp4` | `assets/images/reel-posters/reel-02.webp` | `assets/reels/reel-02.mp4` | `assets/images/reel-poster-02.webp` | Celeste Satin Evening Gown | Western Wear | ₹25,000 |
| `assets/reels/reel_3.mp4` | `assets/images/reel-posters/reel-03.webp` | `assets/reels/reel-03.mp4` | `assets/images/reel-poster-03.webp` | Vrinda Handwoven Linen Set | Casual Wear | ₹16,000 |
| `assets/reels/reel_4.mp4` | `assets/images/reel-posters/reel-04.webp` | `assets/reels/reel-04.mp4` | `assets/images/reel-poster-04.webp` | Samira Fuchsia Maxi Dress | Occasion Wear | ₹26,000 |
| `assets/reels/reel_5.mp4` | `assets/images/reel-posters/reel-05.webp` | `assets/reels/reel-05.mp4` | `assets/images/reel-poster-05.webp` | Charulata Crimson Silk Drape | New Arrivals | ₹17,500 |
| `assets/reels/reel_6.mp4` | `assets/images/reel-posters/reel-06.webp` | `assets/reels/reel-06.mp4` | `assets/images/reel-poster-06.webp` | Giselle Pleated Party Gown | Festive Collection | ₹22,000 |
| `assets/reels/reel_7.mp4` | `assets/images/reel-posters/reel-07.webp` | `assets/reels/reel-07.mp4` | `assets/images/reel-poster-07.webp` | Artisanal Hand-Embroidered Vest| Artisanal Craft | ₹12,500 |

---

## 6. Image Inventory & Proposed `RENAME_MAP.csv`

Every single referenced image and video will follow the pattern `<section>-<NN>.webp` or `<role>.png`:

| Old Asset Path | Proposed New Path | Used In Pages |
| :--- | :--- | :--- |
| `assets/images/logo-badge.png` | `assets/images/logo-badge.png` | All 7 HTML pages |
| `assets/images/hero-01.webp` | `assets/images/hero-01.webp` | `index.html`, `js/products.js` |
| `assets/images/hero-02.webp` | `assets/images/hero-02.webp` | `index.html`, `js/products.js` |
| `assets/images/hero-03.webp` | `assets/images/hero-03.webp` | `index.html`, `js/products.js` |
| `assets/images/hero-04.webp` | `assets/images/hero-04.webp` | `index.html`, `js/products.js` |
| `assets/images/hero-05.webp` | `assets/images/hero-05.webp` | `index.html`, `js/products.js` |
| `assets/images/hindu-bride-01.webp` | `assets/images/collection-01.webp` | All 7 HTML pages, `js/products.js` |
| `assets/images/hindu-bride-02.webp` | `assets/images/product-01.webp` | `index.html`, `js/products.js` |
| `assets/images/hindu-bride-03.webp` | `assets/images/product-02.webp` | `index.html`, `js/products.js` |
| `assets/images/hindu-bride-04.webp` | `assets/images/product-03.webp` | `index.html`, `js/products.js` |
| `assets/images/christian-bride-01.webp`| `assets/images/collection-02.webp` | All 7 HTML pages, `js/products.js` |
| `assets/images/christian-bride-02.webp`| `assets/images/product-04.webp` | `index.html`, `js/products.js` |
| `assets/images/christian-bride-03.webp`| `assets/images/product-05.webp` | `about.html`, `index.html`, `js/products.js` |
| `assets/images/christian-bride-04.webp`| `assets/images/product-06.webp` | `index.html`, `js/products.js` |
| `assets/images/engagement-01.webp` | `assets/images/collection-03.webp` | All 7 HTML pages, `js/products.js` |
| `assets/images/engagement-02.webp` | `assets/images/product-07.webp` | `index.html`, `js/products.js` |
| `assets/images/engagement-03.webp` | `assets/images/product-08.webp` | `about.html`, `index.html`, `js/products.js` |
| `assets/images/engagement-04.webp` | `assets/images/product-09.webp` | `index.html`, `js/products.js` |
| `assets/images/engagement-05.webp` | `assets/images/product-10.webp` | `index.html`, `js/products.js` |
| `assets/images/white-gown-01.webp` | `assets/images/collection-04.webp` | All 7 HTML pages, `js/products.js` |
| `assets/images/white-gown-02.webp` | `assets/images/product-11.webp` | `index.html`, `js/products.js` |
| `assets/images/white-gown-03.webp` | `assets/images/product-12.webp` | `index.html`, `js/products.js` |
| `assets/images/pavithrappattu-01.webp` | `assets/images/collection-05.webp` | All 7 HTML pages, `js/products.js` |
| `assets/images/pavithrappattu-02.webp` | `assets/images/product-13.webp` | `index.html`, `js/products.js` |
| `assets/images/roja-01.webp` | `assets/images/collection-06.webp` | All 7 HTML pages, `js/products.js` |
| `assets/images/roja-02.webp` | `assets/images/product-14.webp` | `about.html`, `index.html`, `js/products.js` |
| `assets/images/handwork-01.webp` | `assets/images/collection-07.webp` | All 7 HTML pages, `js/products.js` |
| `assets/images/handwork-02.webp` | `assets/images/product-15.webp` | `about.html`, `index.html`, `js/products.js` |
| `assets/images/handwork-03.webp` | `assets/images/product-16.webp` | `about.html`, `index.html`, `js/products.js` |
| `assets/images/legacy-01.webp` | `assets/images/collection-08.webp` | All 7 HTML pages |
| `assets/images/legacy-02.webp` | `assets/images/product-17.webp` | `index.html`, `js/products.js` |
| `assets/images/best-seller-01.webp` | `assets/images/product-18.webp` | `index.html`, `js/products.js` |
| `assets/images/featured-01.webp` | `assets/images/product-19.webp` | `index.html`, `js/products.js` |
| `assets/images/featured-02.webp` | `assets/images/product-20.webp` | `index.html`, `js/products.js` |
| `assets/images/featured-03.webp` | `assets/images/product-21.webp` | `js/products.js` |
| `assets/images/new-arrival-01.webp` | `assets/images/product-22.webp` | `index.html`, `js/products.js` |
| `assets/images/new-launch-01.webp` | `assets/images/product-23.webp` | `index.html` |
| `assets/images/new-launch-02.webp` | `assets/images/product-24.webp` | `index.html` |
| `assets/images/mosaic-01.webp` | `assets/images/story-01.webp` | `about.html`, `index.html`, `js/products.js` |
| `assets/images/mosaic-02.webp` | `assets/images/story-02.webp` | `about.html`, `index.html`, `js/products.js` |
| `assets/images/mosaic-03.webp` | `assets/images/story-03.webp` | `about.html`, `js/products.js` |
| `assets/images/mosaic-04.webp` | `assets/images/story-04.webp` | `about.html`, `js/products.js` |
| `assets/images/instagram-01.webp` | `assets/images/social-01.webp` | `index.html`, `js/products.js` |
| `assets/images/instagram-03.webp` | `assets/images/social-02.webp` | `index.html`, `js/products.js` |
| `assets/images/reel-posters/reel-01.webp` | `assets/images/reel-poster-01.webp` | `index.html`, `reels.html` |
| `assets/images/reel-posters/reel-02.webp` | `assets/images/reel-poster-02.webp` | `index.html`, `reels.html` |
| `assets/images/reel-posters/reel-03.webp` | `assets/images/reel-poster-03.webp` | `index.html`, `reels.html` |
| `assets/images/reel-posters/reel-04.webp` | `assets/images/reel-poster-04.webp` | `index.html`, `reels.html` |
| `assets/images/reel-posters/reel-05.webp` | `assets/images/reel-poster-05.webp` | `index.html`, `reels.html` |
| `assets/images/reel-posters/reel-06.webp` | `assets/images/reel-poster-06.webp` | `index.html`, `reels.html` |
| `assets/images/reel-posters/reel-07.webp` | `assets/images/reel-poster-07.webp` | `index.html`, `reels.html` |
| `assets/reels/reel_1.mp4` | `assets/reels/reel-01.mp4` | `index.html`, `reels.html` |
| `assets/reels/reel_2.mp4` | `assets/reels/reel-02.mp4` | `index.html`, `reels.html` |
| `assets/reels/reel_3.mp4` | `assets/reels/reel-03.mp4` | `index.html`, `reels.html` |
| `assets/reels/reel_4.mp4` | `assets/reels/reel-04.mp4` | `index.html`, `reels.html` |
| `assets/reels/reel_5.mp4` | `assets/reels/reel-05.mp4` | `index.html`, `reels.html` |
| `assets/reels/reel_6.mp4` | `assets/reels/reel-06.mp4` | `index.html`, `reels.html` |
| `assets/reels/reel_7.mp4` | `assets/reels/reel-07.mp4` | `index.html`, `reels.html` |

---

## 7. Metadata, Page Titles, Alt Texts & JSON-LD

### 7.1 Page Titles & Meta Descriptions
Keep `<meta name="robots" content="noindex, nofollow">` on all pages. Update titles and descriptions:
* **`index.html`**:
  * Title: `Your Brand | Contemporary Fashion &amp; Apparel`
  * Meta Description: `Discover contemporary fashion, handcrafted ethnic wear, tailored western outfits, and artisanal collections at Your Brand.`
  * OG Title: `Your Brand | Contemporary Fashion &amp; Apparel`
  * OG Description: `Explore curated fashion collections, artisanal craftsmanship, and everyday luxury at Your Brand.`
* **`collections.html`**:
  * Title: `Collections | Your Brand`
  * Meta Description: `Explore our handcrafted clothing collections: Ethnic Wear, Western Wear, Occasion Wear, Festive Collection, and Casual Wear.`
* **`about.html`**:
  * Title: `About Our Brand &amp; Heritage | Your Brand`
  * Meta Description: `Discover the story, craftsmanship, design process, and textile heritage behind Your Brand.`
* **`contact.html`**:
  * Title: `Contact &amp; Store Location | Your Brand`
  * Meta Description: `Get in touch with Your Brand, visit our flagship store, or connect via WhatsApp for styling consultations.`
* **`reels.html`**:
  * Title: `Style Showcase &amp; Reels | Your Brand`
  * Meta Description: `Watch styling showcases, outfit movement videos, and client diaries from Your Brand.`
* **`product-detail.html`**:
  * Title: `Product Details | Your Brand`
  * Meta Description: `View fabric details, craftsmanship specifications, and enquire directly about this piece at Your Brand.`
* **`404.html`**:
  * Title: `404 - Page Not Found | Your Brand`
  * Meta Description: `The page you are looking for does not exist. Explore collections and new arrivals at Your Brand.`

### 7.2 JSON-LD Status
* Audit result: No `<script type="application/ld+json">` currently exists in any HTML files. None to modify or remove.

### 7.3 Alt Text
* Every `alt` tag mentioning `M LOFT`, `Joel Jacob Mathew`, `bridal`, `bride`, `saree`, `Kasavu`, `Kanchipuram`, `Kerala` will be replaced with clean apparel descriptive text (e.g., `alt="Your Brand Insignia"`, `alt="Classic Silk Kurta Set"`, `alt="Tailored Evening Gown"`, `alt="Craftsmanship in Our Atelier"`).

---

## 8. Specific Page Sections to Clean Up

1. **`index.html` Celebrations Section (`#celebrations`)**:
   - Current titles/captions reference bridal entries, weddings, muhurtham, and Changanassery.
   - Proposed: Rephrase to editorial lookbook captions (e.g. "Crimson Silk Ensemble — Editorial Look", "Ivory Tailored Silhouette — Evening Gala", etc.).
2. **`index.html` Photo Mosaic (`#mosaic`)**:
   - Current labels: "Our Brides", "Happiness", "Handcrafted", "Beauty of Bride".
   - Proposed: "Our Community", "Timeless Style", "Handcrafted", "Elegance in Motion".
3. **`index.html` Testimonials (`.testimonials-section`)**:
   - Currently: Bride testimonials with names & locations (e.g. "Anjali & Siddharth — Changanassery", "Dr. Maria & Roshan — Kottayam").
   - Proposed: Generic client testimonials ("Ananya S. — Verified Buyer", "Maria R. — Regular Client", "Sneha N. — Special Edition", "Reshma K. — Bespoke Client").
4. **`index.html` New Launch Banner (`#new-launch`)**:
   - Currently: "New Launch Alert: The M. Loft Legacy Collection"
   - Proposed: "New Launch Alert: The Signature Line Capsule"
5. **`index.html` Trust Strip (`.trust-strip`)**:
   - Currently references "Bridal Craftsmanship", "Atelier in Changanassery".
   - Proposed: "Artisanal Craftsmanship", "Flagship Store & Global Shipping".
6. **`about.html` Story & Process**:
   - Remove Joel Jacob Mathew narrative; describe brand design ethos, master tailors, handpicked natural textiles, 4-step consultation process.
7. **`contact.html` Consultation Form**:
   - "Book a Bridal Consultation" -> "Book a Personal Styling Consultation".
   - Event type dropdown options: Wedding, Reception, Sangeet, Festive, Formal -> Evening Gala, Festive Celebration, Cocktail & Formal, Casual Styling, Other.

---

## 9. Implementation Phases & Workflow

Following approval of this plan:
* **Phase 1**: Replace all brand, owner, contact, text, categories, products, descriptions, titles, meta tags, and alt texts across all 7 HTML pages, `js/products.js`, `js/main.js`, and `css/style.css`.
* **Phase 2**: Rename all media references to `<section>-<NN>.webp`, generate and save `RENAME_MAP.csv`.
* **Phase 3**: Generate neutral placeholder `.webp` images at accurate aspect ratios via Python + Pillow; generate short silent MP4 placeholders via ffmpeg (or graceful video degradation); write `assets/IMAGE_GUIDE.md`.
* **Phase 4**: Automated sweep for forbidden keywords across all files; browser verification of all 7 pages (desktop + 375px mobile); bump CSS/JS cache buster (`?v=7.0`).
