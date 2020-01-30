Run all codes on PyCharm 2019.3.2 (Community Edition)

------Section 1 Data Collection -------------------
---> linksscraper.py:
This python code scrapes all the links of all the popular books by date on https://www.goodreads.com/book/popular_by_date.
All the links are stored in  links.json file.
--> booksscraper.py:
This python codes read all the books links in links.json one by one, and scrapers those books to get the
required information and store it in booksData.json.
------End of Data Collection Section 1 -----------------

-------Section 2 Data Analysis --------------------------
-------Part 1 -------
---> highestRated.py:
This python code collect top 10 highest rated books from the books data collect in Section 1 stored in
booksData.json and after collecting top 10 high rating books stores in highestRated.json file.
-------Part 2 -------
--->popularAuthor.py:
This python code get authors with maximum books in popular books stack and all those authors are stored in
popularAuthor.json file.
--------Part 3 -------
---> genres.py:
This python code collects all the genres coming in the popular books stack by iterating each book genres,
as a result all the genres are collected and stored in genres.json file.
--------Part4 --------
---> genresRating.py:
This python code picks the genres of each book and rating of that book is assigned to all the genres in that book,
after iterating each book the average rating of each genre is calculated and stored in genresRatingAll.json file.
-------End of Data Analysis Section 2 --------------------

