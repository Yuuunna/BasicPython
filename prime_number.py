def prime_number(n):
    if int(n) <= 1:
        print("False")
    else:
        for i in range(2, int(int(n) ** 0.5) + 1):
            if int(n) % i == 0:
                print(n + "は素数でない")
                break
        else:
            print(n + "は素数である")

n = input("nの値を入力: ")
prime_number(n)


#制御構文課題
#a = input("aの値を入力: ")
#b = input("bの値を入力: ")

#if int(a) <= 1:
    #print("False")
#else:
    #for i in range(2, int(int(a) ** 0.5) + 1):
        #if int(a) % i == 0:
            #print(a + "は素数でない")
            #break
    #else:
        #print(a + "は素数である")

#if int(b) <= 1:
    #print("False")
#else:
    #for i in range(2, int(int(b) ** 0.5) + 1):
        #if int(b) % i == 0:
            #print(b + "は素数でない")
            #break
    #else:
        #print(b + "は素数である")