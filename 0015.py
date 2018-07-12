'''
纯文本文件 city.txt为城市信息.写到 city.xls 文件中
'''

import json
from collections import OrderedDict
import xlwt

with open('city.txt', 'rb') as f:
    content = f.read()

content = content.decode("UTF-8")

d = json.loads(content, object_pairs_hook=OrderedDict)

file = xlwt.Workbook()

table = file.add_sheet('city')

for row, i in enumerate(list(d)):

    table.write(row, 0, i)

    table.write(row, 1, d[i])

file.save('city.xls')