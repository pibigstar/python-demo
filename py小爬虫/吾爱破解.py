#coding:utf8
import urllib2
from bs4 import BeautifulSoup
import time
class craw():
    def crawSpider(self):
        page=1
        dates=[]
        try:
            while page<=10:
               root_url="http://www.52pojie.cn/forum-2-"+str(page)+".html"
               html_cont=urllib2.urlopen(root_url).read()
               date=self.parse1(html_cont)
               dates.append(date)
               page=int(page)+1
               print page
               self.output_txt(dates)
        except Exception as e:
            print e
    def parse1(self,html_cont):
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        res_date={}
        links=soup.find_all('a',class_="s xst")
        #print links
        for link in links:
            res_date['url']=link['href']
            res_date['title']=link.get_text()
        return res_date
    def output_txt(self,dates):
        fout=open("D://wuai.txt","a")
        for date in dates:
           print date['url']
           print date['title']
           fout.write(date['title'].encode('utf-8')+"\t")
           fout.write(date['url'].encode('utf-8')+"\n\n\n")
           time.sleep(3)
        fout.close()
                   
           
if __name__=="__main__":
    obj_spider=craw()
    obj_spider.crawSpider()