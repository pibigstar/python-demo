# -*-coding:utf-8 -*-
import login
import getInfo

if __name__ == '__main__':
    login.qq = "741047261"
    login.password="leikewei/7410."
    heards = login.get_heards()
    getInfo.get_friends(heards)
