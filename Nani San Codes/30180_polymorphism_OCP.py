class Item:
    _weight = None
    def __init__(self, weight):
        self._weight = weight
    
    def display_weight(self):
        pass
        
class Coins(Item):
    _amount = None
    def __init__(self, weight, amount):
        super().__init__(weight)
        self._amount = amount
    def display_weight(self):
        print(f"Weight of the Coins: {self._weight}g")
        
class RareItem(Item):
    _value = None
    def __init__(self, weight, value):
        super().__init__(weight)
        self._value = value
    def display_weight(self):
        print(f"Weight of the Rare Item: {self._weight}g")
        
class Key(Item):
    _code = None
    def __init__(self, weight, code):
        super().__init__(weight)
        self._code = code
    def display_weight(self):
        print(f"Weight of the Key: {self._weight}g")
        
class CrossBow(Item):
    _power = None
    def __init__(self, weight, power):
        super().__init__(weight)
        self._power = power
    def display_weight(self):
        print(f"Weight of the Crossbow: {self._weight}g")
        
class Book(Item):
    _title = None
    def __init__(self, weight, title):
        super().__init__(weight)
        self._title = title
        
    def display_weight(self):
        print(f"Weight of the Book: {self._weight}g")
    
class IPad(Item):
    __model = None
    def __init__(self, weight, model):
        super().__init__(weight)
        self.__model = model
    def display_weight(self):
        print(f"Weight of the iPad: {self._weight}g")
        
class Bag:
    __current_weight = None
    __items = None
    def __init__(self, current_weight=0, items=[]):
        self.__current_weight = current_weight
        self.__items = items
    def canAddItem(self, item : Item):
        return self.__current_weight + item._weight <= 4500
    
    def addItem(self, item : Item):
        if self.canAddItem(item):
            self.__items.append(item)
            self.__current_weight += item._weight
            print(f"Added {item.__class__.__name__} to the bag.")
            
    def display_current_weight(self):
        print(f"Current weight in the bag: {self.__current_weight} grams")

##usage
pennies = Coins(10, 5)
nickles = Coins(20, 20)
ruby = RareItem(200, 10000)
emerald = RareItem(700, 19000)
safe_key = Key(100, 'secret')
master_key = Key(300, 'master')
crossbow = CrossBow(5000, 10)
calculus = Book(350, 'Differential Calculus')
physics = Book(700, 'Newtonian Mechanics')
iPad = IPad(1200, 'iPad Pro')
iPad_mini = IPad(950, 'iPad Mini')

item_list = [pennies, ruby, emerald, safe_key, master_key, crossbow, calculus, physics, iPad, iPad_mini]

bag = Bag()

for item in item_list:
    item.display_weight()
    if bag.canAddItem(item):
        bag.addItem(item)
    else:
        print("Item cannot be added as it exceed the maximum allowed weight.")
    bag.display_current_weight()
    print("----------------------------------------------------------------")
        
    
