# This pattern is writting a class or a simple interface which simplifies complications underneath a sophisticated system
# Example a home theatre system with multiple machines for doing something example amplifier,screen.DVD etc can be aggregated into movie.on(),movie.off()
#Another benefit of this is even if classes underneath change it won't impact how the client uses the interface


class Amplifier:
    
    @staticmethod
    def on():
         print("Amplifier on")
    
    @staticmethod
    def off():
        print("Amplifier off")


class DVDPlayer:
    
    @staticmethod
    def on():
        print("DVDPlayer on")
    
    @staticmethod
    def off():
        print("DVDPlayer off")


class Screen:
    
    @staticmethod
    def on():
        print("Screen on")
    
    @staticmethod
    def off():
        print("Screen off")

class WindowShades:

    @staticmethod
    def up():
        print("Shades Up")
    
    @staticmethod
    def down():
        print("Shades down")


# Now below is the facade class for the client to use to watch a movie

class HomeTheatre:

    def __init__(self,Amplifier,DVDPlayer,Screen,WindowShades):
        self.Amplifier=Amplifier
        self.DVDPlayer=DVDPlayer
        self.Screen=Screen
        self.WindowShades=WindowShades


    def watchmovie(self):
        self.Amplifier.on()
        self.DVDPlayer.on()
        self.Screen.on()
        self.WindowShades.down()
    
    def stopmovie(self):
        self.Amplifier.off()
        self.DVDPlayer.off()
        self.Screen.off()
        self.WindowShades.up()



# Below functions are simulating the clicks on remote

def click_watch_movie(theatre):
    theatre=theatre(Amplifier,DVDPlayer,Screen,WindowShades)
    return theatre.watchmovie()



def click_stop_movie(theatre):
    theatre=theatre(Amplifier,DVDPlayer,Screen,WindowShades)
    return  theatre.stopmovie()






    


