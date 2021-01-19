# To be used for runtime flexibility in method/application usage without falling into inheritance nightmare
# We use aggregation/composition instead of inheritance

#More details at:https://refactoring.guru/design-patterns/decorator


#In a purely functional sense decorators can be used to modify existing function using a more generalized code written
#Examples of usage are:-You only want to run functions during particular time of day.Hence,you create a decorator function which takes any function and runs it only a particular part of the day
#Check examples and refresher logic at https://realpython.com/primer-on-python-decorators/

def arithmetic(func):
    def wrapper(*args,**kwargs):
        print("Before the function")
        func(*args,**kwargs)
        print("after the function")
        return func(*args,**kwargs)
    return wrapper


@arithmetic
def add(a):
    print("add")
    return a*5 

# We can similarly use decorator classes

class arithmetic2():
    def __init__(self,func):
        self._func=func
    
    def __call__(self,*args,**kwargs):
        print("Before running the function")
        b= self._func(*args,**kwargs)
        return f"This is {b}"


@arithmetic2
def test(a):
    return a*5



# Now lets try and implement a decorator based structure for a cafe billing systemas in the headfirst book
from abc import ABC,abstractmethod

class Beverage(ABC):
    def __init__(self):
        self.description=None
    
    def get_description(self,*args,**kwargs):
        pass

    @abstractmethod
    def cost(self):
        pass



class Houseblend(Beverage):

    @milk
    def cost(self):
        return 50

class Darkroast(Beverage):

    def cost(self):
        return 20

class Espresso(Beverage):

    def cost(self):
        return 30


class Decaf(Beverage):

    def cost(self):
        return 40

# class milk():
#     def __init__(self,coffee):
#         self._coffee=coffee

#     def __call__(self):
#         raw_cost=self._coffee()
#         return raw_cost+5


def milk(cost):
    def inner_cost(*args,**kwargs):
        raw_cost=cost(*args,**kwargs)
        return raw_cost+5
    return inner_cost    


# The problem with using decorators as above trying to incorporate multiple costs in a coffee is that you cannot do that at run time it has to be done before compiling

# We will now try and implement this pricing tool as mentioned in the book


class Beverage(ABC):
    description=None
    
    @abstractmethod
    def get_description(*args,**kwargs):
        return description

    @abstractmethod
    def cost():
        pass


# class Condimentdecorator(Beverage):

#     @abstractmethod
#     def get_description(*args,**kwargs):
#         return description

#     @abstractmethod
#     def cost():
#         pass


class Espresso(Beverage):
    description=None

    def __init__(self):
        self.get_description()

    def get_description(self,*args,**kwargs):
        self.description="Espresso"

    def cost(self):
        return 1.99


class Mocha(Beverage):
   
    description=None

    def __init__(self,beverage):
        self.beverage=beverage
        self.get_description()

    def get_description(self):
        self.description=self.beverage.description+" "+"Mocha"
        
    def cost(self):
        return self.beverage.cost()+2

class Whippedcream(Beverage):
   
    description=None

    def __init__(self,beverage):
        self.beverage=beverage
        self.get_description()

    def get_description(self):
        self.description=self.beverage.description+" "+"Whippedcream"
        
    def cost(self):
        return self.beverage.cost()+3


# Now you have a pricing which can get pricing for whatever lee

#Only Espresso

coffee=Espresso()
print(coffee.description)
print(coffee.cost())
#Add Mocha
coffee=Mocha(coffee)
print(coffee.description)
print(coffee.cost())

# Add another Mocha
coffee=Mocha(coffee)
print(coffee.description)
print(coffee.cost())

# Add Whipped cream
coffee=Whippedcream(coffee)
print(coffee.description)
print(coffee.cost())




    



















 





