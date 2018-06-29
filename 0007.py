'''
统计一下你写过多少行代码。包括空行和注释，但是要分别列出来

python 代码中的注释块怎么获取没有想到更好的办法，有待优化
'''

import os
import re

code_lines = 0
empty_lines = 0
notes_lines = 0

file_path = "E:\\file\\workbook\\example.py"

is_notes = 0

with open(file_path, encoding='UTF-8') as f:

    for line in f.readlines():

        if not len(line) or re.match(r'\s+$', line):

            empty_lines += 1
        elif line.startswith('#'):

            notes_lines += 1
        elif line.startswith("'''") and is_notes == 0:

            notes_lines += 1

            is_notes = 1
        elif line.startswith("'''") and is_notes != 0:

            notes_lines += 1

            is_notes = 0
        elif is_notes != 0:

            notes_lines += 1

        else:

            code_lines += 1

    print("文件是：{0}".format(os.path.basename(file_path)))

    print("代码行数是：{0}".format(code_lines))
    print("注释行数是：{0}".format(notes_lines))
    print("空白行数是：{0}".format(empty_lines))






