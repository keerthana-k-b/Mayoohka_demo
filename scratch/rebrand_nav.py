import re

DROPDOWN_GRID = """            <div class="dropdown-grid">
              <a href="collections.html?c=sarees" class="dropdown-card">
                <img src="assets/images/collection-01.webp" alt="Sarees" class="dropdown-thumb" width="64" height="64" loading="lazy">
                <div class="dropdown-card-text">
                  <div class="dropdown-title">Sarees</div>
                  <div class="dropdown-desc">Kasavu, tissue, organza &amp; celebration drapes</div>
                </div>
              </a>

              <a href="collections.html?c=bridal-sarees" class="dropdown-card">
                <img src="assets/images/collection-02.webp" alt="Bridal Sarees" class="dropdown-thumb" width="64" height="64" loading="lazy">
                <div class="dropdown-card-text">
                  <div class="dropdown-title">Bridal Sarees</div>
                  <div class="dropdown-desc">Pure Kanchipuram silks &amp; Muhurtham weaves</div>
                </div>
              </a>

              <a href="collections.html?c=lehengas" class="dropdown-card">
                <img src="assets/images/collection-03.webp" alt="Lehengas" class="dropdown-thumb" width="64" height="64" loading="lazy">
                <div class="dropdown-card-text">
                  <div class="dropdown-title">Lehengas</div>
                  <div class="dropdown-desc">Bridal lehengas, dhavani sets &amp; half-sarees</div>
                </div>
              </a>

              <a href="collections.html?c=bridal-blouses" class="dropdown-card">
                <img src="assets/images/collection-04.webp" alt="Bridal Blouses" class="dropdown-thumb" width="64" height="64" loading="lazy">
                <div class="dropdown-card-text">
                  <div class="dropdown-title">Bridal Blouses</div>
                  <div class="dropdown-desc">Zardozi, aari, maggam &amp; designer back work</div>
                </div>
              </a>

              <a href="collections.html?c=custom-dresses" class="dropdown-card">
                <img src="assets/images/collection-05.webp" alt="Custom Dresses" class="dropdown-thumb" width="64" height="64" loading="lazy">
                <div class="dropdown-card-text">
                  <div class="dropdown-title">Custom Dresses</div>
                  <div class="dropdown-desc">Bespoke bridal gowns &amp; evening couture</div>
                </div>
              </a>

              <a href="collections.html?c=ready-mades" class="dropdown-card">
                <img src="assets/images/collection-06.webp" alt="Ready-mades" class="dropdown-thumb" width="64" height="64" loading="lazy">
                <div class="dropdown-card-text">
                  <div class="dropdown-title">Ready-mades</div>
                  <div class="dropdown-desc">Designer kurtas &amp; festive coordinates</div>
                </div>
              </a>

              <a href="collections.html?c=kids-wear" class="dropdown-card">
                <img src="assets/images/collection-07.webp" alt="Kids Wear" class="dropdown-thumb" width="64" height="64" loading="lazy">
                <div class="dropdown-card-text">
                  <div class="dropdown-title">Kids Wear</div>
                  <div class="dropdown-desc">Pattu pavadai &amp; custom kids ethnic wear</div>
                </div>
              </a>

              <a href="collections.html?c=gents-wear" class="dropdown-card">
                <img src="assets/images/collection-08.webp" alt="Gents Wear" class="dropdown-thumb" width="64" height="64" loading="lazy">
                <div class="dropdown-card-text">
                  <div class="dropdown-title">Gents Wear</div>
                  <div class="dropdown-desc">Kasavu mundu sets, silk kurtas &amp; groomswear</div>
                </div>
              </a>
            </div>"""

DRAWER_CONTENT = """        <div class="drawer-accordion-content">
          <a href="collections.html?c=sarees" class="drawer-sublink-card">
            <img src="assets/images/collection-01.webp" alt="Sarees" class="drawer-sublink-thumb" width="40" height="40" loading="lazy">
            <span class="drawer-sublink-name">Sarees</span>
          </a>
          <a href="collections.html?c=bridal-sarees" class="drawer-sublink-card">
            <img src="assets/images/collection-02.webp" alt="Bridal Sarees" class="drawer-sublink-thumb" width="40" height="40" loading="lazy">
            <span class="drawer-sublink-name">Bridal Sarees</span>
          </a>
          <a href="collections.html?c=lehengas" class="drawer-sublink-card">
            <img src="assets/images/collection-03.webp" alt="Lehengas" class="drawer-sublink-thumb" width="40" height="40" loading="lazy">
            <span class="drawer-sublink-name">Lehengas</span>
          </a>
          <a href="collections.html?c=bridal-blouses" class="drawer-sublink-card">
            <img src="assets/images/collection-04.webp" alt="Bridal Blouses" class="drawer-sublink-thumb" width="40" height="40" loading="lazy">
            <span class="drawer-sublink-name">Bridal Blouses</span>
          </a>
          <a href="collections.html?c=custom-dresses" class="drawer-sublink-card">
            <img src="assets/images/collection-05.webp" alt="Custom Dresses" class="drawer-sublink-thumb" width="40" height="40" loading="lazy">
            <span class="drawer-sublink-name">Custom Dresses</span>
          </a>
          <a href="collections.html?c=ready-mades" class="drawer-sublink-card">
            <img src="assets/images/collection-06.webp" alt="Ready-mades" class="drawer-sublink-thumb" width="40" height="40" loading="lazy">
            <span class="drawer-sublink-name">Ready-mades</span>
          </a>
          <a href="collections.html?c=kids-wear" class="drawer-sublink-card">
            <img src="assets/images/collection-07.webp" alt="Kids Wear" class="drawer-sublink-thumb" width="40" height="40" loading="lazy">
            <span class="drawer-sublink-name">Kids Wear</span>
          </a>
          <a href="collections.html?c=gents-wear" class="drawer-sublink-card">
            <img src="assets/images/collection-08.webp" alt="Gents Wear" class="drawer-sublink-thumb" width="40" height="40" loading="lazy">
            <span class="drawer-sublink-name">Gents Wear</span>
          </a>
          <a href="collections.html" class="drawer-sublink-all">
            View all collections &rarr;
          </a>
        </div>"""

FOOTER_COLLECTIONS = """          <ul class="footer-links">
            <li><a href="collections.html?c=sarees">Sarees</a></li>
            <li><a href="collections.html?c=bridal-sarees">Bridal Sarees</a></li>
            <li><a href="collections.html?c=lehengas">Lehengas</a></li>
            <li><a href="collections.html?c=bridal-blouses">Bridal Blouses</a></li>
            <li><a href="collections.html?c=custom-dresses">Custom Dresses</a></li>
            <li><a href="collections.html?c=ready-mades">Ready-mades</a></li>
            <li><a href="collections.html?c=kids-wear">Kids Wear</a></li>
            <li><a href="collections.html?c=gents-wear">Gents Wear</a></li>
          </ul>"""

def apply_nav_and_footer(html):
    # Replace dropdown grid
    html = re.sub(
        r'<div class="dropdown-grid">.*?</div>\s*<div class="dropdown-footer">',
        DROPDOWN_GRID + '\n            <div class="dropdown-footer">',
        html,
        flags=re.DOTALL
    )

    # Replace drawer accordion content
    html = re.sub(
        r'<div class="drawer-accordion-content">.*?</div>\s*</div>\s*<div class="drawer-nav-item">\s*<a href="reels.html"',
        DRAWER_CONTENT + '\n      </div>\n\n      <div class="drawer-nav-item">\n        <a href="reels.html"',
        html,
        flags=re.DOTALL
    )

    # Replace footer links for collections
    html = re.sub(
        r'<h3 class="footer-col-title">Collections</h3>\s*<ul class="footer-links">.*?</ul>',
        '<h3 class="footer-col-title">Collections</h3>\n' + FOOTER_COLLECTIONS,
        html,
        flags=re.DOTALL
    )

    return html
