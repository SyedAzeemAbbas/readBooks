import json

with open('booksData.json') as json_data:
    jsonData = json.load(json_data)
    highScore = []
    for i in jsonData:
        for item in i['ratings']:
            ratingScore = (item['ratings_score'])
            bookObject = {
                "name" : i['name'],
                "ratingScore" : ratingScore,
            }
            highScore.append(bookObject)
N = 10
res = sorted(highScore, key=lambda x: x['ratingScore'] , reverse = True)[:N]
print res
with open('topRated.json', 'w') as outfile:
    json.dump(res, outfile, indent=2)