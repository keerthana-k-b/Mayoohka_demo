import os

images = sorted(os.listdir('assets/images'))
print('Total images:', len(images))
collections = [i for i in images if i.startswith('collection')]
heroes = [i for i in images if i.startswith('hero')]
products = [i for i in images if i.startswith('product')]
stories = [i for i in images if i.startswith('story')]
socials = [i for i in images if i.startswith('social')]
reels = [i for i in images if i.startswith('reel')]
print('Collections:', collections)
print('Heroes:', heroes)
print('Products count:', len(products))
print('Stories:', stories)
print('Socials:', socials)
print('Reel posters:', reels)
