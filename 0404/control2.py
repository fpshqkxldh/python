# continue, break
# 반복문 중간에 반복을 더이상 하지 않고 실행을 종료
# 반복문 안쪽에서 실행된다
# 주로 if문 안쪽에서 사용됨

# input으로 입력받는데 무한 반복
# exit이라는 값을 만나면 프로그램 종료
'''
while True:
    word = input("단어를 입력하세요 : ")
    if word == "exit":
        print("종료 단어를 입력 받았습니다. ", word)
        break
    else:
        if word == "apple":
            print("continue를 입력 받았습니다.")
            print("continue 실행 중~~~~~")
            continue
        print("입력한 단어는 : ", word)

    print("저는 아직 while문 안에 있습니다.")

print("수업 종료 과제")
'''
# input으로 입력받는데 무한 반복
# exit이라는 값을 만나면 프로그램 종료
# apple을 받으면 "apple을 입력했다."하고 다시 입력
# 그 외는 해당 단어를 세 번 출력
# continue, break 활용


while True:
    text = input("단어를 입력하세요> ")
    if text == "exit":
        print("종료 단어를 입력 받았습니다. ", text)
        break
    elif text == "apple":
        print("apple을 입력했다")
        continue
    else:
        for i in range(3):
            print(text, end= " ")
    print("저는 아직 while문 안에 있어요~~~~~")

print("수업과제 종료")