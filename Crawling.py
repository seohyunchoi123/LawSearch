import re
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import numpy as np
import pickle


def get_urls(n_pages):
    urls = []
    for i in range(1, n_pages + 1):
        address = 'https://kin.naver.com/qna/expertAnswerList.nhn?dirId=60201&queryTime=2018-11-17%2011%3A43%3A19&page='
        r = requests.get("{}{}".format(address, i))
        soup = BeautifulSoup(r.content, "html.parser")
        all = soup.findAll("tr")
        for t in all[1:]:  # 첫 url은 홈화면임
            urls.append(t.find('a')['href'])
    return (urls)


def get_Q_A(t):
    try:
        r_url = requests.get('https://kin.naver.com' + t)
        soup_url = BeautifulSoup(r_url.content, "html.parser")
        head = soup_url.find('div', {'class': 'title'}).get_text().replace("\n", '').replace('\t', '').replace('\xa0',
                                                                                                               '')
        q = soup_url.find('div', {'class': 'c-heading__content'}).get_text().replace("\n", '').replace('\t',
                                                                                                       '').replace(
            '\xa0', '')
        a = soup_url.findAll('div', {'class': "_endContentsText c-heading-answer__content-user"})[0].get_text().replace(
            "\n", '').replace('\t', '').replace('\xa0', '')
        # 저 링크는 실제로 답변이 다 한개식뿐이다
    except:
        r_url = requests.get('https://kin.naver.com' + t)
        soup_url = BeautifulSoup(r_url.content, "html.parser")
        head = soup_url.find('div', {'class': 'title'}).get_text().replace("\n", '').replace('\t', '').replace('\xa0',
                                                                                                               '')
        q = soup_url.find('div', {'class': 'title'}).get_text().replace('\t', "").replace('\n', '').replace('\xa0', '')
        a = soup_url.findAll('div', {'class': "_endContentsText c-heading-answer__content-user"})[0].get_text().replace(
            "\n", '').replace('\t', '').replace('\xa0', '')
    return (" ".join([head, q]), a)  # 질문에 제목도 같이 붙여놓기


urls = get_urls(99)

Qs = []
As = []
error = 0
i = 0
for url in urls:
    try:
        q, a = get_Q_A(url)
        Qs.append(q)
        As.append(a)
        i += 1
        if i % 50 == 0:
            print(i)
    except:
        error += 1
        print("%d 번쨰 오류 링크 : %s" % (error, url))

print(len(Qs), len(As))

f = open("Qs.pickle", 'wb')
pickle.dump(Qs, f)

f = open("As.pickle", 'wb')
pickle.dump(As, f)