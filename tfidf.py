from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from janome.tokenizer import Tokenizer
import re
import numpy as np
import glob


'''
with open('MLFmethods.txt') as f:
    txt_list2 = f.read()
    txt_list2 = re.sub("\n", " ", txt_list2)
txt_list2 = [txt_list2]
'''
#ファイルの読み込みと成型
files = glob.glob("txtfiles/*")
#print(files)
files2 = []
for file in files:
    with open(file) as f:
        file = f.read()
        file = re.sub("\n", " ", file)
        files2.append(file)

#print(files2)

#モデルの生成
def make_model(docs):
    #docs = [docs]
    vectorizer = TfidfVectorizer(smooth_idf = False)
    #TF-IDFの計算
    values = vectorizer.fit_transform(docs).toarray()
    #特徴量ラベルの取得
    words = vectorizer.get_feature_names_out()
    #結果
    print(values)
    print(words)
    cs = cosine_similarity(values, values)
    return cs

print(make_model(files2))

'''
#cos類似度を計算する
def cos_sim(v1, v2):
    #return cosine_similarity(v1, v2)


va_list = []
for vas in make_model(files2):
    va_list.append(vas)

print(cos_sim(va_list[0], va_list[1]))
'''