try:
    file = input("Faylni nomini kiriting: ")
    with open(file,"r",encoding="utf-8") as f:
        mf = f.read()
        print(mf)
except FileNotFoundError:
    print("Bunday nomdagi fayl mavjud emas!")