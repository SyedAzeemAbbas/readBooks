from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.goodreads.com/book/popular_by_date'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
linkArr = []
for link in content.findAll('tr', attrs={"itemtype": "http://schema.org/Book"}):
    linksObject = {
        "url": link.find('a', attrs={"class": "bookTitle"}).get('href'),
    }
    linkArr.append(linksObject)
    with open('links.json', 'w') as outfile:
        json.dump(linkArr, outfile, indent=2)