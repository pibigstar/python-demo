#coding:utf-8
from multiprocessing import pool as ThreadPool
from bs4 import BeautifulSoup
import urllib2
import urlparse
from threading import Thread
import time
class MyThread(Thread):
    
   
    try:
        root_url="http://www.biquge.cm/8/8263/"
        request=urllib2.Request(root_url)
        request.add_header("user-agent","Mozilla/5.0")
        content=urllib2.urlopen(request).read()
      
        soup=BeautifulSoup(content,'html.parser',from_encoding='utf-8')
        novel_title=soup.find('h1').get_text()
        fout=open('D://'+novel_title+'.txt',"a")
        print novel_title 
      
        links=soup.find('dl').find_all('a')
        for link in links:
            star_time=time.time()
            fout.write(link.get_text().encode('utf-8')+'\n')
            print link.get_text()
            url_full=urlparse.urljoin(root_url,link['href'])
            request=urllib2.Request(url_full)
            request.add_header("user-agent","Mozilla/5.0")
            text_content=urllib2.urlopen(request).read()
            
            soup=BeautifulSoup(text_content,'html.parser',from_encoding='utf-8')
            text_node=soup.find('div',class_='box_con')
            fout.write(text_node.get_text().encode('utf-8'))
            if time.time()-star_time>3:
                continue
        fout.close()
    except Exception as e:
        print e
        
t=MyThread(5)
t.star()
t.close()
t.join()