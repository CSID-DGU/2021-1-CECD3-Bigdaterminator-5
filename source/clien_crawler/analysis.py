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

word_cnt = Counter(nouns)
word_list = word_cnt.most_common(20)
for v in word_list:
    print(v)

print('=========================')
#TF-IDF     
data = pd.read_csv('clien.csv')
corpus = [' '.join(i[0].split(' ')[1:]) for i in data.values]
tk = []
ss = 0
vectorizer = TfidfVectorizer()
sp_matrix = vectorizer.fit_transform(corpus)

word2id = defaultdict(lambda : 0)
for idx, feature in enumerate(vectorizer.get_feature_names()):
    word2id[feature] = idx

for i, sent in enumerate(corpus):
    print( [ (token, sp_matrix[i, word2id[token]]) for token in sent.split() ] )
    for token in sent.split():
        tk.insert(i,token)
         

#TF-IDF 
#전체 CSV 파일 직접 입력 시
#TF-IDF 이미 한번 명사 단위로 정리 한 명단으로 처리할 시

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
print(tfidf_dict)


data_array = A_tfidf_sp.toarray()
tfidf_data = pd.DataFrame(data_array, columns=tfidf_dict)
tfidf_data
tfidf_data.shape

#토픽 모델링
# LDAModel을 생성합니다.
import tomotopy as tp
model = tp.LDAModel(k=20, alpha=0.1, eta=0.01, min_cf=5)

for i, line in enumerate(nouns): #open('natepann.csv', encoding='utf-8')):
    model.add_doc(line.strip().split()) 

model.train(0) 
print('Total docs:', len(model.docs))
print('Total words:', model.num_words)
print('Vocab size:', model.num_vocabs)

 
for i in range(model.k):
    res = model.get_topic_words(i, top_n=10)
    print('Topic #{}'.format(i), end='\t')
    print(', '.join(w for w, p in res))

print('=========================')
negative_word_emotion = ['안','않','못','없','아닌','아니']
est = []
count = 0
ki = 0

data = pd.read_csv('clien.csv')
data.values
for i in data.values:
    for j in negative_word_emotion:
        if j in str(i):
            count += 1
    est.insert(ki,count)
    ki += 1
    count = 0
    
for v in est:
    print(v)
    
print('=========================')
positive_word_emotion = ['훌륭','고맙','감사','좋']
est2 = []
count2 = 0
k = 0

data2 = pd.read_csv('clien.csv')
data2.values
for i in data2.values:
    for j in positive_word_emotion:
        if j in str(i):
            count2 += 1
    est2.insert(k,count2)
    k += 1
    count2 = 0
    
for v in est2:
    print(v)
print('=========================') 
est3 = []
t=0

for i in est:
    est3.insert(t,i-est2[t])
    t +=1
    
for v in est3:
    print(v)
print('=========================')
tt = 0
positive = 0
negative = 0
for v in tk:
    if est3[tt] > 0:
        print(v,' : 부정')
        negative += 1
        if tt == 30 :
            break
    else:
        print(v,' : 긍정')
        positive += 1
    tt += 1
print('=========================')

#% 시각화
import matplotlib.pyplot as plt
pos = positive
neu = negative

size = [pos, neu]

label = ['Positive','Negative']

plt.axis('equal')
plt.pie(x=size, labels=label, autopct='%.2f%%')

plt.legend()
plt.show()