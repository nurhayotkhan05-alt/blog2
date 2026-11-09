import requests
import json

url = requests.get("https://jsonplaceholder.typicode.com/comments")
commants = url.json()

# print(commants)

json_data = []
for commant in commants:
    name = commant["name"]
    email = commant['email']

    json_data.append({
        'name':name,
        'email':email
    })


# print(json_data)

with open('commants.txt','w',encoding="utf-8") as f:
    json.dump(json_data,f,indent=4)
