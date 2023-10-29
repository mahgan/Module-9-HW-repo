# Name:  Mahin Ganesan
# Net UD: mg4ccz
# URL of this file (booklover.py) in GitHub: 
# https://github.com/mahgan/DS5100--mg4ccz-/blob/main/lessons/M08/booklover.py

import pandas as pd

class BookLover():
    def __init__(self,name,email,fav_genre,num_books,book_list):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    def add_book(self,book_name,rating):
        if(book_name not in self.book_list['book_name'].values):
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        else:
            print("Book already read!")
    
    def has_read(self,book_name):
        if(book_name in self.book_list["book_name"].values):
            return True
        return False
    def num_books_read(self):
        return len(self.book_list)
    def fav_books(self):
        favbookdf = self.book_list[self.book_list["book_rating"] > 3]
        return favbookdf
    

if __name__ == '__main__':
    df = pd.DataFrame()
    reader1 = BookLover("Joer","Joer@joerer.com","Sci-Fi",0,df)
    reader1.add_book("Eragon",5)
    reader1.add_book("CW",2)
    reader1.add_book("HappyFeet",10)
    reader1.has_read("Eragon")
    reader1.has_read("Eldest")
    reader1.num_books_read()
    print(reader1.fav_books())