import os
from pathlib import Path
from PIL import Image


image_paths = []
for root, _, files in os.walk('images'):
    if files:
        for file in files:
            image_paths.append(os.path.join(root, file).replace('\\', '/'))
print(image_paths)

save_path = ['./thumbnail/'+i_path.split('/', 1)[-1] for i_path in image_paths]
print(save_path)


for num, image_name in enumerate(image_paths):
    with Image.open(image_name) as img:
        max_size = (100, 100)
        img.thumbnail(max_size)
        img.save(save_path[num])