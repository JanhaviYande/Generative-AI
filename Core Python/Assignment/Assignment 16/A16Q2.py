# Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.
class Product:
    discount = 10
    def __init__(self,pid = 0,pname = None,price = 0,quantity = 0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
    
    def __del__(self):
        print("All products are sold")

    def ShowProduct(self):
        print("Product Id : ",self.pid)
        print("Product Name : ",self.pname)
        print("Product Price : ",self.price)
        print("Product Quantity : ",self.quantity)
        print("How much discount on product : ",Product.discount)
        

    def apply_discount(self):
        discount_amount = (self.price * Product.discount) / 100
        final_price = self.price - discount_amount
        print("Price after discount : ",final_price)
        print("---------------------------------------------------")

p1 = Product(101,"Laptop",55000,1)
p1.ShowProduct()
p1.apply_discount()

p2 = Product()
p2.ShowProduct()
p2.apply_discount()
