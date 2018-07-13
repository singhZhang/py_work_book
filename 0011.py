'''
判断用户输入的词语是否存在敏感词
'''


with open('filtered_words.txt', encoding='UTF-8') as f:

    fread = f.readlines()

    keywords = []

    for w in fread:

        w = w.strip('\n')

        keywords.append(w)

word = input("请输入：")

if word in keywords:

    print('Freedom')

else:

    print('Human Rights')

