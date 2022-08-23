class ClassName2Sub:
    
    def __init__(self):
        pass
       
    @property
    def propertyPrint2(self):
                
        if self.aa > 0:
            res = '양수'
        elif self.aa < 0 :
            res = '음수'
        else : 
            res = '제로'
        
        print( 'ClassName2Sub > self.aa : ', self.aa )
        return(res)

    @propertyPrint2.setter
    def propertyPrint2(self, a):
        if a < 0:
            raise ValueError("Invalid age")
        self.aa = a