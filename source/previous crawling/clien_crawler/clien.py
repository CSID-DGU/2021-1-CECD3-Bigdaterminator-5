#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import time
import os
import sys
import re
import io
import json
import csv
import openpyxl
import pandas as pd
import numpy as np
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from konlpy.tag import Okt
from nltk import Text
from pykospacing import spacing
import kss


# In[2]:


browser = Chrome()

titles = []
links = []
    
#링크, 제목
for i in range(1,3):
    browser.get("https://www.clien.net/service/group/clien_all?&od=T33&category=0&po=" + str(i))
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    container = soup.find('div', class_='list_content') # 크롤링해올 공간
    first_list = container.find_all('div', class_="list_item symph_row")

    for div in first_list:
        link_box = div.find('div', class_="list_title").find('a', class_='list_subject')
        link = "https://www.clien.net" + link_box['href']
        links.append(link)
        real_title = div.find('div', class_="list_title").find('span', class_="subject_fixed").get_text().strip().replace('=', '') # 게시글제목
        real_title = re.sub('[-=+_★♥♡,#/\?:╋^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》—;]', '', real_title)
        titles.append(real_title)


#본문
txt = []
    
for i in links:
    try: 
        res = requests.get(i)
        res.raise_for_status()
        res.encoding = None            
        html2 = res.text
        
        soup = BeautifulSoup(html2, 'html.parser')
        parags = soup.findAll("div", {"class" : "post_article"})
        
        content = ""

        for parag in parags:
            content += parag.text
        content = re.sub('[ㄱ-ㅎㅏ-ㅣa-zA-Z0-9]', '', content)
        content = re.sub('[ㅋ]', '', content)
        #content = re.sub('[&nbsp;|\n|\t|\r]', '', content)
        content = re.sub('[\xa0]', '', content)
        content = re.sub('[-=+_★♥♡,#/\?:╋^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》—;]', '', content)
        content = spacing(content)
        
        txt.append(content)
             
    except HTTPError as e:
        txt.append('')
    except URLError as e:
        txt.append('')
    except AttributeError as e:
        txt.append('')
        
#print(txt)


# In[4]:


#댓글
comments =[]

for i in links:
    try: 
        res = requests.get(i)
        res.raise_for_status()
        res.encoding = None            
        html2 = res.text
        
        soup = BeautifulSoup(html2, 'html.parser')
        contentArea = soup.find("div", {"class" : "comment"})            
        parags = contentArea.findAll("div", {"class" : "comment_view"})
        
        content = ""

        for parag in parags:
            content += parag.text
        content = re.sub('[ㄱ-ㅎㅏ-ㅣa-zA-Z0-9]', '', content)
        content = re.sub('[&nbsp;|\n|\t|\r]', '', content)
        content = re.sub('[\xa0]', '', content)
        content = re.sub('[ㅋ]', '', content)
        content = re.sub('[님]', '', content)
        content = re.sub('[-=+_★♥♡,#/\?:╋^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》—;]', '', content)    
        content = spacing(content)
        
        comments.append(content)
    
    except HTTPError as e:
        txt.append('')
    except URLError as e:
        txt.append('')
    except AttributeError as e:
        txt.append('')

#print(comments)


# In[5]:


# KoNLPy 형태소 분석
okt = Okt() 

title_morphs = []
txt_morphs = []
comment_morphs = []
    
for i in titles:
    title_morphs.append(okt.morphs(i))
    
for i in txt:
    txt_morphs.append(okt.morphs(i))
    
for i in comments:
    comment_morphs.append(okt.morphs(i))  
        
nate_dict = {
    '제목' : titles,
    '본문' : txt,
    '댓글' : comments
}

df = pd.DataFrame(nate_dict) 
df.to_csv('clien.csv', index=False, encoding="utf-8-sig")
    
morphs_dict = {
    '제목 형태소' : title_morphs,
    '본문 형태소' : txt_morphs,
    '댓글 형태소' : comment_morphs
}

df2 = pd.DataFrame(morphs_dict)
df2.to_csv('clien_Morphs.csv', index=False, encoding="utf-8-sig")

browser.close()


# In[ ]:




