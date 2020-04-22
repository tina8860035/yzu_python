s = "she sell sea shell on the shore"
print(s)
print("有 %s 個" % s.count('s'))
print("有 sea 這個字嗎? %d" % s.find('sea'))

#是否都是0-9A-Za-z
#技巧: 先利用replace 去除空白
print(s.replace(' ', ' ').isalpha())

print(s.swapcace())