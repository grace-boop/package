#####呼叫此檔案，可以觀看特定時間間格(設定是一星期)內的看板貼文數變化#######


import json
import collections
import networkx as nx
import urllib.request as req
import matplotlib.pyplot as plt
import bs4
import urllib.request as req
import time
from datetime import datetime 
def txt():                                    ###輸出成txt檔，做animation board
    now = int(time.time())                    ###current time stamp, precision to second
    early = now - 500000                      ###one week ago
    str_now=str(now)                          ###轉成str
    str_early=str(early)
    print(str_early)
    print(str_now)
    struct_time = time.localtime(now) # 轉成時間元組
    timeString = time.strftime("%Y-%m-%d", struct_time)
    board=['Gossiping',
        'Stock',
        'Baseball',
        'C_Chat',
        'Lifeismoney',
        'NBA',
        'DIABLO',
        'home-sale',
        'LoL',
        'Tech_Job',
        'car',
        'Beauty',
        'KoreaStar',
        'MobileComm',
        'sex',
        'BabyMother',
        'PC_Shopping',
        'movie 718',
        'WomenTalk',
        'HatePolitics',
        'Guardians',
        'Boy-Girl',
        'basketballTW',
        'e-shopping',
        'KoreaDrama',
        'japanavgirls',
        'AllTogether',
        'joke',
        'marriage',
        'iOS',
        'Tainan']
    for i in range(len(board)):
        import requests
        r = requests.get("https://ptt.nlpnchu.org/api/GetByBoard?board="+board[i]+"&start="+str_early+"&end="+str_now,verify=False)
        #print(r.status_code)
        list_of_dicts = r.json()
        print(list_of_dicts['total']['value'])
        with open('tt.txt', 'a',encoding= 'utf-8') as fr:          ###輸出成txt檔，做animation board
            if i == 0:
                fr.write('date,name,category,value\n')
            fr.write(timeString+',')
            fr.write(board[i]+',')
            fr.write(board[i]+',')
            fr.write(str(list_of_dicts['total']['value']))
            fr.write('\n')