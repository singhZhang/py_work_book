'''
生成字母验证码
'''
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def rndBackground():

    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndFrontColor():

    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def rndChar():

    return chr(random.randint(65, 90))



if __name__ == '__main__':

    width = 240
    height = 60

    image = Image.new('RGB', (width, height), (255,255,255))

    font = ImageFont.truetype('simsun.ttc', 36)

    draw = ImageDraw.Draw(image)

    for x in range(width):
        for y in range(height):
            draw.point((x,y), fill=rndBackground())

    for t in range(4):
        draw.text((60 * t + 10, 10), rndChar(), font = font, fill = rndFrontColor())

    image = image.filter(ImageFilter.BLUR)

    image.save('vcode.jpg')