
import classFileName
from subClass.sub2 import classFileName2

class classExtendsName(classFileName.className, classFileName2.ClassName2):
    
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital
        classFileName2.ClassName2.__init__(self, -10, 10)
        
    def show(self):
        print(
            """
            국가의 이름은 {} 입니다.
            국가의 인구는 {} 입니다.
            국가의 수도는 {} 입니다.
            """.format(self.name, self.population, self.capital)
        )