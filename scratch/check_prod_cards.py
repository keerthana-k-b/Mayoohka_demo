with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
prod_names = re.findall(r'data-name="([^"]+)"', text)
print('Found product data-names in index.html:', len(prod_names))
for i, name in enumerate(prod_names, 1):
    print(f'{i}: {name}')
