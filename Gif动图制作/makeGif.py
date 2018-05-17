# -*-coding:utf-8 -*-
from PIL import Image

im = Image.open("images/1.jpg")
images = []

images.append(Image.open("images/2.jpg"))
images.append(Image.open("images/3.jpg"))
# loop循环次数，druation每张图切换的时间，单位为毫秒
im.save('images/result.gif', save_all=True, append_images=images, loop=1, duration=1000, comment=b"aaabb")

print("done!")