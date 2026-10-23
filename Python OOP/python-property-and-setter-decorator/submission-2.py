class BankAccount:
    def __init__(self, balance: int): 
        self.balance = balance # Don't modify this line

    @property  
    def alance(self) -> int: # TODO: Convert this method to use the @property decorator
        return self.balance
        
    @alance.setter
    def alance(self, value: int) -> None: # TODO: Convert this method to use the @property decorator
        if value >= 0:
            self.balance = value
        else:
            print("Balance cannot be negative!")


# Don't modify the code below this line
account = BankAccount(1000)
print(account.alance)
account.alance = -100
