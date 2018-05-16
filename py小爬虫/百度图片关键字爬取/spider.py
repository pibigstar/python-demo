#coding:utf8
import requests
import os
import re
import json
import itertools
import urllib
import sys
import urllib2

str_table = {
    '_z2C$q':':',
    '_z&e3B':'.',
    'AzdH3F':'/'
}
char_table = {
'w':'a',
'k':'b',
'v':'c',
'1':'d',
'j':'e',
'u':'f',
'2':'g',
'i':'h',
't':'i',
'3':'j',
'h':'k',
's':'l',
'4':'m',
'g':'n',
'5':'o',
'r':'p',
'q':'q',
'6':'r',
'f':'s',
'p':'t',
'7':'u',
'e':'v',
'o':'w',
'8':'1',
'd':'2',
'n':'3',
'9':'4',
'c':'5',
'm':'6',
'0':'7',
'b':'8',
'l':'9',
'a':'0',
}
char_table = {ord(key):ord(value)for key,value,in char_table.items()}

def decode(url):
    for key,value in str_table.items():
        url=url.replace(key,value)
    return url.translate(char_table)

def buildUrls(word):
    # 转为URL编码
    word = urllib.quote(word)

    url = r"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word="+word+"&f=3&oq=benxi&rsp=0"
    urls = (url.format(word=word,pn=x)for x in itertools.count(start=0,step=60))
    return urls

re_url = re.compile(r'"onjURL":"(.*?)"')
def resolveImgUrl(html):
    imgUrls = [decode(x) for x in re_url.findall(html)]
    return imgUrls

def downImg(imgUrl,dirpath,imgName):
    filename = os.path.join(dirpath,imgName)
    try:
        res = requests.get(imgUrl,timeout=15)
        if str(res.status_code)[0]=='4':
            print(str(res.status_code),":","test:"+imgUrl)
            return False;
    except Exception as e:
        print ('have exception:'+e,imgUrl)
        print (e)
        return False
    with open(filename+'.jpg','wb') as f:
        f.write(res.content)
    return True

def mkDir(dirName):
    dirpath = os.path.join(sys.path[0],dirName)
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    return dirpath

if __name__ == '__main__':
    print ("欢迎使用百度图片你下载脚本\n目前仅支持单个关键词")
    print ("下载结果保存再脚本目录下的img文件夹中")
    print ("="*50)
    print ("请输入你要下载的图片你关键词:\n")
    word = raw_input()
    print word
    dirpath = mkDir("img")
    urls = buildUrls(word)

    index = 0
    for url in urls:
        print ("正在请求：",url)
        html = requests.get(url,timeout=10).content.decode('utf-8')
        imgUrls = resolveImgUrl(html)
        if len(imgUrls)==0:
            break
        for url in imgUrls:
            if downImg(url,dirpath,str(index)+".jpg"):
                index += 1
                print ("已下载%s张"%index)