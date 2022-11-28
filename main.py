from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.bookdepository.com/')
soup = BeautifulSoup(html.text, 'lxml')
books = soup.find('div', class_ ='book-item')
# print(books)
for book in books: 
  book_title = book.find('div', class_ ='item-info').h3.a.text.replace('  ', '')
  book_author = book.find('div', class_ ='item-info').p.span.a.span.text
#   book_price = book.find('',).text.replace(' ', '')
  print(book_title)

