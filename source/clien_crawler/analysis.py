#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import csv
import pandas as pd
from konlpy.corpus import kolaw
from konlpy.tag import Okt
import nltk
from nltk import Text
from collections import Counter


# In[1]:


data = pd.read_csv('clien_Morphs.csv')
data.values
values = "".join(str(i) for i in data.values)

okt = Okt()

total_morphs = okt.morphs(values)

print("전체 형태소 개수: ")
print(len(total_morphs))

nouns = okt.nouns(values)
print("전체 명사 개수: ")
print(len(nouns))

nouns = [noun for noun in nouns if len(noun) >= 2]

bool_words = ['아니', '아서', '아도', '진짜', '생각', '라고', '지만', '정도', '만나', '제가', '지금', 
             '하나', '보이', '얘기', '마음', '우리', '사람', '가지', '생기', '잘못', '때문', '이랑', '문제']

#unique_Nouns = set(nouns)
for word in nouns:
    if word in bool_words:
        while word in nouns: 
            nouns.remove(word)

word_cnt = Counter(nouns)
word_list = word_cnt.most_common(20)
for v in word_list:
    print(v)


# In[ ]:




