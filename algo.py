from Classes import *
#DE (x, y) distance from QB (x,y) - Create Line
#Minimum distance from Tackle (x,y) to Line (x,y) 
#Pressure Zone = pi * (distance from Tackle to QB)^2

def playalgo(play):
    for frames in play.farmelist:
        for players in frames.playerlist:
            x = players[frames].x
            y = players[frames].y
            dir = players[frames].dir
            o = players[frames].o
            #plot(x, y)


                
