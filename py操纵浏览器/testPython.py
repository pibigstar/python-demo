# -*-coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
path = "D:/tools/webdriver/chrome/chromedriver.exe"
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=path)
driver.get("https://zhaoxuyang.com/")


driver.save_screenshot('screen/1.jpg')

# 退出
sys.exit(0)
driver.quit()