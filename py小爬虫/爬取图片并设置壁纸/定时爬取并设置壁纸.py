# -*-coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import datetime
import win32gui,win32con,win32api
from PIL import Image
import threading

# 设置桌面壁纸
def setWallpaper(imgPath):

   # 下载最新图片
   url = 'http://bingwallpaper.com/'
   result = requests.get(url)
   soup = BeautifulSoup(result.text,'lxml')
   image = soup.select('.cursor_zoom img')
   image_url = image[0].get('src')
   res = requests.get(image_url)
   with open(imgPath,'wb') as file:
      file.write(res.content)

   # 格式转换
   bmpImage = Image.open(imgPath)
   newPath = imgPath.replace('.jpg', '.bmp')
   bmpImage.save(newPath, "BMP")
   # 打开指定注册表路径
   reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
   # 最后的参数:2拉伸,0居中,6适应,10填充,0平铺
   win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
   # 最后的参数:1表示平铺,拉伸居中等都是0
   win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
   # 刷新桌面
   win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, newPath, win32con.SPIF_SENDWININICHANGE)
   print("set wallpaper done")

   # 每隔一个小时执行一次
   threading.Timer(60 * 30, setWallpaper()).start()

if __name__=='__main__':

   filepath = "D:\\images"
   date = datetime.datetime.now()
   cd = str(date.year) + '0' + str(date.month) + str(date.day)
   imgPath = os.path.join(filepath, cd + '.jpg')
   if not os.path.exists(filepath):
      os.makedirs(filepath)

   setWallpaper(imgPath)