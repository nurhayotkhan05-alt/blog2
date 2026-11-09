# requests
# venv - vertual muhit
# json

# venv - fayllarni muhitda ushlash uchun kutubxonalar bilan boglash uchun ishlatiladi
# venv = har bir vversiyada katta loyihalar ishlashini ta'minlab beraoladi
# python -m venv venv
# py -m venv venv
# venv ishlashi uchun: 
# venv\Scripts\activate
# ctrl + shift + p / venv

# pip install requests

# request - saytdagi malumotlarni o'qishga yordam beradi
# get operatori - ma;lumotlarni olishga yordam beradi
# json - ma'lumotlarni saqlaydi

import requests
import json

url = requests.get('https://jsonplaceholder.typicode.com/users')
# saytdagi ma'lumotlarni o'qib oldi
users = url.json()
# ma'lumolarni saqladi

# print(users)

json_data = []

for user in users:
    name = user['name']
    username = user['username']
    email = user['email']

    json_data.append({
        "name": name,
        "username" : username,
        "email" : email
    }
    )

# print(json_data)

with open("users.txt","w",encoding="utf-8") as f:
    json.dump(json_data,f,indent=4,ensure_ascii=False)