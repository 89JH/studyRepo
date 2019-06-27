#객체지향프로그래밍 - 01
#클래스이름 : 일반적으로 대문자로 시작

class Calculator:
    def __init__(self):
        self.color = "black"
        self.result = 0


    def plus(self):
        return

    def minus(self):
        return


class Bike:
    #생성자 - self는 파이썬 인터프리터에서 자동으로 인식한다
    #속성
    def __init__(self):
        self.color = "black"
        self.weight = 3
        self.height = 2

    #기능(메소드)
    def drive(self):
        print("drive")

    def brake(self):
        print("brake")

    def gear(self):
        print("gear")

#객체생성
myBike = Bike()
print(myBike.color)

#객체생성
myBike2 = Bike()
myBike2.color = "red"
print(myBike2.color)

myBike2.drive()
myBike2.brake()


#객체생성
myBike3 = Bike()




