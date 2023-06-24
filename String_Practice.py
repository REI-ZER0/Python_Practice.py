"""문자열 연습"""
head = "Python"
tail = " Is Fun"
String = "Life is too short, You need Python"
print(head +  tail) # 문자열 2개 더해서 출력
print(head * 2) # 같은 문장 n번 곱해서 출력
print(len(head)) # len() 이용하여 문장 길이 출력

# 문자열 인덱싱과 슬라이싱
print(String[3]) # String 변수 문자열에서 4번째 문장 출력(0부터 세서 0, 1, 2, 3)
print(String[-1]) # 가장 끝 글자인 n 출력
print(String[0:4]) # 0부터 4번째 글자까지만 출력(Life), [시작되는 문자 번호 : 끝나는 문자 번호]
print(String[:4]) # 0부터 4번째 글자까지만 출력(Life), 각 문자 번호가 비어있으면 처음부터 시작되거나 끝까지 출력됨.

# 문자열 포메팅
# 바로대입
print("I wanner %d won" % 100000000000) # 숫자 바로 대입
print("\nI wanner %s" % "Happy Life") # 문자열 바로 대입
# 변수로 대입
life = "Happy Seoul Life"
money = 100000000
print("\nI wanner %s" %life) # 변수로 문자열 대입
print("\nI wanner %d money and %s" %(money, life)) # 2개 이상의 변수 대입 방법

""" 문자열 포맷 코드
%d : 정수
%c : 문자
%s : 문자열
%f : 실수
%% : % """



