import booklover
import pandas as pd
import booklover.booklover as bl
reader = bl.BookLover("BillNye","Bill@ScienceGuy.com","Romance",0,pd.DataFrame())
reader.add_book("Eragon",5)
print(f"Number of books read: {reader.num_books_read()}")