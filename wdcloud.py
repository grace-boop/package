########用dic過濾API找到出現最多次數的詞語,並輸出文字雲(以政黑板為例)#####
#######可以優化的:辭典可以加權限#####



import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud
#from udicOpenData.dictionary import *##助教給的dictionary,後來沒用因為很醜
from PIL import Image
import jieba
import numpy as np
from collections import Counter
###file = open("HatePolitics.json",'r',encoding='utf-8')
###papers = " "
###U have to follow the step to open the distinct file
def wdcloud(file):
    for line in file.readlines():
        dic=json.loads(line)
        article_title=dic['_source']['article_title']
        content=dic['_source']['content']
        papers=papers+article_title+content
    #dump2es.py jieba
    jieba.set_dictionary('2021-10-12 dict.txt.big.txt')
    jieba.add_word('柯文哲')
    jieba.add_word('陳時中')
    jieba.add_word('張亞中')
    jieba.add_word('朱立倫')
    jieba.add_word('國民黨')
    jieba.add_word('民眾黨')
    jieba.add_word('民進黨')
    jieba.add_word('台灣')
    jieba.add_word('高端')
    jieba.add_word('塔綠班')                            ####要自己多增加常用字，這個是for 政黑板

    with open('stops.txt', 'r', encoding='utf8') as f:  ####中文的停用字，我也忘記從哪裡拿到的，效果還可以，繁體字的資源真的比較少，大家將就一下吧
        stops = f.read().split('\n') 
    stops.extend(['Re','討論','「','的','民黨','會','都'])
    terms = [t for t in jieba.cut(papers, cut_all=True) if t not in stops]
    sorted(Counter(terms).items(), key=lambda x:x[1], reverse=True)
    #print(type(terms))

    font = 'SourceHanSansTW-Regular.otf'
    my_wordcloud = WordCloud(background_color='black',font_path=font,relative_scaling=0.5).generate_from_frequencies(frequencies=Counter(terms))#generate(words)

    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()
    #存檔
    my_wordcloud.to_file('word_cloud.png')

######articut好像更好，但弄不出來，討厭