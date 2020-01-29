from bs4 import BeautifulSoup
import requests
import json
import re
booksArr = []

with open('data.json') as json_data:
    jsonData = json.load(json_data)
    for i in jsonData:
        urlAfter = i['url']
        urlBefore = "https://www.goodreads.com/"
        url = urlBefore + urlAfter
        print url
        response = requests.get(url, timeout=10)
        content = BeautifulSoup(response.content, "html.parser")
        isbn = content.find("span", attrs={"itemprop": "isbn"})
        if isbn is not None: isbn = isbn.text.encode('utf-8')
        genres = []
        for cat in content.findAll('div', attrs={"class": "elementList"}):
            catText =  cat.find("div", attrs={"class": "left"})
            if catText is not None: catText = re.sub('[^a-zA-Z0-9 >.]', '',catText.text.encode('utf-8').replace("  ",""))
            genres.append(catText)
        ratings = []
        ratingsObject = {
            "ratings_score": re.sub('[^0-9.]', '',content.find("span", attrs={"itemprop": "ratingValue"}).text.encode('utf-8')),
            "ratings_count": content.find("meta", attrs={"itemprop": "ratingCount"}).get('content'),
        }
        ratings.append(ratingsObject)

        bookObject = {
            "name": content.find('h1', attrs={"id": "bookTitle"}).text.encode('utf-8').replace("\n", "").replace("  ", ""),
            "url": url,
            "author": content.find("a", attrs={"class": "authorName"}).text.encode('utf-8'),
            "description": re.sub('[^a-zA-Z0-9 .]', '', content.find("div", attrs={"id": "descriptionContainer"}).text.encode('utf-8').replace("\n...more\n\n", "")),
            "ISBN": isbn,
            "genres": genres,
            "ratings": ratings,
        }
        booksArr.append(bookObject)
        print  bookObject

with open('booksData.json', 'w') as outfile:
    json.dump(booksArr, outfile, indent=2)

