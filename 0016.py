
'''
读取 txt 里面的内容存储到xls
'''

import json
from collections import OrderedDict
import xlwt

with open('numbers.txt', 'rb') as f:
    content = f.read()

content = content.decode("UTF-8")

d = json.loads(content, object_pairs_hook=OrderedDict)

file = xlwt.Workbook()

table = file.add_sheet('number')

for row, i in enumerate(list(d)):

    for col, j in enumerate(d[row]):

        table.write(row, col, j)

file.save('number.xls')