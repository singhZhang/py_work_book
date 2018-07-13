'''
抓取页面中的图片
'''

import requests
from bs4 import BeautifulSoup as bs
import os, random


url = "http://tieba.baidu.com/p/2166231880"

r = requests.get(url)

text = r.text

soup = bs(text, "html.parser")

a = soup.find_all('img', {'class','BDE_Image'})

imgPath = "E:\\file\\workbook\\img\\baidu"

if not os.path.exists(imgPath):
    os.makedirs(imgPath)

for i in a:
    with open(imgPath + "\\" + str(random.random()) + ".jpg", 'wb') as f:
        html = requests.get(i['src'])
        f.write(html.content)