'''
把 txt 文本里面的内容读取出来存储到 xls 表格中去
'''
import json
from collections import OrderedDict
import xlwt

with open('student.txt', 'rb') as f:
    content = f.read()

content = content.decode("UTF-8")

d = json.loads(content, object_pairs_hook=OrderedDict)

file = xlwt.Workbook()

table = file.add_sheet('test')

for row, i in enumerate(list(d)):

    table.write(row, 0, i)

    for col, j in enumerate(d[i]):

        table.write(row, col+1, j)

file.save('student.xls')