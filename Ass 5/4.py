class account:
    def __init__(self):
        self.money = 0
    def deposit(self , n):
        self.money += n
    def withdraw(self , n):
        self.money -= n
    def balance(self):
        print("Current Balance is" , self.money)

a = account()
a.deposit(100)
a.balance()
a.withdraw(50)
a.balance()
a.deposit(100)
a.balance()