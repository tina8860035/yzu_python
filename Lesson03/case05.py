def mask(money):
    x = money // 5
    size = "成人"
    return x, size

my_x, my_size = mask(120)
print(my_x, my_size)
