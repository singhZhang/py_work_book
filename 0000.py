'''
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果
'''

from PIL import Image,ImageDraw,ImageFont
font = ImageFont.truetype('simsun.ttc',24) #设置字体及其大小 不同字体可在c:\windows\font中找到
im01 = Image.open("123123.jpg")  #路径不能包含中文，要打双斜线
draw = ImageDraw.Draw(im01)
draw.text((100,6),'4', fill=(255,0,0),font=font)
#draw.text((10,6),u'晚上', fill=(255,0,0),font=font)
#draw.text((50,6),unicode('白天','utf-8'), fill=(255,0,0),font=font)
im01.show()