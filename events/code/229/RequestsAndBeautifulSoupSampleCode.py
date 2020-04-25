import requests
from bs4 import BeautifulSoup

url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"
r = requests.get(url)

soup = BeautifulSoup(r.content)

divs = soup.find_all("div", {"class": "highlight"})

for div in divs:
    print(div)

links = soup.find_all("a")

for link in links:
    "<a href='%s'>%s</a>" % (link.get("href"), link.text)

