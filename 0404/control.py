#제어문

'''
if 조건 : 
    실행문
else if = elif
elif 조건 :
    실행문1
else:
    실행문2    
'''

hour = 11
if hour < 12 :
    print("12시가 지나지 않아서 오전입니다.")
elif hour < 18 :
    print("아직 12 ~ 18시 사이이므로 저녁이 아닙니다.")
else : 
    print("18시가 지나 저녁입니다.")

# score < 200 50만원을 줌
# 200 <= score < 400 100만원
# 400 <= score < 500 10000만원
'''
score_str = input("점수는? ")
score = int(score_str)
if score < 200 :
    print("50만원 획득")
elif score < 400 :
    print("100만원 획득")
else : 
    print("10000만원 획득")
'''
#점심식사
'''
print("점심시간입니다~~~~~~~")
answer = input("서브웨이 먹을래? ")
if answer == "yes" :
    print("8호관 1층으로 오세요")
elif answer == "no" :
    again_answer = input("학식은 어때? ")
    if again_answer == "yes" :
        print("8호관 3층으로 오세요")
    else :
        print("오늘 점심은 먹지 않는다구요? 알겠습니다.")
'''
#반목문
#for
print("EX1")
for i in 1,3,4,5,6,7 :
    print(i)

print("range1")
for i in range(1,10,2) :
    print(i)

print("range2")
for i in range(10):
    print(i)

print("range sum")
sum = 0
for i in range(10):
    sum += i

else:
    print("for문의 조건이 더이상 만족하지 않습니다.")
    print("i가 range(11)에서 벗어남")
    print("for문이 breaksk countiue로 종료된게 아니라 정상 종료시에만 실행")

print("sum: ", sum)


#while문

i = 10
while i > 5:
    print(i,"는 5보다 큽니다.")
    i = i -1

# n = 1 부터 5까지 찍어내는 프로그래밍
# 1 2 3 4 5

i = 1
while i <= 5:
    print(i, end= ' ')
    i = i + 1
else:
    print("while이 잘 끝났습니다.")
    print("현재 i의 값은 ", i, "입니다.")


# 놀이기구 탑습
# 4명 탑승 가능, 5명 안됨
# 키 150이상인 사람만 탐승 가능
# 입력을 키를 받음
# 탑승인원 체크, 키 체크
# while문을 끝내는 조건은? 사람이 4명을 채웠는가

p = 0
while p < 4:
    height = input("키가 몇인가요> ")
    height_c = int(height)
    if height_c >= 150:
        p = p + 1
        print("한명 탑승")
        print("현재 탑승 인원: ", p)
    else:
        print("탑승이 불가 다음 사람")

else:
    print("4명 모두 탑승이 완료")
    print("놀이기구가 출발합니다.")