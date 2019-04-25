# -*-coding:utf-8 -*-
import requests
import login
import urllib
import json



def get_friends(heards):
    url = get_friends_url()
    result = requests.get(url=url, heards=heards)
    friendsList = json.load(result)["data"]["uinlist"]
    print friendsList


def get_friends_url(self):
    url = 'https://h5.qzone.qq.com/proxy/domain/base.qzone.qq.com/cgi-bin/right/get_entryuinlist.cgi?'
    params = {
        'uin': login.qq,
        'ver': 1,
        'fupdate': 1,
        'action': 1,
        'g_tk': login.get_g_tk()
    }
    url = url + urllib.urlencode(params)
    return url