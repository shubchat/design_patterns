# We will write an observer pattern where there is an observable and multiple observers based on whether it is a push or GET request based app we will need to design the pub sub model
# Examples:Weather subscription service,Twitter pub/sub

# Example 1:Weather subscription service

from abc import ABC,abstractmethod

class Observable(ABC):


    @abstractmethod
    def addsub(self)->None:
        pass
    
    @abstractmethod
    def removesub(self):
        pass

    @abstractmethod
    def notifychange(self):
        pass

    @abstractmethod
    def notifylogic(self):
        pass



class WeatherData(Observable):

    subscribers=['a','b','c']




    def __init__(self,subscriber,new_sub=False,remove_sub=False):
        self.subscriber=subscriber
        self.new_sub=new_sub
        self.remove_sub=remove_sub
        self.managesub()
        self.gettemp()
        self.gethumidity()
        self.getuv()

        

    def gettemp(self):
        self.temp=10
 
 
    def gethumidity(self):
        self.humidity=5

   
    def getuv(self):
        self.uv=1
       
    
    def addsub(self)->'Message that subscriber has been added':
        self.subscribers.append(self.subscriber)
        return "Subscriber has been added"

   
    def removesub(self)->'Message that subscriber has been removed':
        self.subscribers.remove(self.subscriber)
        return "Subscriber has been removed"

    def managesub(self):
        if self.new_sub:
            self.addsub()
        if self.remove_sub:
            self.removesub()

    
    @property
    def notifylogic(self):
        return True 


    def notifychange(self):
        if (self.notifylogic and self.subscriber in self.subscribers):
            return {'temp':self.temp,'humidity':self.humidity,'uv':self.uv}
        else:
            pass







# Below is how it will look at a suscriber system


class Subscriber(ABC):

    @abstractmethod
    def update(self):
        pass



class SubA(Subscriber):

    def __init__(self):
        self.name='SubA'
       
    def update(self):
        if self.name in WeatherData.subscribers:
            return WeatherData(self.name).notifychange()




