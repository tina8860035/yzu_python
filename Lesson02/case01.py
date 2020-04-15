# -*- coding:UTF-8 -*-
import keyword

print("我是中文")

if 2 > 0 :
    print("A")
    print("B")
else:
    print("C")
    print("D")
print("E")
a = 100
b = 0b100 #二進位
c = 0o12 #八進位
d = 0x12 #十六進制
print(a,b,c,d)

#型態
a = 10
b = 3.14
c = 1+2j
print(c,type(c))

#變數初始值
age,name = 18,'Tina'
print(age,name)

#布林值
check = True
print(check,type(check))
score = 55
mark = score >=60
print(mark,type(mark))

#保留字
kw = keyword.kwlist
print(kw)

#刪除變數
a = 10
print(a)
del a
print(a)


