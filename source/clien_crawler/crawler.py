import re
import requests
from bs4 import BeautifulSoup

from pprint import pprint

# links
def get_data(keyword):    
    def _get(page):
        url = 'https://www.clien.net/service/group/community?&od=T31&category=0&po={}'.format(page)
        req = requests.get(url)
        bs = BeautifulSoup(req.text, 'lxml')

        # 범위 벗어난 페이지인 경우
        if bs.find('div', class_='board-nav-area').get_text() == '':
            return [], False

        container = bs.find('div', class_='nav_content') # 크롤링해올 공간
        divs = container.find_all('div', class_="list_item symph_row")

        result = list()
        for div in divs:
            try:
                #title & link
                link_box = div.find('div', class_="list_title").find('a', class_='list_subject') # 게시글제목
                link = "https://www.clien.net" + link_box['href']
                title = link_box.get_text().strip().replace('=', '')

                view = div.find('div', class_="list_hit").find('span', class_="hit").get_text().strip().replace('=', '') # 조회수
                date = div.find('div', class_="list_time").find('span', class_="time popover").get_text().strip().replace('=', '') # 작성날짜

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

                temp = {"link": link, "title": title, "author": auth, "view": view, "date": date, "contents": contents, "comments": comments}
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
    contents = bs.find('div', class_='post_article').get_text().strip().replace('\xa0', ' ').replace('\n', ' ').replace('\t', ' ').replace('=', '')
    return contents

def get_comments(bs):
    wrapper = bs.find('div', class_='comment')
    comments = wrapper.find_all('div', class_='comment_row')

    result = list()
    for item in comments:
        try:
            temp = {
                'author': '',
                'date': '',
                'comment': ''
            }
            nickname = item.find('span', class_='nickname')
            if nickname.find('img'):
                temp['author'] = nickname.find('img')['alt']
            else:
                temp['author'] = nickname.get_text().strip().replace('\n', ' ')
            temp['date'] = item.find('span', class_='time popover').get_text().strip().replace('\xa0', ' ').replace('\n', '').replace('\t', '').replace('=', '')
            if '/' in temp['date']:
                temp['date'] = temp['date'].split('/')[0].strip()
            temp['comment'] = item.find('div', class_='comment_view').get_text().strip().replace('\xa0', ' ').replace('\n', ' ').replace('\t', ' ').replace('=', '')
            result.append(temp)
        except:
            continue
    return result
