import requests

res = requests.get('http://www.naver.com')
res.encoding='utf-8' #한글 깨지지 않음
text=res.text #한글 깨지지 않음
text = res.content.decode('utf-8')
print( res.status_code )
print( res.text )
#print '한글'
print('evanroy')