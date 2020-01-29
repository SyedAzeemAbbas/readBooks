import json

genres = []
with open('booksData.json') as json_data:
    jsonData = json.load(json_data)
    for i in jsonData:
        for x in i['genres']:
            if x is not None:
                genres.append(x)
res = []
for i in genres:
    if i not in res:
        res.append(i)
print res
with open('genres.json', 'w') as outfile:
    json.dump(res, outfile, indent=2)