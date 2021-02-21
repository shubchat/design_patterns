# The state pattern is used when we have a problem where there are multiple stages and there are different actions that might move you from one state to another it allows to simplify coding of states and the transitions and also allows for flexible code
#base

# We will start with the problem in the book of a gumball machine

from abc import ABC,abstractmethod
import random

class State(ABC):

    @abstractmethod
    def insert_quarter():
        pass

    @abstractmethod
    def eject_quarter():
        pass
    
    @abstractmethod
    def turn_crank():
        pass

    @abstractmethod
    def dispense():
        pass

class SoldState(State):

    def __init__(self,gumball_machine):
        self.gumball_machine=gumball_machine

    def insert_quarter(self):
        print("Please wait,We already have your quarter and cannot accept another one")
    
    def eject_quarter(self):
        print("Sorry!You already turned the crank")

    def turn_crank(self):
        print("turning twice will not get you another gumball")
    
    def dispense(self):
        self.gumball_machine.release_ball()
        
        if self.gumball_machine.get_count()>0:
            self.gumball_machine.set_state(self.gumball_machine.getNoQuarterState())
        
        else:
            print("Oops!out of gumballs!")
            self.gumball_machine.set_state(self.gumball_machine.getSoldOutState())


class NoQuarterState(State):

    def __init__(self,gumball_machine):
        self.gumball_machine=gumball_machine

    def insert_quarter(self):
        print("Thanks!For the quarter")
        self.gumball_machine.set_state(self.gumball_machine.getHasQuarterState())
    
    def eject_quarter(self):
        print("Sorry!You have not inserted the quarter yet")

    def turn_crank(self):
        print("Operation not allowed!")
    
    def dispense(self):
        print("Operation not allowed!")


class HasQuarterState(State):

    def __init__(self,gumball_machine):
        self.gumball_machine=gumball_machine
        self.random_winner=random.choice(['Winner','Looser'])

    def insert_quarter(self):
        print("Thanks!We already have a quarter")
    
    def eject_quarter(self):
        print("Ejecting your quarter ......")
        self.gumball_machine.set_state(self.gumball_machine.getNoQuarterState())

    def turn_crank(self):
        # print(self.random_winner)
        if self.random_winner!='Winner':
            print("Sorry you could not win this time!Better Luck next time.")
            self.gumball_machine.set_state(self.gumball_machine.getSoldState())
        else:
            print("Congrats you Won!")
            self.gumball_machine.set_state(self.gumball_machine.getWinnerState())

    def dispense(self):
        print("Operation not allowed!")


class SoldOutState(State):

    def __init__(self,gumball_machine):
        self.gumball_machine=gumball_machine

    def insert_quarter(self):
        print("Sorry!We are out of gumballs as of now")
    
    def eject_quarter(self):
        print("Operation not allowed!")

    def turn_crank(self):
        print("Operation not allowed!")

    def dispense(self):
        print("Operation not allowed!")


class WinnerState(State):

    def __init__(self,gumball_machine):
        self.gumball_machine=gumball_machine

    def insert_quarter(self):
        print("Operation not allowed!")
    
    def eject_quarter(self):
        print("Operation not allowed!")

    def turn_crank(self):
        print("Operation not allowed!")

    def dispense(self):
        
        self.gumball_machine.release_ball()
        
        if self.gumball_machine.get_count()>0:
            print("You are a winner,you get two gumballs")
            self.gumball_machine.release_ball() # We release another gumball if available
            self.gumball_machine.set_state(self.gumball_machine.getNoQuarterState())
        
        else:
            print("Oops!you can only have one gumball as we are out!")
            self.gumball_machine.set_state(self.gumball_machine.getSoldOutState())




class GumballMachine:

    def __init__(self,cnt_gumballs):
        self.cnt_gumballs=cnt_gumballs
        self.current_state=NoQuarterState(self)
    
       
    def release_ball(self):
        if self.cnt_gumballs>0:
            print("Gumball released!")
            self.cnt_gumballs+=-1
    
    def has_quarter_state(self):
        self.current_state=HasQuarterState(self)


    def get_count(self):
        return self.cnt_gumballs

    def set_state(self,state):
        self.current_state=state

    def getHasQuarterState(self):
        return HasQuarterState(self)
    
    def getNoQuarterState(self):
        return NoQuarterState(self)
    
    def getSoldState(self):
        return SoldState(self)

    def getSoldOutState(self):
        return SoldState(self)

    def getWinnerState(self):
        return WinnerState(self)

    
    

