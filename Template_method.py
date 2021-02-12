# The method creates a gloabl algorithm in a abstract class which the subclasses are suppose to use ,it then allows subclasses to change ceratin parts of algorithm to keep flexibility

from abc import ABC,abstractmethod

class Beverage(ABC):

    def prepare_recipe(self)->"The algorithm which has components define in base class while some componenents are abstracted away for subclasses to handle": 
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Water Boiling")

    @abstractmethod
    def brew(self):
        pass

    def pour_in_cup(self):
        print("Pouring in cup")

    @abstractmethod
    def add_condiments(self):
        pass


class Coffee(Beverage):

    def brew(self):
        print("Brew the coffee grinds")

    def add_condiments(self):
        print("Add more hot water")



class Tea(Beverage):

    def brew(self):
        print("Steep the Tea Bag")

    def add_condiments(self):
        print("Add a slice of lemon")



        

