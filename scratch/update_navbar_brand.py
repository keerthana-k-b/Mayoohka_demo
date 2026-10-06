import os
import re

# 1. Update css/style.css
css_path = 'd:/Mayoohka_demo/css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Remove .brand-link .brand-text-wrap { display: none !important; }
css = re.sub(r'\.brand-link\s+\.brand-text-wrap\s*\{\s*display:\s*none\s*!important;\s*\}', '', css)

# Update .brand-logo-img base rules
old_logo_rule = """.brand-logo-img {
  height: 48px;
  width: auto;
  max-width: 160px;
  object-fit: contain;
  display: block;
  transition: transform var(--transition-smooth);
}

.site-header.scrolled .brand-logo-img {
  height: 40px;
  transform: scale(0.95);
}"""

new_logo_rule = """.brand-logo-img {
  height: 44px;
  width: auto;
  max-width: 48px;
  object-fit: contain;
  display: block;
  flex-shrink: 0;
  transition: transform var(--transition-smooth);
}

.site-header.scrolled .brand-logo-img {
  height: 38px;
  transform: scale(0.95);
}"""

if old_logo_rule in css:
    css = css.replace(old_logo_rule, new_logo_rule)
else:
    print("Warning: old_logo_rule exact match not found, checking with regex")
    css = re.sub(
        r'\.brand-logo-img\s*\{[^}]*\}',
        """.brand-logo-img {
  height: 44px;
  width: auto;
  max-width: 48px;
  object-fit: contain;
  display: block;
  flex-shrink: 0;
  transition: transform var(--transition-smooth);
}""",
        css,
        count=1
    )

# Ensure mobile styles under max-width: 767px allow brand-text-wrap and handle <= 480px
# Let's check mobile brand-link in CSS:
# In @media (max-width: 767px):
# Replace brand-sub-text { display: none; } with display for 481-767px and media query for <= 480px
mobile_brand_target = """  .brand-main-text {
    font-size: clamp(1rem, 3.8vw, 1.3rem);
    letter-spacing: 1px;
    line-height: 1;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .brand-sub-text {
    display: none;
  }"""

mobile_brand_replacement = """  .brand-logo-img {
    height: 40px;
    width: auto;
    max-width: 44px;
  }

  .brand-text-wrap {
    display: flex;
    flex-direction: column;
    min-width: 0;
    overflow: hidden;
  }

  .brand-main-text {
    font-size: clamp(1rem, 3.8vw, 1.25rem);
    letter-spacing: 1.5px;
    line-height: 1;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .brand-sub-text {
    font-family: var(--font-sans);
    font-size: 0.52rem;
    font-weight: 600;
    letter-spacing: 1.6px;
    text-transform: uppercase;
    color: var(--accent-gold);
    margin-top: 2px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  /* On mobile <=480px, keep logo and show only MAYOOKHA if space is tight */
  @media (max-width: 480px) {
    .brand-link {
      gap: 7px;
      max-width: calc(100% - 110px);
    }
    .brand-logo-img {
      height: 38px;
    }
    .brand-sub-text {
      display: none !important;
    }
    .brand-main-text {
      font-size: 1.1rem;
      letter-spacing: 1.2px;
    }
  }"""

if mobile_brand_target in css:
    css = css.replace(mobile_brand_target, mobile_brand_replacement)
    print("Replaced mobile brand styles successfully")
else:
    print("Warning: mobile_brand_target not matched exactly, searching lines")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("css/style.css updated successfully")

# 2. Update all 7 HTML pages
pages = ['index.html', 'collections.html', 'about.html', 'contact.html', 'reels.html', 'product-detail.html', '404.html']
for p in pages:
    fpath = os.path.join('d:/Mayoohka_demo', p)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update width/height on logo-header.png and text in brand-sub-text
    old_pattern = r'<img src="assets/images/logo-header\.png"[^>]*>'
    new_img = '<img src="assets/images/logo-header.png" alt="MAYOOKHA – The Bridal Studio" class="brand-logo-img" width="46" height="44" decoding="async">'
    html = re.sub(old_pattern, new_img, html)

    # Sub-text uppercase
    html = re.sub(
        r'<span class="brand-sub-text">\s*The Bridal Studio\s*</span>',
        '<span class="brand-sub-text">THE BRIDAL STUDIO</span>',
        html,
        flags=re.IGNORECASE
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated navbar in {p}")
