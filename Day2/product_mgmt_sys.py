class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock

    def discount(self,discount):
        if discount > 0:
            self.price = self.price - self.price* (discount/100)
            print(f"After discount the new price is {self.price}")

    def display(self):
        print(f"Product Name:{self.name} Price: {self.price}  Stock:{self.stock}")




class ElectronicProduct(Product):
    def __init__(self,name,price,stock,brand,warranty):
        super().__init__(name,price,stock)
        self.brand = brand
        self.warranty = warranty

    def display(self):
        super().display()
        print(f"Brand: {self.brand}, Warranty: {self.warranty} years")

class Book(Product):
    def __init__(self,name,price,stock,author,pages):
        super().__init__(name,price,stock)
        self.author = author
        self.pages = pages

    def display(self):
        super().display()
        print(f"Author: {self.author}, Pages: {self.pages}")


e1 = ElectronicProduct("Laptop",7000,10,"Acer-Nitro",2)
e1.display()
e1.discount(10)

print()


b = Book("Laptop",7000,10,"Sachin",250)
b.display()
b.discount(5)
    
