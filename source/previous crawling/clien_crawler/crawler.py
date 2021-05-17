import re
import requests
from konlpy.tag import Okt
from collections import Counter

from bs4 import BeautifulSoup

from pprint import pprint

# links
def get_data():    
    def _get(page):
        url = 'https://www.clien.net/service/group/clien_all?&od=T33&category=0&po={}'.format(page)
        req = requests.get(url)
        bs = BeautifulSoup(req.text, 'lxml')

        # 범위 벗어난 페이지인 경우
        if bs.find('div', class_='board-nav').get_text() == '':
            return [], False

        container = bs.find('div', class_='list_content') # 크롤링해올 공간
        divs = container.find_all('div', class_="list_item symph_row")

        result = list()
        total_contents = []
        
        for div in divs:
            try:
                #title & link
                link_box = div.find('div', class_="list_title").find('a', class_='list_subject')
                link = "https://www.clien.net" + link_box['href']
                
                title = div.find('div', class_="list_title").find('span', class_="subject_fixed").get_text().strip().replace('=', '') # 게시글제목
                view = div.find('div', class_="list_hit").find('span', class_="hit").get_text().strip().replace('=', '') # 조회수
                date = div.find('div', class_="list_time").find('span', class_="timestamp").get_text().strip().replace('=', '') # 작성날짜

                nickname = div.find('div', class_="list_author").find('span', class_="nickname") # 작성자
                if nickname.find('img'):
                    auth = nickname.find('img')['alt']
                else:
                    auth = nickname.get_text().strip().replace('\n', ' ')

                req2 = requests.get(link)
                bs2 = BeautifulSoup(req2.text, 'lxml')
                try:
                    contents = get_content(bs2)
                except:
                    contents = ''

                comments = []
                comments = get_comments(bs2)
                total_contents.append(contents)
                                    
                nlp = Okt()
                morphs1 = nlp.morphs(title) # 형태소 분석
                strA = ",".join(morphs1)
                morphs2 = nlp.morphs(contents)
                strB = ",".join(morphs2)
                
                countA = len(morphs1)
                countB = len(morphs2)
                count = countA + countB

                temp = {"link": link, "title": title, "author": auth, "view": view, "date": date, "contents": contents, "comments": comments, "morphs1": strA, "morphs2": strB, "counts": count}
                result.append(temp)
           
        
            except Exception as exc:
                continue
                
        return result, True
    
    for page in range(0, 100):
        data, flag = _get(page)
        if flag:
            yield data
        else:
            break

def get_content(bs):
    contents = bs.find('div', class_='post_article').get_text().strip().replace('\xa0', ' ').replace('\n', ' ').replace('\t', ' ').replace('=', '').replace('*', '').replace('!', '').replace('@', '').replace('#', '').replace('^', '').replace('%', '').replace('~', '').replace('?', '').replace('.', '').replace('+', '')
    return contents

def get_comments(bs):
    wrapper = bs.find('div', class_='comment')
    comments = wrapper.find_all('div', class_='comment_row')

    result = list()
    for item in comments:
            
            comment = item.find('div', class_='comment_view').get_text().strip().replace('\xa0', ' ').replace('\n', ' ').replace('\t', ' ').replace('=', '').replace('님', '').replace('*', '').replace('!', '').replace('@', '').replace('#', '').replace('^', '').replace('%', '').replace('~', '').replace('?', '').replace('.', '').replace('+', '')
            
            nlp = Okt()
            morphs3 = nlp.morphs(comment) # 형태소 분석
            strC = ",".join(morphs3)
            countC = len(morphs3)
            temp = {"morphs3": strC, "counts": countC}
                
            result.append(temp)

    return result
