# A factory method lets subclasses decide the concrete implementation of a function
#or a product

# Below is an example of different pizza stores of a single pizza outlet

from abc import ABC,abstractmethod

class PizzaStore(ABC):->'ABC for creating a pizza store'

    @abstractmethod
    def create_pizza():
        pass

class ChicagoPizzaStore(PizzaStore):
    name='Chicago_Pizza'
    def __init__(self,type):
        self.type=type

    def create_pizza(self):
        return Chicago_Pizza(self.type)

    
class NYPizzaStore(PizzaStore):
    name='NY_Pizza'
    def __init__(self,type):
        self.type=type
    
    def create_pizza(self):
        return NY_Pizza(self.type)

    

class Pizza(ABC):
    
    @abstractmethod
    def cheese_pizza():
        pass
    
    @abstractmethod
    def pepperoni_pizza():
        pass

    @abstractmethod
    def clam_pizza():
        pass
    
    @abstractmethod
    def veggie_pizza():
        pass

class Chicago_Pizza(Pizza):
    def __init__(self,pizza_type):
        self.pizza_type=pizza_type

    def __call__(self):

        if self.pizza_type=='Cheese':
            return cheese_pizza()

        elif self.pizza_type=='Pepperoni':
            return pepperoni_pizza()

        elif self.pizza_type=='Clam':
            return clam_pizza()
       
        elif self.pizza_type=='Veggie':
            return veggie_pizza()

    

