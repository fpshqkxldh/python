str = "파이썬은 파이썬은 파이썬은 파이썬은 파이썬은 파이썬은"
newstr = str.replace("파이썬","자바")
print("str: ", str)
print("newstr: ", newstr)

print("str.count('파이썬')", str.count("파이썬"))
print('->'.join(str))

print(str.find("파이썬"))
print(str.find("썬"))
print(str.find("자바"))
#print(str.index("자바"))
#특정 단어를 찾을 때 index는 구동하지 않고 오류를 발생시켜서 프로그램을 멈추는 역할을 합니다.

print(str.split())

print('{} + {} = {}'.format(2,3,5))

a,b = 5, 10
print('{} + {} = {}'.format(a,b,a+b))
print('{0} + {1} = {2}'.format(a,b,a+b))
print('{2} + {0} = {1}'.format(a,b,a+b))

c,d = 5, 10.000
print('{0:d} + {1:f} = {2:f},{3:s}'.format(c,d,c+d,"hihihi"))
#

value = True
print(type(value))
print(int(value))

print(bool(0), bool(1), bool(1.1222), bool(-12))
print(bool("python"), bool("-1"), bool(""))
print('bool("") = ', bool(""))
#bool안에 어떤 수나 문자를 넣더라도 True가 나오고 아무것도 넣어주지 않거나 0을 넣어주면 False가 나온다.

