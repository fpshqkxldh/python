# 튜플, 딕셔너리, 집합

# 리스트
# lst = []
# 수정, 삭제, 추가 등 여러가지가 가능

# 튜플
# 수정이 불가항목들
t1 = (1, 2, 3, 4)
print(t1)
t2 = tuple()
print(t2)
t3 = 1, 2, 3, 4, 5
print(type(t3))

print(t3.index(3))
print(t3.count(3))

t4 = 1, 2, 3, 4, 5, 3, 3, 10, 3
t5 = 100, 200, 300
print("t4 + t5 : ", t4 + t5)
print("t4 : ", t4)
print("t5 : ", t5)

# sorted는 원본을 바꾸지 않고 새롭게 만들어 정렬
# sort는 원본을 바꿔서 정렬
print("t4 : ", t4)
print(sorted(t4))
print("t4 : ", t4)


# dictionary
# key : value로 키에 값을 선언
# 1001 : "홍길동"

d1 = {1001 : "홍길동", 1002 : "김길동", 1003 : "박길동"}
print(d1[1001])
# print(d1[0]) 이렇게 실행하면 오류 발생 [] 안에는 키 값만 넣을 수 있음


# d2 = {}
# 강좌에 대한 dictionary
d2 = dict()
d2['강좌명'] = '파이썬'
d2['개설 요일'] = '화요일'
d2['년도'] = 2003
d2['수강생'] = ['김', '이', '박']
print("d2 : ", d2)
print(d2['수강생'])
print(len(d2))


# dictionary key:value 1:1월, 2:2월......
# for문을 돌려서 각각의 value 값을 찍어라
month = {1 : '1월', 2 : '2월', 3 : '3월', 4 : '4월', 5 : '5월', 6 : '6월', 7 : '7월', 8 : '8월', 9 : '9월', 10 : '10월', 11 : '11월', 12 : '12월'}
# for i in range(1, 13):
#     print(month[i])


# dictionary의 다양한 메소드
print("month.keys() : ", month.keys())
print("month.values() : ", month.values())
print("month.items() : ", month.items())


for i in month.keys():
    print("i : ", i)
    print(month[i])


for i in month.values():
    print(i)

for i in month.items():
    #print(i)
    print(i[1])


# month.items() 활용
print("month.item()")
for k,v in month.items():
    print(v)


# month.keys()라고 하지 않아도 month라고만 써도 가능
for i in month:
    print(i) # 키 값만 불러옴
    print(month[i]) # value 값을 불러옴



print("month.pop(1) : ", month.pop(1)) # key 값을 주고, 해당 item을 제거 
print(month)
print("month.popitem() : ", month.popitem()) # 제일 마지막 item을 제거
print(month)



# month.update()
month.update({3 : 'March'})
print(month)
month.update({15 : '15월'})
print(month)
# 원래 있는 키 값에 어떠한 새로운 아이템을 주더라도 따로 새롭게 생기지 않고 item만 변한다.
# 새로운 키값을 주고 item을 줘서 update를 하면 뒤에 키와 아이템이 추가된다.



# dictionay를 tuple-list로 변환
# tuple -> 변경불가, 수정X (아메리카노, 핫초코, 라떼)
# tuple -> list  유자차 추가 => tuple로 변경
# list -> tuple 수강 신청 전 수강생 변경
# tuple, list => dictionary


seql = ['a', 'b', 'c', 'd']
seqt = tuple(seql)
print(seqt)
print(type(seqt))


seql2 = list(seqt)
print(seql2)
print(type(seql2))


sqed = dict(enumerate(seql))
print(sqed)
print(type(sqed))



# zip
# list, tuple가 여러 개 => 튜플의 조합으로 된 히스트
l1 = ['1조', '2조', '3조']
YA = ['홍', '김', '이']
YB = ['최', '한', 'James']

z = zip(l1, YA, YB)
print(type(z))
print(z)
print(list(z))

print(tuple(zip(l1, YA, YB)))

#
l10 = ['한식', '양식', '중식', '분식']
l11 = ['전주식당', '닥터로빈', '취영루', '토마토']
l12 = ['제육', '파스타', '짬봉', '김밥']

print(list(zip(l10, l11, l12)))

for i in range(4):
    print(l10[i], l11[i], l12[i])

l100 = list(zip(l10, l11, l12))
for i in l100:
    print(i[0], i[1], i[2])

# 위에 리스트에 개수가 각각 다르게 주어지면 3개가 맞춰지는 것만 출력된다.

l101 = list(zip('ABCD', l10, l11, l12))
for i in l101:
    print(i[0], i[1], i[2], i[3])


#dictionary
l10 = ['한식', '양식', '중식', '분식']
l11 = ['전주식당', '닥터로빈', '취영루', '토마토']
l12 = ['제육', '파스타', '짬봉', '김밥']

print(list(zip(l10, l11)))
print(dict(zip(l10, l11))) # list를 세 개로 하면 오류가 난다.

# 세 개를 하는 방법은 뒤에 두 개를 묶어 아이템으로 만들어 주면된다.
print(dict(zip(l10, zip(l11, l12))))

# enumerate 숫자를 붙여주는 함수
print(list(enumerate(l11)))
print(dict(enumerate(l11)))



# EX
lst1 = ['파이썬', 'c언어', '자바', '웹프', '데이터베이스'] # 강의명
lst2 = [101, 102, 103, 104, 105] # 강의실

db = dict(zip(lst1, lst2))
while True:
    k = input("강의명을 입력하세요 >> ")
    if k == 'quit':
        break
    else:
        if k in db.keys():
            print(db[k])
        else:
            continue



