fruits = ["apple","pear","strewbreey","banana"]

try:
    fruit = int(input("Meva turgan indsni kiriting: "))
    print(f"Bu meva bor! Nomi: {fruits[fruit]}")
except IndexError:
    print("Bu meva mavjud emas")