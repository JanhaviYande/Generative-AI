# Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.
class Shirt:
    increament = 0.10
    def __init__(self,sid = 0,sname = None,type = None,price = 0,size = None):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print("All shirts are sold")

    def ShowShirt(self):
        print("Shirt Id : ",self.sid)
        print("Shirt Name : ",self.sname)
        print("Shirt Type : ",self.type)
        print("Shirt Price : ",self.price)
        print("Shirt Size (S,M,L,XL): ",self.size)

    def final_price(self):
        if self.size == 'S':
            final = self.price 
        elif self.size == 'M':
            final = self.price + (self.price * Shirt.increament)
        elif self.size == 'L':
            final = self.price + (self.price * Shirt.increament * 2)
        elif self.size == 'XL':
            final = self.price + (self.price * Shirt.increament * 3)
        elif self.size == 'XXL':
            final = self.price + (self.price * Shirt.increament * 4)
        else:
            print("Invalid Size")

        print("Final Price : ",final)

s1 = Shirt(1,"Raymond","Formal",2000,"M")
s1.ShowShirt()
s1.final_price()