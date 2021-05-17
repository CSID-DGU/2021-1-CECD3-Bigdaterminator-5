from bs4 import BeautifulSoup
import time
from selenium.webdriver import Chrome
import openpyxl
import pandas as pd

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active

browser = Chrome()

result_list = []
result_time = []

for i in range(1,11):
    browser.get("https://www.fmkorea.com/index.php?mid=news&page=" + str(i))
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    result= soup.find_all("td", class_="hotdeal_var8")
    #print('length of result : ' + str(len(result)))
    for i in result:
        i = BeautifulSoup(str(i), 'html.parser')
        try:
            print(i.find("td", class_="title hotdeal_var8").text)
            result_list.append(i.find("td", class_="hotdeal_var8").text)
        except:
            print('Occur Error !')


df = pd.DataFrame({'result_list' : result_list})
df.to_csv('FM_crawling.csv', mode='w', encoding='utf-8-sig')
print(df)
