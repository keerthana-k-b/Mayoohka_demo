with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(850, 1900):
    if i < len(lines):
        line = lines[i]
        if any(w in line for w in ['<section', 'id="', 'class="section-title', 'class="story-', 'class="new-launch', 'class="testimonial', 'class="reel-']):
            print(f'{i+1}: {line.strip()[:100]}')
