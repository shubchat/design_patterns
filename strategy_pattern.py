# Below is a simple strategy pattern where the attributes of duck class are independently set by each of the instances using the set method

class Duck:
    def __init__(self):
        self._fly_technique=None
        self._quack_technique=None

    @property
    def performfly(self):
        if self._fly_technique:
            return f"I fly {self._fly_technique}"
        else:
            return f"I fly default"

    @property
    def performquack(self):
        if self._quack_technique:
            return f"I quack {self._quack_technique}"
        else:
            return f"I quack default"


    @property
    def performswim(self):
        return f"I swim"

    
    def set_fly_technique(self,fly_technique):
        self._fly_technique=fly_technique
    
    
    def set_quack_technique(self,quack_technique):
        self._quack_technique=quack_technique

    
    
# Another way where we directly take a function input fron the user


class Duck2:
    def __init__(self,fly=None,quack=None):
        if fly!=None:
            self.perform_fly=fly
        if quack!=None:
            self.perform_quack=quack
        
    def perform_fly(self):
        print('Default fly')
    
    def perform_quack(self):
        print('Default quack')

#Below is a function which we will use to modify perform fly at run time

def rubber_fly():
    print("Rubber duck flies")


def main():

    rubberduck=Duck2()
    rubberduck.perform_fly()
    rubberduck=Duck2(rubber_fly)
    rubberduck.perform_fly()

# if __name__=='__main__':
#     main()



# In case we want the function assigned during run time to use the attributes of the object we can define it in a different way

import types

class Duck3:
    def __init__(self,name,fly=None,quack=None):
        if fly!=None:
            self.perform_fly=types.MethodType(fly,self)
        if quack!=None:
            self.perform_quack=types.MethodType(quack,self)
        self.name=name
        
    
    def perform_fly(self):
        print('Default fly')
    
   
    def perform_quack(self):
        print('Default quack')
 
    

def rubber_fly2(self):
    print(f"Rubber duck {self.name} flies")



def main2():
    rubberduck=Duck3(name='ducky',fly=rubber_fly2)
    rubberduck.perform_fly()

if __name__=="__main__":
    main2()

    
