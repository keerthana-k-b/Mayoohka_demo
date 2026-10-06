import subprocess
import json

script = """
const header = document.querySelector('.site-header');
const headerInner = document.querySelector('.header-inner');
const toggle = document.querySelector('.mobile-toggle');
const brandLink = document.querySelector('.brand-link');
const brandImg = document.querySelector('.brand-logo-img');
const brandWrap = document.querySelector('.brand-text-wrap');
const brandMain = document.querySelector('.brand-main-text');
const brandSub = document.querySelector('.brand-sub-text');
const actions = document.querySelector('.header-actions');

console.log(JSON.stringify({
  windowWidth: window.innerWidth,
  headerWidth: header.offsetWidth,
  headerInnerWidth: headerInner.offsetWidth,
  toggleRect: toggle ? toggle.getBoundingClientRect() : null,
  brandLinkRect: brandLink ? brandLink.getBoundingClientRect() : null,
  brandImgRect: brandImg ? brandImg.getBoundingClientRect() : null,
  brandMainRect: brandMain ? brandMain.getBoundingClientRect() : null,
  brandSubDisplay: brandSub ? window.getComputedStyle(brandSub).display : null,
  actionsRect: actions ? actions.getBoundingClientRect() : null,
  actionsDisplay: actions ? window.getComputedStyle(actions).display : null,
  actionsChildren: actions ? Array.from(actions.children).map(c => ({
    tag: c.tagName,
    cls: c.className,
    display: window.getComputedStyle(c).display,
    rect: c.getBoundingClientRect()
  })) : []
}, null, 2));
"""

# Test with node/puppeteer or Chrome evaluate
with open('scratch/eval_header.js', 'w', encoding='utf-8') as f:
    f.write(script)

print("Saved eval_header.js")
