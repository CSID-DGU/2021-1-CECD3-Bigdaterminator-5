import re
import time
from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
from konlpy.tag import Hannanum
from konlpy.tag import Kkma
from konlpy.tag import Okt
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from wordcloud import WordCloud

kkma = Kkma()
okt = Okt()

url = input('분석할 url을 입력하세요. (ex: 4Zcp4HYDFaS9 ) : ')
url = 'https://www.mangoplate.com/restaurants/'+url
font_path_input = 'C:/Windows/Fonts/malgun.ttf'
browser = webdriver.Chrome('./chromedriver.exe')
browser.get(url)
browser.implicitly_wait(2)

body = browser.find_element_by_tag_name('body')

# 내용 저장을 위한 배열 지정
mg_id = []
mg_content = []
mg_date = []

# 더보기 한번에 리뷰 5개씩밖에 출력이 안됨
# 전체 리뷰 수 보통 가장 많은 것이 120개 따라서 더보기를 약 30번 클릭하면 보통 끝까지 다 스크롤
# 중구 식당에 대한 리뷰 수도 통계내어 page_down 변수 수정할 수 있음
# 바디 스크롤하며 더보기 클릭하고, 로딩 시간 염두에 두어 sleep(1)한다.

page_down = 30
while page_down:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    page_down -= 1
    try:
        더보기 = browser.find_element_by_css_selector('div.RestaurantReviewList__MoreReviewButton')
        action = ActionChains(browser).move_to_element(더보기)
        action.perform()
        더보기.click()
    except:
            None

html0 = browser.page_source
html = BeautifulSoup(html0, 'html.parser')
browser.close()

result = html.find_all("li", class_='RestaurantReviewItem RestaurantReviewList__ReviewItem')
print('리뷰 개수 : ' + str(len(result)))

for i in result:
    i = BeautifulSoup(str(i), 'html.parser')
    try:
        mg_id.append(i.find("span", class_='RestaurantReviewItem__UserNickName').text)
        mg_content.append(i.find("p", class_='RestaurantReviewItem__ReviewText').text)
        mg_date.append(i.find("span", class_='RestaurantReviewItem__ReviewDate').text)
    except:
        print('Exception')

df = pd.DataFrame({'id': mg_id, 'content': mg_content, 'date': mg_date})
df.to_csv('mango_crawling.csv', mode='w', encoding='utf-8-sig')
print(df)

total_review = ''
#dataframe 열 'content'만큼 range 돌며 내용 가져와 전처리
#앞으로 문장 단위로 자르고 이상한 띄어씌기 등에 대한 전처리를 포함하도록 코딩해야함.
for i in range(len('content')):
    r = df.loc[i]['content']
    #하나의 리뷰에서 문장 단위로 자르기
    #불용어 제거: 영어, 자음, 모음, 특수문자 제거
    for sentence in kkma.sentences(r):
        sentence = re.sub('([a-zA-Z])','',sentence)
        sentence = re.sub('[ㄱ-ㅎㅏ-ㅣ]+','',sentence)
        sentence = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','',sentence)
        total_review += sentence


hannanum = Hannanum()
noun_words = list(hannanum.nouns(total_review))
print(noun_words)

count = Counter(noun_words)
words = dict(count.most_common())
print(words)
print(len(words))

words_ = words
words_save = pd.DataFrame({'words' : words_, 'amount' : len(words_)})
words_save.to_csv("mango_crawling_words.csv", mode='w', encoding='utf-8-sig')

#wordcloud 시각화
wordcloud = WordCloud(font_path=font_path_input, background_color='white', width=1600, height=1200)
cloud = wordcloud.generate_from_frequencies(words)
plt.imshow(cloud)
plt.axis('off')
plt.show()
