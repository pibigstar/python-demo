# -*-coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait   # WebDriverWait的作用是等待某个条件的满足之后再往后运行
import time
import sys

# 构造网页驱动
driver = webdriver.PhantomJS(executable_path='phantomjs.exe')
# 打开网页
driver.get('http://www.cncrawler.com/forum.php')

# 输入表单
driver.find_element_by_xpath('//*[@id="ls_username"]').send_keys('pibigstar')
driver.find_element_by_xpath('//*[@id="ls_password"]').send_keys('123456')

# 截取当前页面的图片
driver.get_screenshot_as_file('yanzhengma.jpg')

# 手工打码
input_solution = input('请输入验证码 :')
driver.find_element_by_xpath('//input[@name="captcha"]').send_keys(input_solution)
time.sleep(2)

# 表单的提交  表单的提交，即可以选择登录按钮然后使用click方法，也可以选择表单然后使用submit方法
driver.find_element_by_xpath('//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button').click()

# 定位当前页面
sreach_widonw = driver.current_window_handle

try:
    dr = WebDriverWait(driver,5)
    if driver.find_element_by_xpath('//*[@id="um"]/p[1]/strong/a'):
        print('登录成功')
except:
    print('登录失败')

# 截取当前页面的图片
driver.save_screenshot('screen/screen_shoot.jpg')

# 退出
sys.exit(0)
driver.quit()