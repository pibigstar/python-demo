#-*- coding:utf-8 –*-
import os
import jieba.analyse
from PIL import Image,ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator

#读取data里面的词

def read_data(content_path):
    content = ''
    for f in os.listdir(content_path):
        #拼接文件完整路径
        file_fullPath = os.path.join(content_path,f)
        #判断是否是文件
        if  os.path.isfile(file_fullPath):
            print ('loading{}'.format(file_fullPath))
            #将文件内容进行拼接
            content += open(file_fullPath,'r').read()
            #每首歌歌词之间用换行符分割
            content +='\n'
        print ('done loading')
        return content

content = read_data('./data')
#显示内容前面部分
print (content[:99])

#使用jieba 提取关键词

#这里使用jieba的textrank提取1000个关键词及其比重
result = jieba.analyse.textrank(content,topK=1000,withWeight=True)
#生成关键词比重字典
keywords = dict()
for i in result:
    keywords[i[0]] = i[1]
print (keywords)

#使用wordcloud生成词云图

#初始化图片
image = Image.open('./images/qiaoba.png')
graph = np.array(image)

#生成云图，这里需要注意的是WordCloud默认不支持中文，所以这里需要加载中文黑体字库
wc = WordCloud(font_path='./fonts/simhei.ttf',background_color='white',max_words=1000,mask=graph)
wc.generate_from_frequencies(keywords)
image_color = ImageColorGenerator(graph)

#显示图片
plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_color))
plt.axis("off") #关闭图像坐标系
plt.show()