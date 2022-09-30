class User:
    def __init__(self, first_name, last_name, star_bal=0, int_rate=0.05):
        self.first_name = first_name
        self.last_name = last_name 
        self.account = ChaseBank(star_bal, int_rate)

def make_withdrawal(self,amount):
    self.account.withdraw(amount)
    return self 

def show_user_bal(self):
    print(self.first_name, self.last_name)
    self.account_info()
    return self 

def deposit(self, amount):
    self.account.deposit(amount)
    return self

def yield_int(self):
    self.account.yield_int()
    return self 

class ChaseBank:
    def __init__(self, int_rate=0.5, balance=0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        print('You are making a deposit' + str(amount))
        self.balance += amount
        return self 

    def withdraw(self, amount):
        # if(self.balance - amount) >= 0:
# if statement changes because now we care about self bal being less 
        if self.balance < amount: 
            print("You don't have enough funds")
            self.balance -= amount
        else:
            print('Withdrawing moneys' + str(amount))
            self.balance -= amount
        return self 

    def account_info(self):
        print("Balance:" + str(self.balance))
        print("Interest Rate:", self.int_rate)
        return self 

    def yield_int(self):
        print("Processing interest rate") 
        self.balance += (self.balance * self.int_rate)
        return self 
    
savings = ChaseBank(.010,1500)
checking = ChaseBank(.05, 3500)

savings.deposit(5).deposit(10).deposit(45).withdraw(100).yield_int().account_info()
checking.deposit(10).deposit(15).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_int().account_info()


