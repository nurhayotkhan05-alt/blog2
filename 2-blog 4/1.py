from countryinfo import CountryInfo
import json

Country_data = []

while True:
    Country_name = input("Davlat nomini kiriting: ").lower()
    if Country_name == "stop":
        print("Dastur to'xtatildi!")

        with open("country_information.txt","a",encoding="utf-8") as f:
            json.dump(Country_data,f,indent=4,ensure_ascii=False)
            break

    try:
        get_country = CountryInfo(Country_name)
        data = get_country.info()

        # print(data)

        name = data['name']
        area = data['area']
        capital = data['capital']
        population = data['population']

        print(f"Davlat nomi: {name}\n"
              f"Hududi: {area}\n"
              f"Poytaxti: {capital}\n"
              f"Aholi soni: {population}\n")

        Country_data.append({
            "name" : name,
            "area": area,
            "capital" : capital,
            "population" : population
        }
        )

    except:
        print("Siz kiritgan nom bo'yicha davlat topilmadi!")