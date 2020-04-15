# -*- coding:UTF-8 -*-
import random

#轉型態
a = "100"
b = "90"
c = "0.5"
print(a+b)
print(int(a)+int(b)+float(c))

score = 95
print(("成績=")+str(score))

#隨機亂數
r = random.randrange(1, 50)
print(r)
a = random.randint(1, 50, 2)
print(a)
