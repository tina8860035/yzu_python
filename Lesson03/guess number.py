import random as r
ans = r.randint(1,99)
min = 0
max = 100
count = 7

while count > 0:
    guess = int(input("(%d次數)請輸入數字 %d ~ %d :" % (count, min, max)))
    count -= 1  # count = count-1
    # 先驗證輸入數字是否在範圍裡?
    if guess <= min or guess >=max:
        print('數字範圍錯誤, 請重新輸入 !')
        continue
    if guess == ans:
        print('恭喜你答對了')
        break;

    elif guess < ans:
        min = guess

    else:
        max = guess