import requests 
from bs4 import BeautifulSoup as bs


r = requests.get("https://github.com/nezlobnaya")

soup = bs(r.content)


print(soup.prettify())