# BeautifulSoup-BooksToScrape
This is a demo project of using Python, Beautifulsoup, and requests to scrape books displaced at first page of all genre. Also I have included a demo about selecting(using random number) the genre and book title to see its details 

## Project steps
Here is an outline of the steps that I followed:

1. Downloaded the webpage( http://books.toscrape.com) using requests
2. Parsed the HTML source code using BeautifulSoup library and extract the desired infromation (also used REGEX)
3. Built the scraper components
4. Compiled the extracted information into Python list and dictionaries
5. Made interactive demo to display informations

## Future Work
1. Converting the python dictionaries into Pandas DataFrames
2. Write information to the final CSV file
3. Develop a flask app to desplay information

## References
1. Let’s Build a Python Web Scraping Project from Scratch | Hands-On Tutorial by Aakash N S, CEO, Jovian: https://www.youtube.com/watch?v=RKsLLG-bzEY
2. Beautiful Soup Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Note: The scripts in this demo works only for "http://books.toscrape.com" website

