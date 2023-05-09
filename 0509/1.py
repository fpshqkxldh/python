# 모듈의 이해와 활용
# import로 다른 모듈을 불러옴
# sys는 기본으로 제공하는 것이기에 그냥 사용이 가능하지만 
# 다른 회사가 만든 것들은(numpy 등) 먼저 설치하여야지만 사용이 가능하다
# pip install numpy를 통해서 다운받는다.

import sys
print(sys.builtin_module_names)

import numpy as np
import math
# from math import gcd
# 이렇게 하면 math에서 gcd만 불러올 수 있다. ','를 통해서 여러 개를 불러올 수도 있음
# 이 때 사용시 math.gcd를 하지 않아도 되고 gcd(10,20)으로 바로 사용이 가능

np.array([1,2,3,4,5])
print(type(np.array([1,2,3,4,5])))

arrA = np.array([1,2,3,4,5])
arrB = np.array([6,7,8,9,10])

print(arrA + arrB) 
# -,*,/ 도 사용 가능

print(math.fsum([1,2,3]))
print(math.gcd(10,20))
print(math.ceil(5.333))


# 나만의 메소드 만들기
# 내 메소드 활용

import hello as h

print("==================")
h.helloworld()
# hello 메소드에 있는 내용 전부를 출력 후에 h.helloworld()를 실행해서 'hello world!!' 두번 나온다.
# name이라는 값을 원래 메소드 안에서 출력하면 main이라고 나오지만  여기서 실행하면 hello가 나온다.
# 이를 이용해서 hello 메소드에서 조건을 주어 다른 곳에서는 출력이 되지 않게할 수 있다.

print("__name__ in 1.py : ", __name__)



# 다른 파일에 있는 메소드 불러오기
from hong.ai import helloai
helloai.helloworld()
