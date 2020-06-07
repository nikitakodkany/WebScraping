#Python Scipt to Web Scrape Covid19 information

import requests
from bs4 import BeautifulSoup

green = '\033[32;1m'
red = '\033[31;1m'
cyan = '\033[36;1m'
ENDC = '\033[m'

url = "https://www.worldometers.info/coronavirus/"
r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")
data = s.find_all("div", class_="maincounter-number")

print("Total Cases: ",cyan, data[0].text.strip(), ENDC)
print("Total Deaths: ",red, data[1].text.strip(), ENDC)
print("Total Recovered: ",green, data[2].text.strip(), ENDC)
