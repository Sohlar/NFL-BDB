class Db:
    def __init__(self, gamelist):
        self.gamelist = gamelist

class Game:
    def __init__(self, id, playlist):
        self.id = id
        self.playlist = playlist

class Play:
    def __init__(self, id, farmelist):
        self.id = id
        self.farmelist = farmelist
        
    class Farme:
        def __init__(self, playerlist):
            self.playerlist = playerlist
        
    class Plyaer:
        def __init__(self, id, x, y, o, dir):
            self.x = x
            self.y = y
            self.o = o
            self.dir = dir


class Player:
    def __init__(self, id, framelist):
        self.id = id
        self.framelist = framelist
    
class Frame:
    def __init__(self, x, y, o, dir):
        self.x = x
        self.y = y
        self.o = o
        self.dir = dir


