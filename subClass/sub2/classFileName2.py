
from subClass.sub2 import classFileName2sub

class ClassName2(classFileName2sub.ClassName2Sub):
    
    def __init__(self, a, b):
        self.aa = a
        self.bb = b
        
    def print(self):
        print( "subClass > ClassName2 ", self.aa , " / " , self.bb )
        
    @property
    def propertyPrint(self):
                
        if self.aa > 0:
            res = '양수'
        elif self.aa < 0 :
            res = '음수'
        else : 
            res = '제로'
        
        print( 'self.aa : ', self.aa )
        return(res)