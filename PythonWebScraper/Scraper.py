import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Fujifilm-Instax-Mini-Lime-Green/dp/B06X9C2696/ref=sr_1_12?crid=1J983Z2VSUV2K&dchild=1&keywords=polaroid+cameras&qid=1613288924&sprefix=polaroid+%2Caps%2C316&sr=8-12'
headers = {'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
page = requests.get(URL,headers=headers)

soup = BeautifulSoup(page.content,'html.parser')
print(soup.prettify())

try:
    price = soup.find(id='priceblock_ourprice').get_text()
    print(float(price))
except:
    pass
