import re
import requests
from bs4 import BeautifulSoup
# import pandas as pd

# Parse URL using BeautifulSoup
def get_page_info(url):
  # Download the page
  response = requests.get(url)
  
  # check successful response
  if response.status_code != 200:
      raise Exception('Failed to load page {}'.format(url))
  
  #Page conetnt
  page_contents = response.text
  
  # Parse using BeautifulSoup
  doc  = BeautifulSoup(page_contents, 'html.parser')    
  
  return doc

# Find Book Genre
def get_book_genre(scrap):  
  # Find all unordered list with class"nav nav-list"
  ul_cat = scrap.find_all('ul', {'class': "nav nav-list"})
  # Use regex to parse un-necessary characters, strings etc
  books_genre_ul =  ''.join(tag.text.replace('\n', '') for tag in ul_cat)
  genre_ul = re.sub('\s{2,}',',', books_genre_ul)[1:-1].split(",")
  return genre_ul[1:]

# Find book genre URLs
def get_genre_url(scrap):
  book_genre = get_book_genre(scrap)
  len_genre = len(book_genre)
  # Find all a tags with href element
  project_href = [i['href'] for i in scrap.find_all('a', href=True)]    
  base_url = "http://books.toscrape.com/"
  books_genre_urls = [base_url + tag for tag in project_href[3:len_genre+3]]
  return books_genre_urls

# Find all book title list of each genre (shown in first page)
def get_books_title(document):
  book_doc = [i for i in document.find_all('a', title=True)]
  book_doc_len = len(book_doc)
  book_doc_list = []
  for i in range(book_doc_len):
      book_doc_list.append(book_doc[i].text.strip())
      
  return book_doc_list

# Find all book URLs list of each genre (shown in first page)
def get_books_title_url(doc):
  book_doc_url = [i for i in doc.find_all('a', title=True)]
  book_doc_url_len = len(book_doc_url)
  book_doc_url_list = []
  for i in range(book_doc_url_len):
      book_doc_url_list.append(book_doc_url[i]['href'])
      
  book_doc_url_str = str(book_doc_url_list)        
  for i in range(book_doc_url_len):
      book_doc_url_str = re.sub('\.{2,}\/{1,}','', book_doc_url_str)
      
  book_doc_url_str = re.sub(r'\[', '', book_doc_url_str) 
  book_doc_url_str = re.sub(r'\]', '', book_doc_url_str)
  book_doc_url_str = re.sub(r"\'", '', book_doc_url_str)
  book_doc_url_str = re.sub(r"\ ", '', book_doc_url_str)
  book_doc_url_list = book_doc_url_str.split(",")
  
  return ["http://books.toscrape.com/catalogue/" + url for url in book_doc_url_list]

# Find Book detail like book title, price etc
def get_book_info(book_title_url):
  book_info = get_page_info(book_title_url)    
  book_info_header = [header.text.strip() for header in book_info.find_all('th')]
  book_info_detail = [desc.text.strip() for desc in book_info.find_all('td')]
  book_dict = dict(zip(book_info_header, book_info_detail))
  book_dict['title'] = ''.join(title.text.strip() for title in book_info.find_all('title'))
  book_dict['url'] = book_title_url
  return book_dict

# Scrap URL
def scrap_web(url):
    # get_page_info() return BeautifulSoup doc
    document = get_page_info(url)
    
    # It will return list of each genre title
    book_genre = get_book_genre(document)
    length_book_genre = len(book_genre)
    
    # It will return list of each genre url
    book_genre_url = get_genre_url(document)
    length_genre_url = len(book_genre_url)
    
    value = int(input(f"Please enter a number less than {length_genre_url} to see your chosen genre\n"))
    print(f'You have chosen {book_genre[value]} category')
    
    # It will return BeatifulSoup doc of each book page
    info = get_page_info(book_genre_url[value])
    
    # It will return book_tile of all books in one particlar genre
    book_title_list = get_books_title(info)
#     print(book_title_list)
    len_book_title = len(book_title_list)
    
    # It will return urls of all books in one particlar genre
    book_title_url = get_books_title_url(info)    
    
    value2 = int(input(f"Enter a number less than {len_book_title} to scrape\n"))
    print(f'Your Book Title is:  "{book_title_list[value2]}"')
                    
    book_info = get_book_info(book_title_url[value2])
    # books_df = pd.DataFrame(book_info)
    
    return book_info

web_url = "http://books.toscrape.com"
print(scrap_web(web_url))