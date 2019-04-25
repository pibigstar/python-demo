# -*-coding:utf-8 -*-
from selenium import webdriver
import time

qq = ""
password = ""

headers = {
            'host': 'h5.qzone.qq.com',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.8',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'connection': 'keep-alive'
        }
cookies = {}

def get_heards():
    path = "D:/tools/webdriver/chrome/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)

    driver.get('https://i.qq.com/?rd=1')
    driver.switch_to.frame('login_frame')
    # 进入到输入账号密码页面
    driver.find_element_by_id('switcher_plogin').click()
    driver.find_element_by_id('u').clear()
    driver.find_element_by_id('u').send_keys(qq)
    driver.find_element_by_id('p').clear()
    driver.find_element_by_id('p').send_keys(password)
    driver.find_element_by_id('login_button').click()
    time.sleep(3)
    # 隐式等待,当查找元素或元素并没有立即出现的时候，隐式等待将等待一段时间再查找
    driver.implicitly_wait(3)

    driver.get('http://user.qzone.qq.com/{}'.format(qq))
    cookie = ''
    for item in driver.get_cookies():
        cookie += item["name"]+"="+item["value"]
    get_g_tk()
    cookies = cookie
    headers["Cookie"] = cookies
    return headers


def get_g_tk():
    p_skey = cookies[cookies.find('p_skey=') + 7: cookies.find(';', cookies.find('p_skey='))]
    h = 5381
    for i in p_skey:
        h += (h << 5) + ord(i)
    print('g_tk', h & 2147483647)
    g_tk = h & 2147483647
    return g_tk