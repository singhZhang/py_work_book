'''
替换用户输入的字符串中的敏感词
'''

def getKeywords():

    with open('filtered_words.txt', encoding='UTF-8') as f:

        fread = f.readlines()

        keywords = []

        for w in fread:
            w = w.strip('\n')

            keywords.append(w)

    return keywords


if __name__ == '__main__':

    keywords = getKeywords()

    str_input = input("请输入一句话：")

    print(str_input)

    for fw in keywords:

        if fw in str_input:

            fw_len = len(fw)

            str_input = str_input.replace(fw, '*'*fw_len)

    print(str_input)
