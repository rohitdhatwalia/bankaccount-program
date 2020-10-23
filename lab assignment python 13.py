class BankAccount:
    account_number = int(input("enter your account number : "))
    customer_name = input("enter your name : ")
    account_type = input("enter your account type : ")
    print("your account have rs. 1000/-")

    def deposit(self,balance):
        bal = 1000
        bal = bal + balance
        return bal
        
    def withdraw(self,balance2):
        
        if balance2 >= 10000:
            min = bal2 - balance2
            if min >= 1000:
                print("rameaning balance is :",min)
            else:
                print("you have less than rupess 1000/- in your account , so please deposit rupess later")
                
            
        else:
            print("you can only withdraw maximum amount of rupess 10000/- per transaction ")
            
n= int(input("enter a number : "))
for i in range(n):
    obj1 = BankAccount()
    bal2 = obj1.deposit(balance = int(input("enter your balance for deposite : ")))
    print("total balance : " , bal2)
    
    obj1.withdraw(balance2 = int(input("enter your balance for withdraw: ")))


print("Account number : ",BankAccount.account_number)
print("Customer name : " , BankAccount.customer_name)
print("Account type : ",BankAccount.account_type)