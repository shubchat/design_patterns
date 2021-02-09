# A factory method lets subclasses decide the concrete implementation of a function
# or a product

# Below is an example of different pizza stores of a single pizza outlet

from abc import ABC, abstractmethod


class PizzaStore(ABC):
    @abstractmethod
    def create_pizza():
        pass


class ChicagoPizzaStore(PizzaStore):
    name = "Chicago_Pizza"

    def __init__(self, type):
        self.type = type

    def create_pizza(self):
         Pizza=ChicagoPizza(self.type)
         return Pizza()


class NYPizzaStore(PizzaStore):
    name = "NY_Pizza"

    def __init__(self, type):
        self.type = type

    def create_pizza(self):
        Pizza=NYPizza(self.type)
        return Pizza()


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


class ChicagoPizza(Pizza):
    def __init__(self, pizza_type):
        self.pizza_type = pizza_type

    def __call__(self):

        if self.pizza_type == "Cheese":
            return self.cheese_pizza()

        elif self.pizza_type == "Pepperoni":
            return self.pepperoni_pizza()

        elif self.pizza_type == "Clam":
            return self.clam_pizza()

        elif self.pizza_type == "Veggie":
            return self.veggie_pizza()

        else:
            return "We dont serve this pizza"

    @staticmethod
    def cheese_pizza():
        return "Chicago cheese pizza"
    @staticmethod
    def pepperoni_pizza():
        return "Chicago pepperoni pizza"
    @staticmethod
    def clam_pizza():
        return "Chicago clam pizza "
    @staticmethod
    def veggie_pizza():
        return "Chicago veggie pizza"


class NYPizza(Pizza):
    def __init__(self, pizza_type):
        self.pizza_type = pizza_type

    def __call__(self):

        if self.pizza_type == "Cheese":
            return self.cheese_pizza()

        elif self.pizza_type == "Pepperoni":
            return self.pepperoni_pizza()

        elif self.pizza_type == "Clam":
            return self.clam_pizza()

        elif self.pizza_type == "Veggie":
            return self.veggie_pizza()
        else:
            return "We dont serve this pizza type"

    @staticmethod
    def cheese_pizza():
        return "NY cheese pizza"

    @staticmethod
    def pepperoni_pizza():
        return "NY pepperoni pizza"

    @staticmethod
    def clam_pizza():
        return "NY clam pizza "

    @staticmethod
    def veggie_pizza():
        return "NY veggie pizza"




