# from decorator_pattern import *

# if __name__=="__main__":    
#     # add()
#     greet()


from abc import ABC,abstractmethod


class Test(ABC):

    @abstractmethod
    def yes():
        pass
    
    def no(self):
        print("No")


class Test2(Test):
    def yes(self):
        print("Yes")



    