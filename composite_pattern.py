#In composite pattern we try to implement a tree like hierarchial structure where we will have a base class definingnall the mthods we might expect across the componenets ,some of them might make sense and some may not for a component
# A component can decide which method it wants to inherit from the composite

#Lets take an example of a different menus and menu items as in the book



class MenuComponent():
    
   
    def add(self):
        pass

  
    def remove(self):
        pass

    
    def get_child(self):
        pass

   
    def get_name(self):
        pass

   
    def get_description(self):
        pass


    def get_price(self):
        pass

    
    def is_vegetarian(self):
        pass

  
    def __str__(self):
        pass


class MenuItem(MenuComponent):

    def __init__(self,name,description,vegetarian,price):
        self.name=name
        self.description=description
        self.vegetarian=vegetarian
        self.price=price
    
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def is_vegetarian(self):
        return self.vegetarian

    def __str__(self):
        return f"{self.name}:{self.description},{self.price}"


class Menu(MenuComponent):

    def __init__(self,name,description,menu_items=[]):
        self.name=name
        self.description=description
        self.menu_items=menu_items

    def add(self,item):
        self.menu_items.append(item)
        return f"{item} added to the menu"

    def remove(self,item):
        self.menu_items.remove(item)
        return f"{item} removed from the menu"
    
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description
    
    def get_child(self,i):
        return self.menu_items[i]

    def __str__(self):
        return f"{self.name}:{self.description}"


# In the same way we can have a hierarchy of Menucomponent and items 
    





    

        


