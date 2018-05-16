#-*- coding:utf-8 -*-
from PIL import Image

img = "test.png"
height = 50
width = 100
output = "test2.txt"
chars = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

length = len(chars)


def get_char(r,g,b,alpha = 256):

    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0+1)/length

    return chars[int (gray/unit)]




if __name__ == '__main__' :

    txt = ""
    im = Image.open(img)
    im = im.resize((width,height),Image.NEAREST)
    for i in range(height):
        for j in range(width):
            txt += get_char(*im.getpixel((j,i)))
        txt += "\n"

    print txt

    if output:
        with open(output,'w') as f:
            f.write(txt)

    else:
        with open("output.txt","w") as f:
            f.write(txt)


