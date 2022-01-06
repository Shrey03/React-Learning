class Account:

    def __init__(self , owner  , balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,x):
        return f"{x} Money is added and your total balance is {x + self.balance}"

    def withdrawl(self,y):
        if y > self.balance:
            return f"sorry you are exceeding your account balance. you current balance is {self.balance}"
        else:
            final = self.balance - y
            return f"{y} is withdrawn and final balance is {final}"


A = Account("Shrey",1000)

# print(A.deposit(100))
# print(A.withdrawl(2000))
        