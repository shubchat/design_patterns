# A command pattern allows us to decouple the requestor and the implementer objects so that diverse implementations can be used with similar requestor or front end interfaces.
#It can be used as a replacement for a callback
# examples:
# A IOT remote which has eight slots for eight functions now each of these eight slots/switches can do eight things but we can keep the slots and functions decoupled for convenience and flexibility of implementation

#Lets try and implement a remote control with a on/off switch

from abc import ABC,abstractmethod

class Command(ABC):

    @abstractmethod
    def execute():
        pass


class LightOn(Command):

    @staticmethod
    def execute():
        Light.on()
    
    @staticmethod
    def undo():
        Light.off()

class LightOff(Command):

    @staticmethod
    def execute():
        Light.off()
    
    @staticmethod
    def execute():
        Light.on()



class Light:

    def on():
        print("Light On")
    
    def off():
        print("Light off")



# Lets now design a simple remote controll with one button


class SimpleRemoteControl:

    def set_slot(self,command):
        self.slot=command
    
    def button_pressed(self):
        self.slot.execute()
    
    def undo(self):
        self.slot.undo()










