"""기초"""
# 터미널에 출력하고 싶으면 print()를 써서 출력.
# 사칙연산
plus = 1 + 2 # 더하기, 값 : 3
minus = 3 - 2 # 빼기, 값 : 1
multiply = 3 * 4 # 곱하기 값 : 12
divide = 4 / 2 # 나누기, 값 : 2.0, 소숫점까지 출력되기때문에 float형식으로 출력, 정수값으로 출력하고 싶으면 int(divide)를 출력할때 사용하면 됨.
remainder = 4 % 3 # 나머지, 값 : 1
print("plus : ", plus,  ",minus : ", minus, ",multiply : ", multiply, ",divide : ", divide, ",remainder : ", remainder)

# 그 외에도
# 거듭제곱 : **, AND 연산자 : &, OR연산자 : |, XOR 연산자 : ^, 대소구분 : (<,>), 같음 : ==, 같지않음 !=,

# 변수에 숫자 대입 후 계산
one = 1
two = 2
# 더하기 : 3, 빼기 : -1, 곱하기 : 2, 나누기 : 0.5, 나머지 : 1 출력됨
print("\nplus : ", one + two,  ",minus : ", one - two, ",multiply : ", one * two, ",divide : ", one / two, ",remainder : ", one % two)
print("\n")

#변수에 문자 및 숫자 대입 후 출력
# (",")와 ('.')둘 다 사용가능. 단, 출력할때 (",")를 출력하고 싶으면 (',')사용, 그 반대의 경우엔 반대로 사용.
message = "Hello Python"
birthday = 19990724
print(message, birthday)
print("\n")

# 형변환 - int() : 정수형, float() : 실수형, str() : 문자열, chr() : 문자, bool() : 불리언
# 형태를 알아보고 싶을땐 type() 사용
trans = 1
print(type(int(trans)), type(float(trans)), type(str(trans)), type(chr(trans)), type(bool(trans)))
print(int(trans), float(trans), str(trans), chr(trans), bool(trans))
print("\n")
"""흐름 제어"""
# if() 조건문
# if(조건1): 식1... elif(조건2): 식2... else(조건 3): 식3...
Ifstatement = 3
if(Ifstatement > 1):
    print("if문","True")
elif(Ifstatement < 0):
    print("if문","False")
print("\n")

# for문
# for 변수 in 몇번 반복?: 조건...
# range(x, y) : x부터 y - 1까지의 값까지 도달
for i in range(1, 4):
    print("for문",i)
print("\n")

# while문
# while 조건: 식... (조건이 끝날때 까지 무한 반복)
whilex = 0
while whilex < 3:
    whilex += 1
    print("while 문",whilex)
print("\n")

# 함수
# def 함수명(입력값1, 입력값2):
def func(x, y):
    print("함수 예시", x + y)
# func(1, 2)써서 사용

# 탈출 코드
# \n : 줄바꿈, \t : 탭간격...

