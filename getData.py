from bs4 import BeautifulSoup

import requests

#url_get = "https://milhapremiada.com/reserva-manual/2/64993351742"
#url_get ="https://milhapremiada.com/sorteio/3-mil-reais-no-pix?"
#url_get = "https://milhapremiada.com/cadastra-reserva"
#url_get = "https://milhapremiada.com/consultar-reserva"
name = input('Qual a URL do site desejado?\n')
dígitos= input('Quantos dígitos ?\n')
primeira = input('Qual o número premiado?\n')
numere= input('Qual o número  do bilhete?\n')
url_get =  name
html = requests.get(url_get).content

soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())

temperatura = soup.find("table", class_="table")
#print(temperatura)