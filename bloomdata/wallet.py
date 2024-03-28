'''
This module simulates and works as a wallet/bank
'''

class Wallet:
    '''
    This class works as a wallet and can run 2 function
    '''

    def __init__(self, initial_amount=0):
        self.balance = initial_amount
s
    def withdraw(self, amount):
        '''
        This function withdraws an amount of cash from your wallet
        '''
        if self.balance < amount:
            return "Not enough funds to withdraw"
        self.balance = self.balance - amount
        return f"Remaining balance after withdrawal: ${self.balance}"

    def deposit(self, amount):
        '''
        This function deposits an amount of cash into your wallet
        '''
        self.balance = self.balance + amount
        return f"After your deposit, your wallet now has a balance of: ${self.balance}"

    def __repr__(self):
        return f"Wallet with balance of: ${self.balance}"


if __name__ == '__main__':
    wallet1 = Wallet(100)
    print(f"You have ${wallet1.balance} in your wallet")
    print(wallet1.deposit(60))
    print(wallet1.withdraw(100))
    print(wallet1.withdraw(20))
    print(f"You have ${wallet1.balance} in your wallet")
