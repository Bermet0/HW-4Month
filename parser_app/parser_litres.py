import requests
from bs4 import BeautifulSoup as bs
from django.views.decorators.csrf import csrf_exempt

URL = "https://www.litres.ru/"
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}


# start
@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


# get data
@csrf_exempt
def get_data(html):
    soup = bs(html, 'html.parser')
    items = soup.find_all('div', class_='ArtV2Default-module__container_3ymrO')
    litres_book = []

    for item in items:
        litres_book.append({
            "title_name": item.find("div", class_='ArtInfo-modules__wrapper_2lOpZ').get_text(),
            "description": item.find("div", class_='ArtRating-module__rating_1RpVb').get_text(),
            "image": URL + item.find('div', class_='AdaptiveCover-module__image_3rtyg').find('img').get('src')
        })

    return litres_book


# endparser
@csrf_exempt
def parser_litres():
    html = get_html(URL)
    if html.status_code == 200:
        litres_book_2 = []
        for page in range(0, 1):
            html = get_html(f'https://www.litres.ru/popular/', params=page)
            litres_book_2.extend(get_data(html.text))
        #return litres_book_2
        print(litres_book_2)

    else:
        raise Exception('Error in Parse')


parser_litres()
