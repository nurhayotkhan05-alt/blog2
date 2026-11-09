import json
import requests
# pip install BeautifulSoup
# pip install beautifulsoup4
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


def pars_texno(category):
    texno_data = []
    load_dotenv()

    URL = os.getenv("URL")
    HOST = os.getenv("HOST")

    HEADERS = {
        "USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"

    }

    html = requests.get(URL + category,headers=HEADERS).text
    soup = BeautifulSoup(html,"html.parser")

    blocks = soup.find_all('div',class_='col-3')

    # print(blocks)

    for block in blocks:
        image_link = block.find('a',class_="product-link")
        images = image_link.find('img').get('data-src')
        title = block.find('h2').get_text()
        price = block.find('div',class_='product-price__current').get_text(strip=True)

        texno_data.append({
            "images": images,
            "title": title,
            'price': price
        })

    with open('smartphone.json','w',encoding='utf-8') as f:
        json.dump(texno_data,f,indent=4)

pars_texno('katalog/smartfony/')