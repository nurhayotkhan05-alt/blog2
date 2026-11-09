with open("ismlar.txt","r",encoding="utf-8") as f:
    ismlar = f.read()


print(ismlar.replace(" ","_"))