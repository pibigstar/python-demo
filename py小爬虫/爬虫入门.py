#coding:utf-8
import urllib2
import cookielib
from bs4 import BeautifulSoup
import requests
from lxml import etree
url="http://www.baidu.com"

print "第一种方法,不做任何处理"
response1=urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print "将爬虫伪装成一个浏览器"
request=urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2=urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print "第三种，增加cookie处理"
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3=urllib2.urlopen(request)
print response3.getcode()
print len(response3.read())
print cj


print  "使用Xpath"
content = requests.post(url, data=data, cookies=cookies)
selector = etree.HTML(content)
title = selector.xpath('//*[@id="cb_post_title_url"]')