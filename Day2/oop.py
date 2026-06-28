class Product:
    Count = 0
    def __init__(self,name,price,stock,code):  #__init__ technically known as Constructor but full form is initializer
        self.name = name
        self.price = price
        self.stock = stock
        self.code = code
        Product.Count +=1
    
    def __del__(self):
        Product.Count -= 1
    

    def display_info(this):
        print(this.name,this.price,this.stock,this.code)

    def discount(self,discount):
        if not discount < 0:
            self.price = self.price - self.price* (discount/100)

    
    def sold(self,quantity):
        if self.stock == 0:
            print("Out of stock, no items left!")
            return
        
        if quantity > self.stock:
            print(f"Only {self.stock} left! Selling {self.stock} instead of {quantity}")
            self.stock = 0
            return

        else:
            self.stock = self.stock - quantity

        print("Remaining stock",self.stock)



p1 = Product("ipad",78000,10,"ipadm2")


p1.sold(2)
p1.sold(3)

print(Product.Count)
print(dir(p1))
print(type(p1))

#new product
#macbook
#price 1.5 lakh
#code macm5
#stock 5

#4 sold 
# 3 sold 









# #same from procedural.py nut change variable
# def discount(price,discount): 
#     return price*(1.0-(discount/100))  

# def display_info(obj):
#     print(obj.name,obj.price,obj.code)


# def sold(name,stock):
#     print(name,"has been sold")
#     stock = stock -1 if stock>0 else 0
#     return stock

# print("info about ipad")
# display_info(p1)
# print("Stock Remaining",p1.stock)


# #simulate a sale of product 1
# p1.stock = sold(p1.name,p1.stock)
# print("Stock Remaining",p1.stock)

