# 튜플, 딕셔너리, 집합

# 리스트
lst = []
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