import matplotlib.pyplot as plt
from konlpy.tag import Hannanum
from bs4 import BeautifulSoup
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import pandas as pd
import re
from collections import Counter
from wordcloud import WordCloud
# Expected chromedriver.exe
# selenium 은 보통의 크롤러의 상위버전이라고 생각하면 됨.
# 즉, 무언가를 클릭하고, 이벤트가 일어났을 때 크롤링을 할 때 사용함.

url = input('input child url(ex: 4Zcp4HYDFaS9 ) : ')
url = 'https://www.mangoplate.com/restaurants/'+url
font_path_input = 'C:/Windows/Fonts/malgun.ttf'
browser = Chrome()
browser.get(url)
browser.implicitly_wait(2)

body = browser.find_element_by_tag_name('body')

# 내용 저장을 위한 배열 지정
mg_id = []
mg_content = []
mg_date = []

# 더보기 한번에 리뷰 5개씩밖에 출력이 안됨
# 전체 리뷰 수에서 나눠서 버튼 계속 누르기..

while True:
    try:
        더보기 = browser.find_element_by_css_selector('div.RestaurantReviewList__MoreReviewButton')
        더보기.click()
        time.sleep(1)
    except:
        break

html0 = browser.page_source
html = BeautifulSoup(html0, 'html.parser')
browser.close()
result = html.find_all("li", class_='RestaurantReviewItem RestaurantReviewList__ReviewItem')
print('lenth of result : ' + str(len(result)))
for i in result:
    i = BeautifulSoup(str(i), 'html.parser')
    try:
        mg_id.append(i.find("span", class_='RestaurantReviewItem__UserNickName').text)
        mg_content.append(i.find("p", class_='RestaurantReviewItem__ReviewText').text)
        mg_date.append(i.find("span", class_='RestaurantReviewItem__ReviewDate').text)
    except:
        print('Exception!!!!!!!!!')

df = pd.DataFrame({'id': mg_id, 'content': mg_content, 'date': mg_date})
df.to_csv('mango_crawling.csv', mode='w', encoding='utf-8-sig')
print(df)

texts = ''
for i in list(df['content']):
    texts += i

# 이모티콘 제거
emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

# 분석에 어긋나는 불용어구 제외 (특수문자, 의성어)
han = re.compile(r'[ㄱ-ㅎㅏ-ㅣ!?~,".\n\r#\ufeff\u200d]')

comment_result = []
str_result = ''
for i in texts:
    tokens = re.sub(emoji_pattern, "", i)
    tokens = re.sub(han, "", tokens)
    str_result += tokens
    comment_result.append(tokens)

hannanum = Hannanum()
noun_words = list(hannanum.nouns(str_result))
print(noun_words)

count = Counter(noun_words)
words = dict(count.most_common())
print(words)
print(len(i))
print(len(words))
words_ = words
words_save = pd.DataFrame(words_, index=[0])
words_save.to_csv("mango_crawling_words.csv", mode='w', encoding='utf-8-sig')

#wordcloud 시각화
wordcloud = WordCloud(font_path=font_path_input, background_color='white', width=1600, height=1200)
cloud = wordcloud.generate_from_frequencies(words)
plt.imshow(cloud)
plt.axis('off')
plt.show()
