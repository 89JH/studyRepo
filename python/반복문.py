#반복문
#range(시작, 끝, 증가값)
#container형(list, tuple, dictionory)
#for i container형

#구구단
for i in range(2, 10, 1):
    for j in range(1, 10, 1):
        print("{0} * {1} = {2}".format(i, j, i*j))

"""
sList = ["a", "hello", 123, 31.4]

for i in sList:
    print(i)

sTuple = ("a", "hello", 456, 31.4)

for i in sTuple:
    print(i)

sDic = {"홍길동":20, "홍길자":40, "홍길순":30}

for i in sDic:
    print(i)
    print(sDic[i])
    print('{0} : {1}'.format(i, sDic[i]))
"""

count = 0
target = 100
sum = 0

while count <= target:
    sum = sum + count
    count = count + 1

print('0부터 {0}까지의 합 - {1}'.format(target, sum))

for i in range(10):
    #짝수만 출력 i % 2 == 1 -> 홀수만 continue
    if(i % 2 == 1):
        continue
    print(i)

for i in range(10):
    if(i > 5):
        break
    print(i)






