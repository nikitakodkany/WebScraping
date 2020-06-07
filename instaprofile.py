#Python script that web scrapes Instagram Profile Picture

import requests
from bs4 import BeautifulSoup

username = "o3ito"
URL = "https://www.instagram.com/{}/"

r = requests.get(URL.format(username))
s = BeautifulSoup(r.text,"html.parser")
u = s.find("meta", property="og:image")
url = u.attrs['content']

with open(username+'.jpg', "wb") as picture:
    binary = requests.get(url).content
    picture.write(binary)
