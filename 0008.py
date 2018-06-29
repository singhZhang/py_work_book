'''
一个HTML文件，找出里面的正文

同时找出页面上所有的链接
'''


import requests
from bs4 import BeautifulSoup

url = "http://www.laruence.com/2011/12/30/2435.html"

html = requests.get(url)

soup = BeautifulSoup(html.text, "html.parser")

# 获取页面正文

print(soup.body.text.encode('GBK','ignore').decode('GBK'))

# 查找所有的 链接

for item in soup.find_all('a'):

    print(item.get('href'))


