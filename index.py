import requests 
from bs4 import BeautifulSoup as bs


r = requests.get("https://github.com/nezlobnaya")

soup = bs(r.content)
word_find = soup.find("h2")

# print(soup.prettify())
print(word_find)
print(soup.find_all('title', limit=10))
print(soup.find(string="nezlobnaya"))