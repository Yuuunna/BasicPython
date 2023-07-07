from math import sin
import math

a = 0
b = math.pi/2
n = 100
h = (b - a) / n

integral_approximation = (h/2) * (math.sin(a) + 2 * sum(math.sin(a + i*h) for i in range(1, n)) + math.sin(b))

print(integral_approximation)
