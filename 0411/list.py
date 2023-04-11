# 리스트
# ['김', '이', '박', '최']
# 튜플
# ('김', '이', '박', '최')
# 딕셔너리 -> 사전
# {key: value, k1:v1, k2:v2........}
address = {'홍길동' : '서울', '김길동' : '부천', 'james' : '미국'}
print(address['홍길동'])


# list
lst = [10, 20, 30, 40, 50]
str_list = ['하', '호']
print(type(lst))
print(lst[0], " ", lst[1], " ", lst[len(lst) - 1])

# 빈리스트 생성 -> 하나씩 원소를 추가
list1 = []
print(list1)
list1.append("python")
list1.append("java")
list1.append("c++")
list1.append("python")
list1.append("python")
list1.append("python")
list1.append("python")
print(list1)

for i in list1:
    print(i)

for i in range(len(list1)):
    print(list1[i])

print(list1)
print("count : ", list1.count("python"))
print("index : ", list1.index("python"))


# 수정
list1[0] = "AI"
list1[2] = "IOT"
print(list1)

list2 = list1[0:3:1] # 0, 1, 2
print(list2)
list2 = list1[1:5:1] # 1, 2, 3, 4
print(list2)
list2 = list1[1:len(list1):1] # 1, 2, 3, 4, 5, 6
print(list2)
list2 = list1[2:6:3] # 2 5
print(list2)
list2 = list1[::-1] #
print(list2)

# list1의 일부를 list3에 대입
list2 = list1[2:6:3]
print(list2)
list3 = [1, 2, 3, 4, 5, 6, 7, 8]

list3[1:2] = list2
print(list3)

list3[1] = list2
print(list3)

# 튜플은 수정 불가 -> append, insert 등 값 변경 x

#list insert
food = []
food.append("짜장면")
food.append("샌드위치")
print(food)
food.insert(0, "파스타")
print(food)
food.insert(2, "제육")
print(food)

'''
food.remove("제육")
print(food)

print("food.pop: ", food.pop())
print(food)
print("food.pop: ", food.pop())
print(food)
'''

print(food)
dessert = ["커피", "케익", "와플"]

# 방법1
food.extend(dessert)
print(food)

# 방법2
food_list = food + dessert
print(food_list)

# del은 메모리에 저장되어 있는 변수 자체를 지워서 다시 접근하지 못하게 하는 것입니다.
# del로 정의한 변수를 print하면 정의되지 않는다며 오류가 발생
# del food
# print(food)

# reverse는 그 위치에 값을 아예 바꾸는 것이다.
print(food)
food.reverse()
print(food)


a = "1"
print(type(a))
print(int(a) + 5) # 잠깐 int형으로 변환해서 계산 후 원래 string으로 돌아감

# print(a + 5)
# 문자와 숫자는 더할 수 없기 떄문에 오류 발생

# sort()
# sorted()
l1 = ["banana", "apple", "orange", "mango"]
print(l1)
print("sorted(l1) : " , sorted(l1))
print("        l1 : ", l1)

l1.sort()
print(l1)


# 리스트 컴프리헨션
# 0 ~ 10까지 있는 list를 만들자
# 1)
l3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l3)

# 2)
l3 = []
for i in range(11):
    l3.append(i)
print(l3)

# 3)
# 리스트 변수명 = [i for i in range()]
l3 = [i for i in range(11)]
print(l3)



# 0 ~ 10까지 숫자의 제곱을 원소로 가지는 리스트를 작성(i**2)
ex1 = [i**2 for i in range(11)]
print(ex1)

# 0 ~ 10까지 숫자의 3배를 원소로 가지는 리스트를 작성(i**2)
ex2 = [i*3 for i in range(11)]
print(ex2)

# "hello"를 10개 가지는 리스트를 작성(i**2)
ex3 = ["hello" for i in range(10)]
print(ex3)

# 위에 코드와 같은 결과
'''
ex3_1 = []
for i in range(10):
    ex3_1.append("hello")
print(ex3_1)
'''

# 0 ~ 10 까지의 숫자의 제곱을 리스트로 만들어라
# 짝수만 제곱에 넣어라
ex4 = []
for i in range(11):
    if(i % 2 == 0):
        ex4.append(i**2)
print(ex4)

ex4_1 = [i**2 for i in range(11) if i % 2 == 0]
print(ex4_1)



# l2 = l1 은 같은 주소 값을 가리키기 때문에 다른 하나의 리스트를 변경하면 같이 변한다.
# 이를 얕은 복사라고 하고 shallow copy라고도 한다.
# l3에 l1이나 l2의와 같은 리스트에 다른 주소 값을 을 주어서 저장할 수 있다
# 이때는 l3를 변경해도 l1과 l2는 변하지 않는다. 이를 깊은 복사(deep copy)라고 한다.

# 얕은 복사
print("    food : ", food)
wishlist = food
print("wishlist : ", wishlist)

food.pop()
print("    food : ", food)
print("wishlist : ", wishlist)

print(food is wishlist)

# 깊은 복사
food2 = food[:]
food3 = list(food)

print("deep copy")
print(" food : ", food)
print("food2 : ", food2)
print(food is food2)

food2.append("김밥")
print(" food : ", food)
print("food2 : ", food2)

food.append("라뽁이")
print("    food : ", food)
print("wishlist : ", wishlist)
print("   food2 : ", food2)

