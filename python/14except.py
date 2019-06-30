"""
#예외처리 try / except
try:
    userData = int(input('0 이상의 숫자를 입력하세요-'))
    result = int(10 / userData)
    print('result : {0}'.format(result))

except:
    print('Sorry~~')


#else: / finally:
#예외가 발생하지 않으면 else문 실행
#예외 발생 여부에 상관없이 finally문 실행

try:
    userData = int(input('(try)0 이상의 숫자 입력-'))
    result = int(10/userData)
except:
    print('(except)Sorry~~')
else:
    print('(else)정상적으로 입력되었습니다.')
finally:
    print('(finally)여기는 항상실행')


#Exception 클래스
#모든 예외 클래스는 Exception에 종속(?) 되어있다.
#모든 예외 클래스는 Exception클래스의 자식클래스
try:
    userData = int(input('0이상의 숫자입력-'))
    result = int(10/userData)
except ZeroDivisionError as e: #0 나누기 에러 발생했을때만 처리 하는 exception
    print('ZeroDivisionError 예외 발생 : {0}'.format(e))
except Exception as e: #숫자가 아닌 다른 것이 들어 왓을때만 발생하는 exception
    print('Exception 예외 발생 : {0}'.format(e))
except: #모든 에러 처리
    print('모든 Exception 처리 : {0}'.format(result))
"""

#사용자 Exception 클래스(사용자 정의 함수)
class myException(Exception):
    def __init__(self, e):
        super().__init__('{0}으로 나눌수 없습니다.'.format(e))

def division(x,y):
    if(y != 0):
        return x/y
    else:
        #사용자가 만든 Exeption을 보여주겠다 할때 사용하는 keyword(함수) - raise
        raise myException(y)

try:
    numX = int(input('x값-'))
    numY = int(input('y값-'))
    result = division(numX, numY)
    print('result : {0}'.format(result))

except myException as e:
    print('예외 발생 : {0}'.format(e))
else:
    print('정상실행')
finally:
    print('자원해제')


