def check_score(score):
    return "pass" if score >= 60 else "fail"

max = lambda x, y : x if x > y else y
print("max=", max(70, 20))
print(check_score(max(70, 20)))

bmi = lambda h, w : w / (h/100)**2
print("bmi=", bmi(170, 60))

weather = lambda : print("24.5度")
weather()

def hello():
    print('hello')

def calc(x, y):
    return x + y

f1 = lambda : hello()
f2 = lambda x, y : calc(x, y)

f1()
print(f2(3,5))