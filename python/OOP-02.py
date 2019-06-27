
#외부에서 접근 가능 - public
#외부에서 접근 불가능 - private
"""
    private 네이밍 규칙
    - 접두사 : __ 사용
    - 접미사 : _ 까지 허용
"""



class PayJh:
    def __init__(self):
        self.day = 5
        self.__money = 1000000

    def changeMoney(self, money):
        self.__money = money
    
    def getMoney(self):
        return self.__money



myJh = PayJh()

print(myJh.day)
#print(myJh.__money)
print(myJh.getMoney())
myJh.changeMoney(2000000)
print(myJh.getMoney())


"""
    객체의 생성은 __name__()함수(메서드, method)가 담당하고, 
    초기화는 __init__() 함수(메서드, method)가 담당한다.
    __init__()함수보다 __name__()함수가 먼저생성된다.
    아래의 예제의 doubleMajor는 클래스 변수이므로
    jh객체에도 자동적으로 추가되어 표현된다.( 순서에 따라 다를수 있음.)
"""
class Student:
    doubleMajor = []

    def __init__(self, name, age, gender, major):
        self.name = name
        self.age = age
        self.gender = gender
        self.major = major

    def printStudentInfo(self):
        print('name : {0}'.format(self.name))
        print('age : {0}'.format(self.age))
        print('gender : {0}'.format(self.gender))
        print('major : {0}'.format(self.major))
        print('doubleMj : {0}'.format(self.doubleMajor))

    def setDoubleMajor(self, doubleMajor):
        self.doubleMajor.append(doubleMajor)

jh = Student('최종효', '31', 'M', '컴공')
hj = Student('송효정', '28', 'F', '사학과')
hj.setDoubleMajor(['소비자심리', '유통'])
jh.printStudentInfo()
hj.printStudentInfo()


"""
    정적 메서드와 클래스 메서드
    정적 메서드 : @staticmethod
    클래스 메서드 : @classmethod
"""

#스태틱메소드는 객체를 생성하지 않고 바로 클래스로 접근 가능한 메소드
#staticmethod
class Earth:
    @staticmethod
    def getRadious():
        return 6400
    
    @staticmethod
    def getSurfaceArea():
        return 1111111111

print('Earth Radious : {0}'.format(Earth.getRadious()))
print('Earth SurfaceArea : {0}'.format(Earth.getSurfaceArea()))


#클래스 메소드는 객체가 생성되기 전에 클래스 영역에서 생성된 메소드
#데이터를 공유해서 사용할 수 있다.
#classmethod
class PopulationStatistics:
    population = 0

    def plusPop(self):
        PopulationStatistics.population += 1
    
    def minusPop(self):
        PopulationStatistics.population -= 1

    #cls는 객체가 아니라 클래스 자체를 가리킨다.
    @classmethod
    def getPop(cls):
        return cls.population

PopulationStatistics().plusPop()
PopulationStatistics().plusPop()
PopulationStatistics().plusPop()
print('1 {0}'.format(PopulationStatistics.getPop()))

PopulationStatistics().minusPop()
print('2 {0}'.format(PopulationStatistics.getPop()))







