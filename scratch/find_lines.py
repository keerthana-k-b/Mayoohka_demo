with open('index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if 'collections-grid' in line:
            print(f'collections-grid line: {i}')
        if 'id="collections"' in line:
            print(f'id="collections" line: {i}')
        if 'id="products"' in line:
            print(f'id="products" line: {i}')
        if 'id="mosaic"' in line:
            print(f'id="mosaic" line: {i}')
        if 'id="reels"' in line:
            print(f'id="reels" line: {i}')
