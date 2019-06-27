#튜플 - 소괄호
#리스트와 같지만 요소(데이터) 수정 불가
#var = ('1', '2', '3')

sTuple = ("123", "최종효", "송효정", "최종효", "최종효2")

#길이 - len
print('len - ', len(sTuple))

#결합 - 기존튜플 + 새로운 튜플
print(sTuple + ("a", "b", "c"))

#슬라이싱 - [1:2] / '<' 인듯
print(sTuple[0:2]) 

#인덱스 검색 - index()
print(sTuple.index("최종효"))

#데이터 개수 찾기 : count()
print(sTuple.count("최종효"))

