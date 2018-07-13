'''
读取 xls 文件内容，并写到 xml 文件中
'''

import xlrd
import xml.dom.minidom as md

workbook = xlrd.open_workbook('student.xls')

worksheets = workbook.sheet_names()

worksheet = workbook.sheet_by_name('test')

content = {}

for i in range(worksheet.nrows):

    print(worksheet.row_values(i))

    content[i+1] = worksheet.row_values(i)[1:]

xmlfile = md.Document()

root = xmlfile.createElement('root')

students = xmlfile.createElement('student')

xmlfile.appendChild(root)

root.appendChild(students)

comment = xmlfile.createComment('学生信息表 "id" : [名字， 数学， 语文，英语]')

students.appendChild(comment)

xmlcontent = xmlfile.createTextNode(str(content))

students.appendChild(xmlcontent)

with open('student.xml', 'wb') as f:

    f.write(xmlfile.toprettyxml(encoding='UTF-8'))

print("SUC")















