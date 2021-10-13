#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import csv
import pandas as pd
from konlpy.tag import Komoran
from konlpy.corpus import kolaw
from konlpy.tag import Okt
import nltk
from nltk import Text
from collections import Counter
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from future.utils import iteritems
from collections import Counter
from collections import defaultdict
from sklearn.manifold import TSNE
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer


# In[1]:


data = pd.read_csv('clien.csv')
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
             '하나', '보이', '얘기', '마음', '우리', '사람', '가지', '생기', '잘못', '때문', '이랑', '문제'
             ,'그냥','정말','무슨','저런']

#unique_Nouns = set(nouns)
for word in nouns:
    if word in bool_words:
        while word in nouns: 
            nouns.remove(word)
            
#단순 최다 빈도 명사
#word_cnt = Counter(nouns)
#word_list = word_cnt.most_common(20)
#for v in word_list:
#    print(v)

#TF-IDF 계산값 출력
data = pd.read_csv('clien.csv')
corpus = [' '.join(i[0].split(' ')[1:]) for i in data.values]

vectorizer = TfidfVectorizer()
sp_matrix = vectorizer.fit_transform(corpus)

word2id = defaultdict(lambda : 0)
for idx, feature in enumerate(vectorizer.get_feature_names()):
    word2id[feature] = idx

for i, sent in enumerate(corpus):
    print( [ (token, sp_matrix[i, word2id[token]]) for token in sent.split() ] )
    
#TF-IDF 명사 단위로 분석 후 처리할 시

article_data = pd.read_csv('clien.csv', encoding='utf-8', header= None)
values = [' '.join(i[0].split(' ')[1:]) for i in article_data.values]

as_one = ''
for noun in nouns:
    as_one = as_one + ' ' + noun
words = as_one.split()

counts = Counter(words)

vocab = sorted(counts, key=counts.get, reverse=True)

#단어 빈도 정리
word2idx = {word.encode("utf8").decode("utf8"): ii for ii, word in enumerate(vocab,1)}

#딕셔너리로 정리
idx2word = {ii: word for ii, word in enumerate(vocab)}

#tf-idf 
tfidf = TfidfVectorizer(max_features = 10, max_df=0.95, min_df=0)

#generate tf-idf term-document matrix
A_tfidf_sp = tfidf.fit_transform(nouns)  #size D x V

#tf-idf dictionary    
tfidf_dict = tfidf.get_feature_names()
print('keyword : ', end = '')
print(tfidf_dict)

morphs_dict = {
    '키워드' : tfidf_dict,
}

df2 = pd.DataFrame(morphs_dict)
df2.to_csv('10키워드s.csv', index=False, encoding="utf-8-sig")

data_array = A_tfidf_sp.toarray()
tfidf_data = pd.DataFrame(data_array, columns=tfidf_dict)
tfidf_data
tfidf_data.shape