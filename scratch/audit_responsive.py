import re

with open('D:/Mayoohka_demo/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's find any width or min-width > 360px without max-width: 100%
matches = re.findall(r'([^{}]+)\{([^{}]+)\}', css)
print(f"Total CSS rule blocks: {len(matches)}")

suspicious = []
for selector, block in matches:
    # check if selector is in a @media query or not
    # look for width: \d+px or min-width: \d+px
    w_matches = re.findall(r'(?:^|;|\s)(?:min-)?width:\s*(\d+)px', block)
    for w in w_matches:
        val = int(w)
        if val > 360:
            # check if block has max-width: 100% or similar
            if 'max-width: 100%' not in block and 'max-width: min(' not in block:
                # also check if selector is something obviously large like containers or desktop only
                suspicious.append((selector.strip().replace('\n', ' '), val, block.strip().replace('\n', ' ')[:100]))

print(f"\nSuspicious rules with fixed width > 360px (found {len(suspicious)}):")
for sel, w, blk in suspicious[:25]:
    # Filter out desktop media queries or container widths
    print(f"  [{w}px] {sel[:60]} -> {blk[:60]}")
