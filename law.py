from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from konlpy.tag import Twitter
from collections import Counter
import numpy as np
import pandas as pd
import re
import pickle

Qs = pickle.load(open('Qs.pickle', 'rb'))
As = pickle.load(open('As.pickle', 'rb'))
law = pd.read_csv("law_refined_181125.csv", encoding='cp949')
law['중과실 구분'][1] = '무면허 운전'
law['중과실 구분'][7] = '음주 운전'

twitter = Twitter()

def get_N_A(Qs):
    docs=[]
    for Q in Qs:
        words=[]
        for t in twitter.pos(Q):
            if t[1] in ['Noun', 'Adjective', 'Verb'] and len(t[0])>=2:
                words.append(t[0])
        docs.append(" ".join(words))
    return(docs)

Qs_words = get_N_A(Qs)

idf_maker = TfidfVectorizer(min_df=2)
tf_idf = idf_maker.fit_transform(Qs_words).toarray()
tf_idf_cat = idf_maker.transform(law['중과실 구분']).toarray()

def cosin_similarity(doc1, doc2) :
    son = sum(doc1*doc2)
    return(son)

def getting_highest(sen, tf_idf):
    score_list = []
    for t in tf_idf:
        score = cosin_similarity(sen, t)
        score_list.append(score)
    return(score_list.index(max(score_list)))

def returning(input_sentence):
    # input_sentence = '무단 횡단을 하다가 차와 가벼운 접촉 사고가 있었습니다. 제가 보행자 입니다. 누가 처벌을 받나요? 합의금을 받을 수 있나요?'

    input_tfidf = idf_maker.transform(get_N_A([input_sentence])).toarray()[0]
    idx = getting_highest(input_tfidf, tf_idf)

    idx_cat = getting_highest(input_tfidf, tf_idf_cat)
    law_cat = "\n\n".join(law.iloc[idx_cat,:])

    interval=64
    q = "\n".join(re.findall("(?s).{,68}", Qs[idx]))[:-1]
    a = "\n".join(re.findall("(?s).{,70}", As[idx]))[:-1]
    t = law.copy()
    t.iloc[idx_cat, 1] = "\n".join(re.findall("(?s).{,70}", t.iloc[idx_cat, 1]))[:-1]
    l = "\n\n".join(t.iloc[idx_cat, :])
    return(q,a,l)
