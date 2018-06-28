'''
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小

从一个目录中取出里面的图片，并修改图片的尺寸后重新保存

代码粗糙，有待优化
'''

import os
from PIL import Image

IPHONE5_WIDTH = 640
IPHONE5_HEIGHT = 1136


def reset_pic_size(file_path, file_new_path, width = IPHONE5_WIDTH, height = IPHONE5_HEIGHT):

    image = Image.open(file_path)
    image_width, image_height = image.size

    # if image_width > width:
    #     image_height = width * image_height // image_width
    #     image_width = width
    # if image_height > height:
    #     image_width = height * image_width // image_height
    #     image_height = height

    new_image = image.resize((width, height), Image.ANTIALIAS)
    new_image.save(file_new_path)


def get_all_img( path ):
    for root, dirs, files in os.walk(path):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files) #当前路径下所有非目录子文件

        for file in files:

            if file.lower().endswith('jpg') or file.lower().endswith('png') or file.lower().endswith('jpeg'):

                file_path = os.path.join(root, file)

                file_new_path = 'iphone5_' + file

                reset_pic_size(file_path, file_new_path)




if __name__ == '__main__':

    path = 'E:\\file\\workbook\\img'

    get_all_img( path )