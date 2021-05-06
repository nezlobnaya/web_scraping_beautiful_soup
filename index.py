import requests
import re
from bs4 import BeautifulSoup as bs

site = 'https://www.google.com'

r = requests.get(site)

soup = bs(r.text, 'html.parser')
word_find = soup.find_all(["Contact GitHub"])
img_tags = soup.find_all('img')

print("IMAGES",img_tags)

urls =[]

for img in img_tags:
    try:
        link = img[('src')]
        print(link)
        urls.append(link)
    except KeyError:pass
urls1 = [img['src'] for img in img_tags]

print("URLS", urls)

for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if not filename:
         print("Regex didn't match with the url: {}".format(url))
         continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the site variable atm. 
            url = '{}{}'.format(site, url)
        r = requests.get(url)
        f.write(r.content)

# print(soup.prettify())
# print("WORD",word_find)
# # print(soup.find_all('title', limit=10))
# print("STRING",soup.find_all(string="nezlobnaya"))
# print("STRING",soup.find_all(string="Contact GitHub"))
# info_to_find = soup.find_all(['title',  "nezlobnaya"])
# # headers = soup.find_all(["h1", "h2",])

# # paragraph = soup.find_all("p")
# print(info_to_find)
# print("________________________")
# # print(headers)
# print("________________________")
# # print(paragraph)

