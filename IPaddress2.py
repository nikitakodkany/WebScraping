#Python Scrip to Web Scrape IP address

import requests
r = requests.get("https://httpbin.org/ip")

ip = r.json()['origin']

parsed = ip.split(",")[0]

yellow = '\033[33;1m'
ENDC = '\033[m'
print("IP ADDRESS: ",yellow, parsed, ENDC)
