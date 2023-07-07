def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

result = gcd(a, b)
print(result)