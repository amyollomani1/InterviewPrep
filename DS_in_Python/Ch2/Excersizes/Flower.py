class Flower:
    def __init__(self, Name, PedalsCount, Price):
        self._name = Name
        self._pedalNum = PedalsCount
        self._price = Price
        
    def getName(self):
        return self._name
    
    def getCount(self):
        return self._pedalNum
    
    def getPrice(self):
        return self._price
       
    def setName(self,newName):
        self._name = newName
        
if __name__ == '__main__':
    flower = Flower('Rose', 10, 15.99)
    
    print('Name =', flower.getName())
    print("Pedals =", flower.getCount())
    print("Price =",flower.getPrice())
