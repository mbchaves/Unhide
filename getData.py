from bs4 import BeautifulSoup

import requests

html = requests.get("https://milhapremiada.com/reserva-manual/2/64993351742").content

soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())