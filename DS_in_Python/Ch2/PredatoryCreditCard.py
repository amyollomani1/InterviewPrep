class PredatoryCreditCard(CreditCard):
        #__init__ class is constructor

    def __init__(self, customer, bank, acnt, limit, apr):
        #Create new credit card instance
        super().__init__(customer, bank, acnt, limit) #super constructor
        self._apr = apr
        
    #Overriding original
    def charge(self,price):
        success = super().char(price) #call original method
        if not success:
            self._balance += 5
            
        return success
       
    #additional new method 
    def process_month(self):
        if self._balanc > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
    
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