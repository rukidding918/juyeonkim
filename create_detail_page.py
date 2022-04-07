import os
from re import A
from bs4 import BeautifulSoup

base_html = 'index.html'

with open(base_html, "rt", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

# html 파일 제목 만들기
img_dir = 'images/'
img_dir_tree = [(root, dirs) for root, dirs, _ in os.walk(img_dir)]

menus = img_dir_tree[0][1]

# 파일별로 구성하기
for item in menus:
    #head 태그 안에 detail.css 삽입
    head = soup.find('head')
    new_link = soup.new_tag('link', attrs={'rel': 'stylesheet', 'href': 'detail.css'})
    head.append(new_link)

    main_div = soup.find("div", {"class": "main-screen"})

    # 기존 내용 삭제
    for old_div in main_div.find_all('div'):
        old_div.decompose()

    # 제목 넣기
    new_h3 = soup.new_tag("div", attrs={'class':"uk-h3"})
    new_h3.string = item
    main_div.insert(1, new_h3)

    # 라이트박스 넣기
    lightbox_div = soup.new_tag('div', attrs={'class': "uk-child-width-1-4 uk-child-width-1-6@m", 'uk-grid': "", 'uk-lightbox': "animation: slide"})
    main_div.append(lightbox_div)


    root_dir = os.path.join('images', item)

    image_paths = []
    for root, dirs, files in os.walk(root_dir):
        if files:
            for file in files:
                image_paths.append(os.path.join(root, file).replace("\\", "/"))

    thumbnail_paths = [f"thumbnails/{item}/" + i_path.split("/", 2)[-1] for i_path in image_paths]

    for img_path, thumb_path in zip(image_paths, thumbnail_paths):
        new_div = soup.new_tag('div')
        lightbox_div.append(new_div)
        caption = img_path.split('/')[2].replace('.jpg', '').replace(' - ', ', ')
        new_a = soup.new_tag('a', attrs={'class': 'uk-inline', 'href': img_path, 'data-caption': caption})
        new_img = soup.new_tag('img', attrs={'src': thumb_path, 'alt': caption})

        new_a.append(new_img)
        new_div.append(new_a)

    with open(f'{item}.html', "wt", encoding="utf-8") as file:
        file.write(str(soup))
