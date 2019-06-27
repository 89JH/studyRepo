#함수
#def 함수명(변수(생략가능)):

def myFun():
    print('Hello python')

myFun()

def myFun2(str):
    print(str)

myFun2("Hello python2")
myFun2("Hello JAVA")
myFun2("Hello nexacro")

def myFun3(var1, var2):
    for i in range(var2):
        print('{1} 번째 {0}'.format(var1, i))

myFun3("Hello python", 5)


def myFun4(var1, var2, var3, var4):
    print("{0}, {1}, {2}, {3}".format(var1, var2, var3, var4))

myFun4("i", "am", "python", "developer")

def myFun5(var1, var2):
    return var1 * var2

result = myFun5(100, 200)
print(result)


result = 10
print('result : {0}'.format(result))

def myFun6(var1, var2):
    result = var1 + var2
    print('result : {0}'.format(result))
    return result

print('myFun6 result : {0}'.format(myFun6(10, 100)))    
print('result : {0}'.format(result))





