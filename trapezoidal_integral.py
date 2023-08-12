from math import sin
import math
math.pi

a = 0
b = 1
n = 100
h = 0

def f(a, b, n):
    h = (b - a) / n
    return((h/2) * (math.sin(a) + 2 * sum(math.sin(a + i*h) for i in range(1, n)) + math.sin(b)))

a = int(input("区間下限を入力"))
b = int(input("区間上限を入力"))
n = int(input("分割数を入力"))

result = f(a, b, n)
print(result)

#from math import sin
#import math

#a = 0
#b = math.pi/2
#n = 100
#h = (b - a) / n

#integral_approximation = (h/2) * (math.sin(a) + 2 * sum(math.sin(a + i*h) for i in range(1, n)) + math.sin(b))

#print(integral_approximation)
