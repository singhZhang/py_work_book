'''

统计文章单词的方法有很多种，

本次执行是按照空格格式化成list后，计算list长度的方法

这种方法是讲 I'm 此类的算作是一个单词

'''

if __name__ == '__main__':

    with open('en.txt') as file:

        str = file.read().split(' ')

    print(str)

    print(len(str))
