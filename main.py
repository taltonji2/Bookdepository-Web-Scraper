from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re


def get_data():
  page = 1
  books = []

  while page != 5:
    response = requests.get(
        f"https://www.bookdepository.com/bestsellers?page={page}")
    html = response.content
    soup = BeautifulSoup(html, "lxml")

    for book_item in soup.find_all("div", class_="book-item"):
        book = {}
        book["title"] = book_item.find("h3", class_="title").a.get_text(strip=True)
        book["author"] = book_item.find("p", class_="author").get_text(strip=True)
        book["format"] = book_item.find("p", class_="format").get_text(strip=True)
        book["publish"] = book_item.find("p", class_="published").get_text(strip=True)
        try:
          price = str(book_item.find("p", class_="price").find("span", class_="sale-price"))[28:33].replace('<',"")
        except:
          price = ""
        book["price"] = price
        books.append(book)

    page = page + 1
  
  print(books)


get_data()
