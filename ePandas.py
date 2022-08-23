


import pandas as pd

'''
시리즈(Series)
'''
pdObj = pd.Series([17000, 18000, 1000, 5000], index=["피자", "치킨", "콜라", "맥주"])

print('시리즈 출력 :')
print('-'*20)
print(pdObj)

print('Series 값 : {}'.format(pdObj.values))
print('Series 인덱스 : {}'.format(pdObj.index))

print('sri["피자"] = ', pdObj["피자"])


'''
데이터프레임(DataFrame)
'''

values = [[1,2,3],
          [4,5,6],
          [7,8,9]]
index   = ['1','2','3']
columns = ['A', 'B', 'C']

pdObj = pd.DataFrame( values, index, columns)

print('DataFrame 출력 : ')
print('-'*20)
print(pdObj)

print('DataFrame 값 : {}'.format(pdObj.values))
print('DataFrame 인덱스 : {}'.format(pdObj.index))



'''
DataFrame 생성
'''

# list 생성
data = [
    ['1000', 'Steve', 90.72], 
    ['1001', 'James', 78.09], 
    ['1002', 'Doyeon', 98.43], 
    ['1003', 'Jane', 64.19], 
    ['1004', 'Pilwoong', 81.30],
    ['1005', 'Tony', 99.14],
]

df = pd.DataFrame(data, columns=['학번', '이름', '점수'], index=['1','2','3','4','5','6'])
print(df)
print(df.head(3))
print(df['학번'])

# dictionary 생성
data = {
    '학번' : ['1000', '1001', '1002', '1003', '1004', '1005'],
    '이름' : [ 'Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],
    '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]
    }

df = pd.DataFrame(data)
print(df)
print(df.tail(2))
print(df['이름'])


'''
외부 데이터 읽기 :: Pandas는 CSV, 텍스트, Excel, SQL, HTML, JSON 등 다양한 데이터 파일을 읽고 데이터 프레임을 생성할 수 있습니다.
'''

pdObj = pd.read_csv('cvsfile.csv')
print(pdObj)


'''
넘파이(Numpy)는 수치 데이터를 다루는 파이썬 패키지입니다. 
다차원 행렬 자료구조인 ndarray를 통해 벡터 및 행렬을 사용하는 선형 대수 계산에서 주로 사용됩니다. Numpy는 편의성뿐만 아니라, 속도면에서도 순수 파이썬에 비해 압도적으로 빠르다는 장점이 있습니다.
'''

import numpy as np

vec = np.array([1,2,3,4,5])
print(vec)


mat = np.array([[10,20,30],[40,50,60]])
print(mat)

print('vec TYPE : ', type(vec))
print('vec 축개수 : ', vec.ndim) #축의 갯
print('vec 크기(shape)', vec.shape)


print('mat TYPE : ', type(mat))
print( mat.ndim )
print( mat.shape )

mat = np.zeros((2,5))
print(mat)

mat = np.ones((2,3))
print(mat)

mat = np.full((2,3),7)
print(mat)

mat = np.eye(3,5)
print(mat)

mat = np.random.random((2,5))
print(mat)

mat = np.arange(1,10,2)
print(mat)

mat = np.array([[1,2,3],[4,5,6],[7,8,9]])

slicing = mat[0,:]
print(slicing)
slicing = mat[0]
print(slicing)

slicing = mat[1,:]
print(slicing)
slicing = mat[1]
print(slicing)

slicing = mat[2,2]
print(slicing)

indexing_mat = mat[[0, 1],[0, 1]]   # [[행1,행2],[열1,열2]]
print(indexing_mat)