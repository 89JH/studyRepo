#파일 읽기 쓰기
#경로를 지정하지 않으면?
''''
파이썬은 파일을 읽거나 쓸때

열기        파일객체 ex) f = open('파일경로', '타입(w(쓰기)/r(읽기))')
ㅣ
읽기/쓰기   파일객체.write('파일에 입력할 내용') ex) f.write('테스트파일')
ㅣ          파일객체.read()
ㅣ
닫기        파일객체.close() ex) f.close()        

형식이되어야 한다.

'''
'''
f = open('D:/pythonFildRW/testFile.txt', 'a')
f.write('\n파이썬입출력테스트333')
f.close()
'''

'''
f = open('D:/pythonFildRW/testFile.txt', 'r')

print('f.read() : {0}'.format(f.read()))
f.close()
'''
#파일모드란? 파일을 다루는 방식
#open(파일이름,파일열기모드)
#r - 읽기전용
#w - 쓰기전용(이미 존재하면 덮어씌움)
#a - 쓰기전용(이미 존재하면 덧붙임)
#x - 이미존재하면 예외(IOError) 발생

#텍스트 읽기 / 쓰기
'''
닫을 필요가 없음 (with ~ as)

리스트 문자열 쓰기 (객체.writelines())

모든문자열 읽기 (객체.readLines) / 행 단위로 문자열 읽기(객체.readline())
'''
'''
with open('D:/pythonFildRW/testFile.txt', 'r') as f:
    print('f.read() : {0}'.format(f.read()))
'''

fl = ['hello python\n', 'hello java\n', 'hello js\n']

'''
with open('D:/pythonFildRW/txtLine.txt', 'w') as f:
    for tl in fl:
        f.write(tl)

with open('D:/pythonFildRW/writeLines.txt', 'w') as f:
    f.writelines(fl)


with open('D:/pythonFildRW/writeLines.txt', 'r') as f:
    ls = f.readlines()
    #type(데이터가 반환되는 타입)
    print('f.readlines(fl) {0}'.format(type(fl)))

    l = ''
    for l in ls:
        print(l, end='')
'''

with open('D:/pythonFildRW/writeLines.txt', 'r') as f:
    l = f.readline()
    print('type(l) : {0}'.format(type(l)))

    cnt = 1

    while l != '':
        print(l, end = '')
        l = f.readline()
        cnt += 1

    print('cnt-1 : {0}'.format(cnt-1))
    


