#리스트 - 대괄호
#배열과 비슷한 구조로 인덱스를 이용한 데이터 관리


sList = ["123","최종효","송효정"]

#전체 명단
print(sList)

#각각
print("인덱스0 : ", sList[0])
print("인덱스1 : ", sList[1])
print("인덱스2 : ", sList[2])

#리스트 갯수 - len
print("전체수 : ", len(sList))

#리스트 추가 - append()
sList.append("최종효2")
print("append - ", sList)

#리스트 삭제 - pop(idx) / idx생략가능
sList.pop(3)
print("pop - ", sList)

#리스트 연장 - extend(['', ''])
sList.extend(['최종효2', '송효정2'])
print("extend - ", sList)

#데이터 삽입 - insert()
sList.insert(0, "인서트 테스트")
print("insert - ", sList)

#특정 데이터 삭제 - remove() / 인덱스로 삭제할 수 없다. 무조건 값 입력
sList.remove("인서트 테스트")
print("remove - ", sList)

#전체 삭제 - clear()
#sList.clear()
#print(sList)

#정렬 - sort() reverse = Fasle(오름차순(default)) / True(내림차순) 
#문자열 / 숫자열 혼합되있을 경우 사용할 수 없다.
#동일한 문자열끼리만 가능하다
sList.sort()
print("sort - ", sList)

#데이터 역순 - reverse()
sList.reverse()
print("reverse - ", sList)

#데이터 슬라이싱 - [n:m]
print("슬라이싱1 - ", sList[1:2])
print("슬라이싱2 - ", sList[2])
print("슬라이싱3 - ", sList[:2])

