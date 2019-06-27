#module
import parts

#필요한 함수만 가져와서 사용할 수 있다.
#from parts import addHandle
#from parts import addDoor
#from parts import *
#이렇게 가져오면 변수명(파일명). 은 안붙여도 된다.
#addHandle()

part = 4

for i in range(0, part, 1):
    parts.addHandle()

#패키지의 대상폴더에는 __init__.py 파일이 꼭 있어야한다.
#아무런 내용이 없는.. 지금까지는 아무런 내용이 없는 init파일이다.
#20190622없어도 실행이되는데..;?
from cookPackage import koreaCooking, chinaCooking

chinaCooking.makeJjajang()
koreaCooking.makeRice()

#패키지 추가하기
'''
import sys
for path in sys.path:
    print(path)
'''
from userPackage import *

