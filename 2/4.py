mevalar = {
    "olma": 15000,
    "banan": 25000,
    "apelsin": 30000,
    "mandarin": 25000,
    "limon": 20000,
    "nok": 25000,
    "uzum": 30000,
    "anor": 25000,
}

try:
    meva = input("Meva nomini kiriting:")
    print(f"{meva}ning narxi: {mevalar[meva]}")
except KeyError:
    print(f"Bu nomdagi meva mavjud emas")