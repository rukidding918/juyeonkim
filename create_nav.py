import os
from bs4 import BeautifulSoup

target = 'index.html'

with open(target, "rt", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")
ul = soup.find("ul", {"class": "uk-nav-sub"})

# 기존 메뉴 삭제
for old_li in ul.find_all('li'):
    old_li.decompose()

# menu 구성하는 거 만들자. ul 밑에 li 지우고 img 폴더명으로 li 만든 뒤
# li 아래 a href='detail' 넣고 저장.

img_dir = 'images/'
img_dir_tree = [(root, dirs) for root, dirs, _ in os.walk(img_dir)]

menus = img_dir_tree[0][1]

for item in menus:
    new_li = soup.new_tag("li")
    title = item.replace(' ', '_')
    new_a = soup.new_tag('a', href=f"{item}.html")
    new_a.string = item
    ul.insert(1, new_li)
    new_li.insert(1, new_a)  
    # insert(x번째, new_tag) # insert_after(new_tag)도 있음.

with open(target, "wt", encoding="utf-8") as file:
    file.write(str(soup))
