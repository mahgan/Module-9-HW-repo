# URL of this file (booklover_test.py) in GitHub: 
# https://github.com/mahgan/DS5100--mg4ccz-/blob/main/lessons/M08/booklover_test.py

import unittest
import pandas as pd
import numpy as np
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self): 
        reader1 = BookLover("Snape","Snape@deatheater.com","Romance",0,pd.DataFrame())
        reader1.add_book("Sorcerer's Stone",1)
        expected = ["Sorcerer's Stone"]
        self.assertEqual(expected,reader1.book_list['book_name'].values)

    def test_2_add_book(self):
        reader2 = BookLover("Snape","Snape@deatheater.com","Romance",0,pd.DataFrame())
        reader2.add_book("Sorcerer's Stone",1)
        reader2.add_book("Sorcerer's Stone",1)
        expected = ["Sorcerer's Stone"]
        self.assertEqual(expected,reader2.book_list['book_name'].values)   
                
    def test_3_has_read(self): 
        reader3 = BookLover("Snape","Snape@deatheater.com","Romance",0,pd.DataFrame())
        reader3.add_book("Sorcerer's Stone",1)
        self.assertTrue(reader3.has_read("Sorcerer's Stone"))           
        
    def test_4_has_read(self): 
        reader4 = BookLover("Snape","Snape@deatheater.com","Romance",0,pd.DataFrame())
        self.assertFalse(reader4.has_read("Chamber of Secrets")) 
        
    def test_5_num_books_read(self): 
        reader5 = BookLover("Snape","Snape@deatheater.com","Romance",0,pd.DataFrame())
        reader5.add_book("Sorcerer's Stone",1)
        reader5.add_book("Chamber of Secrets",3)
        reader5.add_book("Prisoner of Azkaban",2)
        expected = 3
        self.assertEqual(expected,reader5.num_books_read()) 
    def test_6_fav_books(self):
        reader6 = BookLover("Snape","Snape@deatheater.com","Romance",0,pd.DataFrame())
        reader6.add_book("Sorcerer's Stone",2)
        reader6.add_book("Chamber of Secrets",3)
        reader6.add_book("Prisoner of Azkaban",2)
        reader6.add_book("Half Blood Prince",5)
        reader6.add_book("Deathly Hallows",1)
        reader6.add_book("Fault in Our Stars",5)
        actualBooks = reader6.fav_books()["book_name"].values
        self.assertTrue(len(actualBooks) == 2 and "Half Blood Prince" in actualBooks 
                        and "Fault in Our Stars" in actualBooks)

if __name__ == '__main__':
    
    unittest.main(verbosity=3)
