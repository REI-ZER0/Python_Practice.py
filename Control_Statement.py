"""제어문 """
# if 문 : if 조건문: ~ 수행문1... elif 조건문: ~ 수행문2... else 조건문: ~수행문3...(조건문 앞 콜론 필요)
# 조건문에서 비교연산자(>, <, ==, <=, >=), 논리연산자(and, or, not)사용 가능
ifexample = True
if ifexample == True:
    print("Go")
    print("Ride")
    print("Taxi")
elif ifexample == False:
    print("Go")
    print("Ride")
    print("Subway")
    # print("Now") // 들여쓰기 하면 실행 안됨
# in : x in 리스트, 튜플, 문자열 = x가 리스트 or 튜플 or 문자열 안에 있는가?
# not in : x not in 리스트, 튜플, 문자열 = x가 리스트 or 튜플 or 문자열 안에 없는가?
# in과 not in 둘 다 if문 사용 가능

# while문 : while 조건문: ~ 수행문1, 수행문2...
# 조건문의 조건이 충족되거나 바뀌면 탈출
whileexample = 0
while whileexample <= 10: # whileexample이 10을 초과하면 while문 탈출
    print("Hit the Tree Count : ", whileexample)
    whileexample += 1
# 강제탈출은 break문 사용
coffee = 10
money = 30
while money:
    print("커피값은 10원 입니다")
    money -= coffee
    print("잔여금액은", money,"입니다.")

    if money == 0:
        print("돈이 없어 커피를 구매하실수 없습니다")
        break

