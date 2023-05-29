class CreditCard:
        #__init__ class is constructor

    def __init__(self, customer, bank, acnt, limit):
        #Create new credit card instance
        self._customer = customer
        self._bank = bank
        self.account = acnt
        self._limit = limit
        self._balance = 0
            
    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank   
    
    def get_limit(self):
        return self._limit
    
    def charge(self,price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        self._balance -= amount
        
    def get_balance(self):
        return self._balance
    
#testing class:
if __name__ == '__main__':
    wallet = []
    #instance of CreditCard
    wallet.append(CreditCard('John Bowman' , 'California Savings' ,
                    '5391 0375 9387 5309' , 2500))
    wallet.append(CreditCard('John Bowman' , 'California Federal' ,
                    '3858 0399 1954 5309' , 3500))
    wallet.append(CreditCard('John Bowman' , 'California Savings' ,
                    '000 0600 7900 9234' , 5000))

    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        
    for c in range(3):
        print('Customer = ', wallet[c].get_customer())
        while wallet[c].get_balance() > 100:
                wallet[c].make_payment(100)
                print('New balance =', wallet[c].get_balance())
        print()        