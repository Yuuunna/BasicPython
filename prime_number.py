a = input("aの値を入力: ")
b = input("bの値を入力: ")

if int(a) <= 1:
    print("False")
else:
    for i in range(2, int(int(a) ** 0.5) + 1):
        if int(a) % i == 0:
            print(a + "は素数でない")
            break
    else:
        print(a + "は素数である")

if int(b) <= 1:
    print("False")
else:
    for i in range(2, int(int(b) ** 0.5) + 1):
        if int(b) % i == 0:
            print(b + "は素数でない")
            break
    else:
        print(b + "は素数である")