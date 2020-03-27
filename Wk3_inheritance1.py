#class for selecting size of Pizza
class Size:
    def __init__(self, size):
        self.size = size #S, M, L, XL

    def __str__(self):
        return  self.size
                
    def getSize(self):
        print (self.size)
        
    def setSize(self, size):
        self.size= size

# class for selecting half or whole pizza coverage with toppings
class Coverage:
    def __init__ (self, whole):
        self.whole = whole # True or False
    
    def __str__(self):
        if self.whole == True:
            return ' Whole' 
        else:
            return ' Half' #for later, need to add more methods in Order class that will take two halves to make a whole pizza
    
    def setWhole (self):
        self.whole=True
        
    def setHalf (self):
        self.whole=False #for later, need to add methods in an Order class to change from whole pizza to half
    
    def getCover(self):
        print (self.whole)
             
# class to add pizza toppings
class Toppings:
    def __init__(self):
        self.toppings = [] #toppings list

    def __str__(self):
        return  str(self.toppings)
        
    def addToppings(self, topping):
        self.toppings.append(topping)
    
    def getToppings(self):
        print (self.toppings)      
        
# class to build Pizza; inherits from Size, Coverage and Toppings classes (and for later, will add more methods in an Order class interface to collect a Customer's order, which will later use the Pizza class to finalize the order)
class Pizza(Size, Coverage, Toppings):
    def __init__(self, size, coverage, toppings=None):
        
        self.size = size
        self.coverage = coverage
        self.toppings = []
        
    def __str__(self):
        return 'Ordering ' + str(self.size) + ' size with ' + str(self.toppings) + ' on ' + str(self.coverage) + ' pizza ' 
        
def main(): # tests implementation of base clase Pizza which inherits from Size, Coverage and Toppings Classes            
    pizza = Pizza(Size('L'), Coverage(True))
    pizza.addToppings('Pepperoni')
    pizza.addToppings('Sausage')
    pizza.addToppings('Pineapple')
    pizza.getSize()
    pizza.setSize('XL')
    pizza.getToppings()
    print ('\n', pizza, '\n')

    # tests implementation of Size class
    size = Size ('L')
    size.getSize()
    size.setSize('XL')
    print ('\n', size, '\n')

    # tests implementation of Coverage class
    cover = Coverage(False)
    cover.getCover()
    print ('\n', cover, '\n')
    cover.setWhole()
    cover.getCover()
    print ('\n', cover, '\n')

    # tests implementation of Toppings class
    top = Toppings()
    top.addToppings('ham')
    top.addToppings('pineapple')
    top.getToppings()
    print ('\n', top, '\n')

main()
