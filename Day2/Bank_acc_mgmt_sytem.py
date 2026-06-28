class BankAccount:
    def __init__(self,account_no,account_holder,balance):
        self.account_no = account_no
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self,amt):
        if amt > 0:
            self.__balance += amt
            print(self.__balance)
        else: 
            print("Deposit amount must be positive.")


    def withdraw(self,amt):
        if self.__balance > amt :
            self.__balance = self.__balance - amt
            print(f"Successfully withdraw {amt} Rs")
        else:
            req_amt = amt - self.__balance
            print(f"Low _balance.Unable to withdraw please deposit Rs.{req_amt} to withdraw {amt}")

    def check__balance(self):
        print(f"Current _balance is Rs {self.__balance}")
        return self.__balance

    def __str__(self):
        return "Account Number : "+  self.account_no+"Account Name : "+self.account_holder


    def __eq__(self,other):
        if self.account_no == other.account_no:
            return True 
        else:
            return False

a1 = BankAccount("101","Virat",7000)
a2 = BankAccount("101","whyrat",5000)

a1.deposit(23)
a1.withdraw(2000)
a1.check__balance()

print(dir(a1))
a1._BankAccount__balance = 10000000
print(a1)
if a1 == a2:
    print("They are equal")