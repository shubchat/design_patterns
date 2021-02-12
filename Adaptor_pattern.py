# The pattern is to be used when we want to change the functions of a class so that it is useful for a client
#It’s very often used in systems based on some legacy code. In such cases, Adapters make legacy code work with modern classes.

#Lets use a coffee kettle example which is manufactured for US use but needs to be used now in europe

# Client

class Kettle:

    def __init__(self,electric_connection):
        self.electric_connection=electric_connection

    def boil(self):
        if self.electric_connection.voltage()>100:
            print("SOS!Kettle has burnt")
        elif self.electric_connection.voltage()<20:
            print("Not enough voltage to run the kettle")
        else:
            print("Time for coffee!")


#Europe electricity

class Europe:

    @staticmethod
    def voltage():
        return 120


#Now the adaptor

class Adaptor:

    def __init__(self,electric_connection):
        self.electric_connection=electric_connection

    def voltage(self):
        return 90



#Below is how the kettle needs to be used so that we have the correct voltage

def main():
    kettle=Kettle(Adaptor(Europe))
    kettle.boil()


if __name__=='__main__':
    main()