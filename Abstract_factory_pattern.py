# A more deatiled version of factory pattern where we can use abstract classes to control the deatils of implementation of the product(pizza in this case to be delivered)
from abc import ABC,abstractmethod


class PizzaIngredientFactory(ABC):
    
    @abstractmethod
    def create_dough():
        pass
    
    @abstractmethod
    def create_sauce():
        pass

    @abstractmethod
    def create_cheese():
        pass

    @abstractmethod
    def create_veggies():
        pass

    @abstractmethod
    def create_pepperoni():
        pass

    @abstractmethod
    def create_clam():
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    @staticmethod
    def create_dough():
        return 'Thin crust'
    @staticmethod
    def create_sauce():
        return 'Marinara Sauce'
    @staticmethod
    def create_cheeese():
        return 'Reggiano Cheese'
    @staticmethod
    def create_veggies():
        return 'Garlic+Onion+mushroom+Red_pepper'
    @staticmethod
    def create_pepperoni():
        return 'Sliced pepperoni'
    @staticmethod
    def create_clam():
        return 'Fresh Clams'


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    @staticmethod
    def create_dough():
        return 'Thick crust'
    
    @staticmethod
    def create_sauce():
        return 'Plum tomato Sauce'
    
    @staticmethod
    def create_cheeese():
        return 'MozzarelaCheese'
    
    @staticmethod
    def create_veggies():
        return 'Spinach+eggplant'
    
    @staticmethod
    def create_pepperoni():
        return   'Sliced pepperoni'
    
    @staticmethod
    def create_clam():
        return 'Frozen Clams'



class Pizza():

    def __init__(self,dough,sauce,cheese,veggies,pepperoni,clam):
        self.name=None
        self.dough=dough
        self.sauce=sauce
        self.cheese=cheese
        self.veggies=veggies
        self.pepperoni=pepperoni
        self.clam=clam


    @abstractmethod
    def prepare():
        pass

    def bake():
        Print("Bake for 25 min at 250 degrees")

    def cut():
        print("Cut Pizza into diagnol shapes")

    def box():
        print("Boxing pizza into companies branded boxes")

    def setname(self,name):
        self.name=name
    

    def __str__(self):
        return self.name



class CheesePizza(Pizza):

    def __init__(self,ingredient_factory):
        self.ingredient_factory=ingredient_factory

    def prepare(self):
        print("Making Pizza")
        print(self.ingredient_factory.create_dough())
        print(self.ingredient_factory.create_sauce())
        print(self.ingredient_factory.create_cheeese())


class ClamPizza(Pizza):

    def __init__(self,ingredient_factory):
        self.ingredient_factory=ingredient_factory

    def prepare(self):
        print("Making Pizza")
        print(self.ingredient_factory.create_dough())
        print(self.ingredient_factory.create_sauce())
        print(self.ingredient_factory.create_cheeese())
        print(self.ingredient_factory.create_clam())

    



class PizzaStore(ABC):
    @abstractmethod
    def create_pizza():
        pass


class ChicagoPizzaStore(PizzaStore):

    def __init__(self,pizza_type,ingredient_factory):
        self.pizza_type=pizza_type
        self.ingredient_factory=ingredient_factory # How you define the ingredient factory is what decides componenents of a pizza

    def create_pizza(self):
        if self.pizza_type=='Cheese':
            pizza=CheesePizza(self.ingredient_factory)
            pizza.setname="Chicago style cheese Pizza"
            return pizza

        elif self.pizza_type=='Clam':
            pizza=ClamPizza(self.ingredient_factory)
            pizza.setname="Chicago style clam Pizza"
            return pizza
    


class NYPizzaStore(PizzaStore):

    def __init__(self,pizza_type,ingredient_factory):
        self.pizza_type=pizza_type
        self.ingredient_factory=ingredient_factory # How you define the ingredient factory is what decides componenents of a pizza

    def create_pizza(self):
        if self.pizza_type=='Cheese':
            pizza=CheesePizza(self.ingredient_factory)
            pizza.setname="NY style cheese Pizza"
            return pizza

        elif self.pizza_type=='Clam':
            pizza=ClamPizza(self.ingredient_factory)
            pizza.setname="NY style clam Pizza"
            return pizza
    
