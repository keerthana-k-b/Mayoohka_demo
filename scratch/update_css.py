with open('css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('Your Brand — Master Luxury Design System', 'MAYOOKHA – The Bridal Studio — Master Luxury Design System')
text = text.replace('/* Centered logo badge with "Your Brand" wordmark */', '/* Centered logo badge with "MAYOOKHA" wordmark */')
# Also check if any other "Your Brand" or "yourbrand"
text = text.replace('Your Brand', 'MAYOOKHA')
text = text.replace('yourbrand', 'mayoohka_by_aiswarya_')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated css/style.css successfully')
