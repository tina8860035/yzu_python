import sys
import traceback

x = 10
y = int(input('請輸入數字:'))
try:
    z = x / y
    print(z)
#except:
    print('錯誤!錯誤!')

except Exception as e:
    print('錯誤!錯誤!', e)
    print(e.__class__.__name__)
    cl, exc, tb = sys.exc_info()
    lastCallStack = traceback.extract_tb(tb)[-1]
    print(lastCallStack)  # 可抓出哪裡有錯，detail information
else:
    print(z)