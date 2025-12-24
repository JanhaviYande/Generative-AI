# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.
class Book:
    count = 0
    def __init__(self,bid = 0,bname = None,price = 100,author = None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1

    def __del__(self):
        print("Book object destroyed")

    def ShowBook(self):
        print("Book Id : ",self.bid)
        print("Book Name : ",self.bname)
        print("Book Price : ",self.price)
        print("Book Author Name : ",self.author)
        print("Number of Books : ",Book.count)
        print("---------------------------------")

b1 = Book(1,"Python",500,"ABC")
b1.ShowBook()
b2 = Book(2,"Basic C",600,"XYZ")
b2.ShowBook()
b3 = Book ()
b3.ShowBook()

