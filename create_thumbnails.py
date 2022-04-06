import os
from PIL import Image


img_dir = 'images/'
img_dir_tree = [(root, dirs) for root, dirs, _ in os.walk(img_dir)]
menus = img_dir_tree[0][1]

if not os.path.isdir('thumbnails'):
    os.mkdir('thumbnails')

for item in menus:
    if not os.path.isdir(f'thumbnails/{item}'):
        os.mkdir(f'thumbnails/{item}')


image_paths = []
for root, _, files in os.walk("images"):
    if files:
        for file in files:
            image_paths.append(os.path.join(root, file).replace("\\", "/"))

thumbnail_path = ["thumbnails/" + i_path.split("/", 1)[-1] for i_path in image_paths]

for pair in zip(image_paths, thumbnail_path):
    print(pair)

for num, image_name in enumerate(image_paths):
    with Image.open(image_name) as img:
        max_size = (100, 100)
        img.thumbnail(max_size)
        img.save(thumbnail_path[num])
