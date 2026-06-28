

product_name = "ipad"
product_price = 78000
product_code = "ipadm2"
product_stock = 10


product2_name = "ip0d"
product2_price = 40000
product2_code = "ip0d40"
product2_stock = 10 

def discount(price,discount):
    return price*(1.0-(discount/100))

def display_info(name,price,code):
    print(name,price,code)

def sold(name,stock):
    print(name,"has been sold")
    stock = stock -1 if stock>0 else 0
    return stock

print("info about ipad")
display_info(product_name,product_price,product_code)
#simulate a sale of product 1
product_stock = sold(product_name,product_stock)
print("Stock Remaining",product_stock)


# print("info about ipod")
# display_info(product2_name,product2_price,product2_code)
# print(discount(product_price,10))
