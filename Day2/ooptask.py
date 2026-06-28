#new product
#macbook
#price 1.5 lakh
#code macm5
#stock 5

#4 sold 
# 3 sold 


class Product:
    def initializer(self,name,price,stock,code):
        self.name = name
        self.price = price
        self.stock = stock
        self.code = code
    

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
            print(f"only {self.stock} left, So selling {self.stock} to you.\
                  Cannot Provide you remaining {quantity - self.stock} stock")
            self.stock = 0
            return

        else:
            self.stock = self.stock - quantity

        print("Remaining stock",self.stock)



p1 = Product()
p1.initializer("ipad",78000,10,"ipadm2")

p2= Product()
p2.initializer("macbook",150000,5,"macm5")

p2.sold(2)
p2.sold(1)
p2.sold(1)
p2.sold(3)