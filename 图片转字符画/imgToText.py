#-*- coding: utf-8 -*-
from PIL import Image


IMG = "test.png"
WIDTH = 100
HEIGHT = 50
OUTPUT = "test.txt"

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    #灰度值公式
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    #存放所有字符的变量
    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            #  *im.getpixel(j,i)  会返回一个元组 这个元组有三个元素对应的正好是颜色的RGB
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print txt

    #字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)