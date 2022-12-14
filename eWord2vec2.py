import sys
import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
from gensim.models.word2vec import Word2Vec
from konlpy.tag import Okt


# urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings.txt", filename="ratings.txt")

#train_data = pd.read_table('ratings.txt')
train_data = pd.read_csv('ratings.txt', header=0, delimiter='\t')

print(train_data[:5])



print('NULL 값 존재 유무 : ', train_data.isnull().values.any())
print('리뷰 개수 출력 : ',len(train_data)) # 리뷰 개수 출력

train_data = train_data.dropna(how='any') # Null 값이 존재하는 행 제거
print('NULL 값 존재 유무 : ', train_data.isnull().values.any() )
print('리뷰 개수 출력 : ',len(train_data)) # 리뷰 개수 출력




# 정규 표현식을 통한 한글 외 문자 제거
train_data['document'] = train_data['document'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")
print(train_data[:5])

# 불용어 정의
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

# 형태소 분석기 OKT를 사용한 토큰화 작업 (다소 시간 소요)
okt = Okt()
tokenized_data = []
for sentence in train_data['document']:
    temp_X = okt.morphs(sentence, stem=True) # 토큰화
    temp_X = [word for word in temp_X if not word in stopwords] # 불용어 제거
    tokenized_data.append(temp_X)


print( tokenized_data[:5] ) # 상위 5개 출력




model = Word2Vec(sentences=tokenized_data, 
        size=100,
        window=5,
        min_count=5,
        workers=4,
        sg=0)
        
model.wv.most_similar("송강호")

sys.exit(0)