try:
    a = int(input("a = "))
    b = int(input("b = "))
    print(a // b)

except ValueError:
    print("Not'g'ri qiymat kiritdingiz!")
except ZeroDivisionError:
    print("Son no'lga bo'lish mumkin emas!")