"""자료형"""
# 리스트
# 리스트 변수명 = [요소1, 요소2...], 요소에는 정수, 실수, 문자열, 리스트 포함 가능
listexample1= [1, 2, 3]
for i in listexample1:
 print(listexample1[i - 1]) # 1, 2, 3 출력됨
# 리스트 안에 리스트가 요소로 들어가 있을 경우
listexample2 = [1, 2, 3, ["I", "want", "goodlife"]]
print(listexample2[3][1]) # 3번째 요소인 ["I", "want", "goodlife"]에서 2번째 요소인 want 출력됨
# 슬라이싱 : listexample1[:3] = 1, 2, 3 출력
print(listexample1[:3]) # 슬라이싱 예제
# 리스트 연산 : listexample1 + listexample2 = [1, 2, 3, 1, 2, 3, ["I", "want", "goodlife"]
print(listexample1 + listexample2)
# 리스트 반복 : listexmaple1 * n(반복하고 싶은 횟수)
print(listexample1 * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]출력
# 리스트 수정 : 리스트 변수명[수정하고자 하는 요소번호] = 넣고자 하는 값
listexample1[2] = 5
print(listexample1) # 1, 2, 5 출력됨
# 리스트 삭제 : del 리스트 변수명[삭제하고자 하는 요소 번호]
del listexample1[2] # 2번째 요소 삭제
print(listexample1) # 5 삭제됨
# 요소 추가 리스트 변수명.append(추가하고자 하는 요소)
listexample1.append(3) # 2번째에 3 추가
print(listexample1) # 1, 2, 3 출력
# 리스트 정렬 : 리스트 변수명.sort()
listexample3 = [5, 1, 3, 2, 4] # 무작위
listexample3.sort() # 정렬
print(listexample3) # 1, 2, 3, 4, 5로 출력됨
# 리스트 역순 : 리스트 변수명.reverse()
listexample3.reverse()
print(listexample3) # 5, 4, 3, 2, 1로 출력됨
# 위치 반환 : 리스트 변수명.index(찾고자 하는 요소)
print(listexample3.index(3))
# 요소 삽입 : 리스트 변수명.insert(위치, 넣고자 하는 요소)
# 요소 제거 : 리스트 변수명.remove(위치)
listexample3.insert(3, 6)
print(listexample3) # 5, 4, 3, 6, 2, 1 출력
listexample3.remove(3)
print(listexample3) # 5, 4, 3, 2, 1 출력

# 튜플
# 리스트와 다른점 : 리스트는[,]이용. 튜플은 (,)이용
#                리스트는 생성, 삭제, 수정 가능하지만, 튜플은 안됨(고정값)
# 튜플 변수명 = (요소1, 요소2, 요소3...)
tupleexample1 = (1, 2, 3)
print(tupleexample1)
# 요소 삭제, 변경 제외하고 나머지는 리스트와 동일

# 딕셔너리
# 딕셔너리 변수명 = {key1 : value1, key2 : value2...}
dicexample = {"name" : "LKU", "age" : 25}
print(dicexample["name"], dicexample["age"])
# 딕셔너리 key리스트 만들기
# key리스트는 append, insert, remove, sort 수행 불가능
dicexample.keys()
print(dicexample.keys()) # dict_keys(['name', 'age']) 출력됨(반환됨)
# key리스트 속 객체들을 리스트로 변환 : list(dicexample.keys())
print(list(dicexample.keys())) # ['name', 'age'] 출력됨
# value 리스트 만들기 : dicexample.values()
print(dicexample.values()) # dict_values(['LKU', 25]) 출력됨(반환됨)
# key value 둘 다 반환 : dicexample.items()
print(dicexample.items()) # dict_items([('name', 'LKU'), ('age', 25)]) 출력됨(반환됨)
# key, value 둘 다 제거 : dicexample.clear()
# dicexample.clear()
# print(dicexample["name"], dicexample["age"]) 에러 발생

