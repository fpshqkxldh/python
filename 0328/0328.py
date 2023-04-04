'''
sil = input("문자를 입력하세요 > M")
print(len(sil))

print(sil[0:5], sil[6:], sil[6:12])
print(sil[-12:-7], sil[-6:], sil[-6:0])

print("ab" + "\b" + "c")
print("hello \nworld")
print("aaaaa\vbbbbb\vcccccc")
print("aaaaa\"bbbbbb\"cccccc")
'''

str_var = "하하하하"
print(str_var.replace("하","호"))

str_var2 = "안녕하세요. 파이썬. 파이썬. 파이썬. 파이썬. 파이썬 수업입니다."
str_var3 = str_var2.replace("파이썬", "자바")
str_var4 = str_var2.replace("파이썬", "자바", 3)
print("str_var2 = ", str_var2)
print("str_var3 = ", str_var3)
print("str_var4 = ", str_var4)

num = input("실수를 적으세요 >> ")
ch_num = num.replace(".","")
sum = int(ch_num[0]) + int(ch_num[1]) + int(ch_num[2]) + int(ch_num[3]) + int(ch_num[4]) + int(ch_num[5])
print(sum)