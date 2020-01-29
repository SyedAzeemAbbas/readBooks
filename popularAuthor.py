import json
from collections import Counter

author = []
with open('booksData.json') as json_data:
    jsonData = json.load(json_data)
    for i in jsonData:
        author.append(i['author'])

c = Counter(author)
common = c.most_common()
pAuth = []
maxCount = max(common, key = lambda x: x[1]).__getitem__(1)
if maxCount>1:
    for i in common:
        if i[1]==maxCount:
            pAuth.append(i[0])
        else:
            break
    print pAuth
    with open('authors.json', 'w') as outfile:
        json.dump(pAuth, outfile, indent=2)
else:
    print 'All Author have 1 book'



