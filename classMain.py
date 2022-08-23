
'''
구조 

PythonRepos
- classMain.py
- classFileName.py
- subClass
    - sub2
        - clssFileName2.py
        

@property 사용 예제 ::  class2.propertyPrint

다중 상속

    class subA:
        #members
    class A(subA):
        #members
    class B:
        #members
    class child(A, B):
        def __init__(self):
            B.__init__(self,'인수전달')
        #members


@property 사용 예제 ::  class3.propertyPrint2
@propertyPrint2.setter
    
    
try: ~~~ except : ~~~    
    
'''

import sys
import classFileName
from subClass.sub2 import classFileName2
import classExtends


try:
    
    class1 = classFileName.className()
    class2 = classFileName2.ClassName2(100, 20)
    class3 = classExtends.classExtendsName('한국','5000만','서울')



    class1.print()
    class1.set_all(10, 20)
    class1.print()
    print('class2.propertyPrint Return : ', class2.propertyPrint )
    class2.print()

    class3.show()
    class3.classNameShow(3000,2000)
    print( class3.propertyPrint )

    class3.propertyPrint2 = 300
    print( class3.propertyPrint2 )
    
except:
	sys.exit('class test Errors !!')

print('aaa')