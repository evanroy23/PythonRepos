

''''
제어문
https://www.delftstack.com/ko/tutorial/python-3-basic-tutorial/
'''

# if ... elif .. else



a = -34

if a > 0:
    print("Number is Positive")
    print("a > 0 : ", a)
elif a < 0 :
    print("Number is Negative")
    print("a < 0 : ", a)
    
    if a > -100 :
        print(">> a > -100 : ", a)
    else :
        print(">> a < -100 : ", a )
        
else :
    print("Number is zero")
    print("a = 0 : ", a)
    

'''
for 
while
'''

x = [1,2,3,4,5,6,7,8,9]

sum = 0
for i in x :
    sum = sum + i
    
print("sum = ", sum)


sum = 0
i = 0
while i < 10 :
    sum += i
    print( sum , " += ", i )
    i = i + 2
print( "sum = " ,sum )    

'''
for ~ else
list : [] 
'''
x = ['python','java','c','php','kotlin']

print(x)
print(list(x))
print(len(x))
print(list(range(len(x))))

for i in range(len(x)) :
    print( "x array[",i,"] = " , x[i] )
else :
    print ( "x list end !!")    

'''
break, continue
'''

for i in "Python" :
    if i == "h" :
        # break
        continue
    print(i)

'''
pass 는 실제로 null문이며 일반적으로 자리 표시 자로 사용됩니다. 함수 나 루프를 선언하고 싶지만 구현을 제공하지 않으려면 pass 문을 사용할 수 있습니다.
'''
l = ['p', 'y', 't', 'h', 'o', 'n']
for i in l:
    pass


'''
def :: function
'''

def FuntionName(b):
    a = 100 + b
    return a

print(FuntionName(10))


def getName( n='이정호', a=45 ):
    print("name : ", n , " age :" , a )
    return 'a'
getName()

'''
def ::  함수 임의의 인수(*)
        함수 임의의 인수 호출되기 전에 튜플로 변환 (**)
'''

def language(*args):
    for i in args :
        print( "language Name : ", i )
        
language("php", "java", "R", "C++")

def getUserInfo(**args):
    for i in args :
        print( i," = " , args[i])
    
    print("args['name'] : ", args['name'])
        
getUserInfo( name='이정호', age=45 )


'''
def :: 재귀함수
sys :: 파이썬은 재귀 호출 제한을 3000으로 설정
'''


def fact(n):
    if n == 1 :
        return 1
    else :
        factRes = fact( n-1 )
        print( n , " * " , factRes )
        return ( n * factRes )

a = 6
print( fact(a) )


import sys
#sys.getrecursionlimit(10000)
print( sys.getrecursionlimit() )


'''
파일 객체
import os
'''
import os
print( os.getcwd() ) # 현재디렉토리
print( os.listdir() ) # 디렉토리 내용
# os.remove("Python.txt") # 파일 삭제

fobj = open("D:/PythonRepos/Examplefile.txt", 'r+', encoding='UTF8')
#fobj.write("\nHello Python Programming")

lines = fobj.readlines()

for i in lines :
    print(i)
    
fobj.close()


