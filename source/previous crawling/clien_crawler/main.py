import sys
import json
import openpyxl
import configparser
from tqdm import tqdm

from excel import *
from crawler import get_data

result_path = './result.xlsx'
result_word_path = './result_word.xlsx'

if __name__ == "__main__":
    
    try:
        make_excel(result_path)
        print('엑셀 파일 생성.')
    except PermissionError:
        print('엑셀 파일 생성 불가. 열려 있는 엑셀 파일을 종료해주세요.')
        sys.exit(1)
    print('============================')

    start_idx = 1
    with tqdm(total=100, ncols=80, desc='파일 생성 중') as pbar:
        for item in get_data():
            start_idx = append_excel(result_path, item, start_idx)
            pbar.update(1)
    print('============================')
    print('작업 완료.')
    input()
    
    try:
        make_excel2(result_word_path)
        print('엑셀 파일 생성.')
    except PermissionError:
        print('엑셀 파일 생성 불가. 열려 있는 엑셀 파일을 종료해주세요.')
        sys.exit(1)
    print('============================')

    start_idx2 = 1
    with tqdm(total=100, ncols=80, desc='파일 생성 중') as pbar:
        for item in get_data():
            start_idx2 = append_excel2(result_word_path, item, start_idx2)
            pbar.update(1)
    print('============================')
    print('작업 완료.')
    input()