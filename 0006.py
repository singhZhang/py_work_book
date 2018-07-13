'''
你有一个目录，放了你一个月的日记，都是 txt，
为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词

查找目录下所有的txt文件（或者是统一命名规则的文件），
并统计文件中出现频率最多的英文单词
'''

import os
import re


def get_all_files( path ):
    '''
    获取目录下的日记，日记的命名格式为 diary-xxx.txt
    :param path:
    :return:
    '''

    files_list = []

    for root, dirs, files in os.walk(path):

        for file in files:

            if file.lower().startswith('diary-') and file.lower().endswith('txt'):

                files_list.append(os.path.join(root, file))

    return files_list


def get_max_word( file_path ):
    '''
    获取文件中出现的每个单词的数量
    :param file_path:
    :return:
    '''

    keywords = {}

    file_name = os.path.basename(file_path)

    with open(file_path, encoding='utf-8') as f:

        text = f.read()

        word_list = re.findall(r'[a-zA-Z]+', text.lower())

        for word in word_list:

            if word in keywords:

                keywords[word] += 1

            else:

                keywords[word] = 1

        keywords_sorted = sorted(keywords.items(), key=lambda x: x[1], reverse=True)

        return file_name, keywords_sorted[0]



if __name__ == '__main__':

    files_list = get_all_files(os.getcwd())

    if len(files_list):

        for file_item in files_list:

            file_name, find_word = get_max_word(file_item)

            print("日记文件：{0} 中出现最多的单词是 {1},出现的次数是 {2}".format(file_name, find_word[0], find_word[1]))