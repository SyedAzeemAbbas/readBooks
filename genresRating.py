import json

gRating = []
with open('booksData.json') as json_data:
    jsonData = json.load(json_data)
    for i in jsonData:
        ratingScore = 0
        for item in i['ratings']:
            ratingScore = (item['ratings_score'])
        for x in i['genres']:
            if x is not None:
                gObject = {
                    "rating_score" : ratingScore,
                    "genre" : x,
                }
                gRating.append(gObject)
res = []
with open('genres.json') as json_data:
    jsonData = json.load(json_data)
    for i in jsonData:
        resObj = {
            "rating_score": 0,
            "genre" : i,
        }
        res.append(resObj)


for i in gRating:
    for x in res:
        if i['genre'] in x['genre']:
           if x['rating_score'] != 0:
                x['rating_score'] = float((float(x['rating_score']) + float(i['rating_score']))//2)
           else:
                x['rating_score'] = float(x['rating_score']) + float(i['rating_score'])

print res
with open('genresRatingAll.json', 'w') as outfile:
    json.dump(gRating, outfile, indent=2)
with open('genresRating.json', 'w') as outfile:
    json.dump(res, outfile, indent=2)