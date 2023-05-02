# 함수
# input을 주면 output이 나오는 것

'''
input - 숫자 - num1
output = 숫자 - output_num
이런 기능을 하는 function  - multi
'''

# 3을 곱하는 함수 정의
def multi(num1):
    output_num = num1 * 3
    return output_num

# 정의한 함수 호출
print(multi(10))

# 정의한 함수를 호출하는 것은 반드시 함수를 정의한 다음에 함수를 호출해줘야 한다


# hello, input - 사람이름 두 개 입력
# output - 안녕 1번 사람, 안녕 2번 사람

def hello(n1 = "홍", n2 = "김"):
    print("안녕 ", n1, " 안녕 ", n2)


print("기본값")
hello()
print("세팅값")
hello("박지성", "데이비드 베컴")


# 두 수를 입력받아 두 숫자의 합 출력
def sum(num1, num2):
    print("두 수의 합은 : ", num1 + num2)

sum(100, 2000)

def sum1(num1 , num2):
    return num1 + num2

print(sum1(100, 3000))

res = sum1(100, 4000)
print(res)


# 지역 변수, 전역 변수
 # 1)
num = 100
print("num: ", num) # 100

def addone():
    num = 10
    print("addone() ", num + 1) # 11
    print("addone() num : ", num) # 10
    num = num * 8 + 20
    return num

addone()
print("num : ", num) # 100

result1 = addone()
print("num : ", result1)

 # 2)
num1 = 100
print("num1 : ", num1) # 100

def addone1():
    print("addone() ", num1 + 1) # 101
    print("addone() num1 : ", num1) # 100
    # 내부에서 변경 x

addone1()
print("num1 : ", num1) # 100

 # 3) 내부 함수에서 전역 변수를 사용하면 좋겠고 수정도 하고싶고
 # 함수가 끝나도 반영 가능
num2 = 100
print("num2 : ", num2) # 100

def addone2():
    global num2
    num2 = num2 + 1

print("num2 : ", num2) # 100


# 인자의 개수 여러 개인 경우
print()
print(1,2,3,4,5,6,7,8,9)
print()

def hello2(*names):
    for i in names:
        print("hello ", i)

hello2("홍길동", "박지성", "데이비드 베컴", "손흥민")

#합을 구하는 함수
def ssum(*number):
    result = 0
    for i in number:
        result = result + i
    return result

print("합 : ", ssum(1,2,3,4,5,6,7,8,9))
lst1 = [1,2,3,4,5,6,7,8,9]
print(ssum(*lst1))

coffee = {"아메" : 2000, "라떼" : 3000, "티" : 2500}

def printmenu(**keyvalue):
    for key in keyvalue:
        print(key, keyvalue[key])

printmenu(**coffee)
printmenu(아메 = 2000, 라떼 = 3000, 티 = 2500, 핫초코 = 4000, 핫도그 = 3000)

def func1(*num, **menu):
    result = 0
    for n in num:
        result = result + n
    print(result)

    for key in menu:
        print(key, menu[key])

coffee = {"아메" : 2000, "라떼" : 3000, "티" : 2500}
lst1 = [1,2,3,4,5,6,7,8,9]

func1(1,12,4,5,6,6,7,83,아메 = 2000, 라떼 = 3000, 티 = 2500)
func1(*lst1, **coffee)
func1(1,12,4,5,6,6,7,83,**coffee)


# 람다 함수
# 함수를 만드는데, 이름짖기가 귀찮다. 실행문이 하나밖에 없다.

def addlam(x):
    return x + 1

print(addlam(100))

# lambda 파라메터 이름 : 파라메터로 실행하는 문
print((lambda x : x +1)(100))

def mysum1(num1, num2):
    return num1 + num2

print(mysum1(100, 1000))

print((lambda num1, num2 : num1 + num2)(100, 1000))


# map, filter
# 리스트가 존재할 때

# map(함수 , input 리스트)
# map(람다함수, input 리스트)

lst1 = [1,2,3,4,5,6,7,8,9]
print(list(map(lambda x : x + 1 , lst1)))

# lambda num1, num2 : num1 + num2
lst1 = [1,2,3,4,5,6,7,8,9]
lst2 = [12,23,3,54,65,6,72,8,9]

print(list(map(lambda num1, num2: num1 + num2,lst1,lst2)))