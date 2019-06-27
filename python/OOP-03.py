"""
    상속
    -부모클래스의 속성을 자식 클래스에서 사용
    -public으로 정의된것은 다가져올수있다.
    -private은 가져오지 못한다.
"""
#inheritance
class ParentClass:
    def __init__(self):
        self.at1 = 'python'
        self.at2 = 'java'
        self.at3 = 'c++'

    def printAt(self):
        print(self.at1)
        print(self.at2)
        print(self.at3)

    def printMethod(self):
        print('Hello python')

#파이썬도 다중 상속 가능 class명(a,b,c):
#java같은 경우에는 상속을 하면 부모 클래스의 변수까지 사용이 가능하나,
#Python같은 경우에는 사용이 불가능하다, 그래서 강제로 부모 클래스를 초기화(가져와야?)해야 한다.
class ChildClass(ParentClass):
    def __init__(self):
        ParentClass.__init__(self)
        pass

cc = ChildClass()
cc.printMethod()
cc.printAt()


#오버라이딩
#부모클래스의 기능을 자식 클래스에서 재정의 할 수 있다.
#overriding
class ParentClass2:
    def __init__(self):
        pass

    def cooking(self):
        print('make Pizza')

class ChildClass2(ParentClass2):
    def __init__(self):
        pass

    def cooking(self):
        print('make Pasta')

cc2 = ChildClass2()
cc2.cooking()


#다중상속
#자식클래스에서는 부모클래스 여러개를 받을 수 있다.
class ParentCls1:
    def __init__(self):
        pass

    def clsMethod1(self):
        print("clsMethod1")

class ParentCls2:
    def __init__(self):
        pass

    def clsMethod2(self):
        print("clsMethod2")

class ParentCls3:
    def __init__(self):
        pass

    def clsMethod3(self):
        print("clsMethod3")

class ChildCls(ParentCls1, ParentCls2, ParentCls3):
    def __init__(self):
        pass

cc3 = ChildCls()
cc3.clsMethod1()
cc3.clsMethod2()
cc3.clsMethod3()


#추상클래스
#자식클래스에서 반드시 구현해야 되는 기능을 가진 부모 클래스이다.
#자식클래스에 반드시 내려줘야 하는 기능이 있을떄 사용

#Abstract Class(추상클래스)

from abc import ABCMeta
from abc import abstractmethod
class Calculator(metaclass=ABCMeta):
    def __init__(self):
        pass
    
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass

class SmartCalculator(Calculator):
    def __init__(self):
        pass
    
    def add(self):
        print('add')

    def sub(self):
        print('sub')

sc = SmartCalculator()
sc.add()
sc.sub()

#super
#부모클래스를 가리킨다.

#1 위에서 사용한 방법
class ChildClass(ParentClass):
    def __init__(self):
        ParentClass.__init__(self)
        pass

cc = ChildClass()
cc.printMethod()
cc.printAt()

#2 super()함수를 사용한 방법
class ParentCls4:
    def __init__(self):
        self.word = 'python'

class ChildCls4(ParentCls4):
    #위에서는 부모클래스명 자체를 사용하고 self변수까지 주었었는데,
    #super()함수를 사용하면 self변수를 줄 필요없다.
    def __init__(self):
        super().__init__()

cc4 = ChildCls4()
print(cc4.word)


