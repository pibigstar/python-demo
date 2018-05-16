#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

#https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=free&tag=Python&page=1

#存放标题的数组
link_tiltes = []
#存放链接的数组
link_urls = []

#解析出多少页
def get_page(root_url):
    respon = requests.get(root_url)
    soup = BeautifulSoup(respon.text, 'html.parser', from_encoding='utf8')
    pages = soup.select(".pagination > li")
    return len(pages)-2

def crawer(root_url):

    try:
        response = requests.get(root_url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser', from_encoding='utf8')
        titles = soup.select('.course-name')
        urls = soup.select('.course-box')
        for title in titles:
            link_tiltes.append(title.get_text())
        for url in urls:
            link_urls.append("https://www.shiyanlou.com" + url.get('href'))
    except:
        pass


def outPut(output):
    with open(output,'w') as f:
      for i in range(len(link_tiltes)):
          f.write(link_tiltes[i])
          f.write("\t"+link_urls[i]+"\n")
          print link_tiltes[i]
          print link_urls[i]
    f.close()

if __name__ == '__main__':
    tag = "Web"
    output = tag+".txt"
    root_url = "https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=free&tag=" + tag + "&page=";
    pages = get_page(root_url);
    if(pages>0):
        for i in range(pages):
            crawer(root_url + str(i + 1))
    else:
        crawer(root_url)
    outPut(output)