import pandas as pd
import dask.dataframe as dd
import numpy as np
import time
from Classes import *
import algo


def parse_csv():
    start=time.time()

    #Create dataframe of all players with useful data
    players = pd.read_csv('C:/Users/drew/Learning/nfldata/env/data/players.csv', usecols=['nflId', 'officialPosition', 'displayName'])
    #Tackles only" 
    TackleList = pd.DataFrame(players.loc[players['officialPosition'].isin(['T'])])
    #OffensiveLine dataframe has index numbers from "players" => We reset new OL dataframe indexes
    TackleList.reset_index(drop = True, inplace=True)

    QBList = pd.DataFrame(players.loc[players['officialPosition'].isin(['QB'])])
    #Quarterback dataframe has index numbers from "players" => We reset new OL dataframe indexes
    QBList.reset_index(drop = True, inplace=True)

    DEList = pd.DataFrame(players.loc[players['officialPosition'].isin(['DE'])])
    #Defensive End dataframe has index numbers from "players" => We reset new OL dataframe indexes
    TackleList.reset_index(drop = True, inplace=True)

    #scouting_data = pd.read_csv('data/pffScoutingData.csv')
    tracking_data2 = pd.read_csv('C:/Users/drew/Learning/nfldata/env/data/week1.csv', header=0)

    #drops all entries not in Tackle list
    tracking_data2['nflId'].where(tracking_data2['nflId'].isin(TackleList["nflId"]), 0, inplace=True)
    tracking_data2 = tracking_data2.drop(tracking_data2.loc[tracking_data2['nflId'] == 0].index)
    tracking_data2.reset_index(drop=True, inplace=True)
    ballsnaplist = tracking_data2.index[tracking_data2['event'] == 'ball_snap'].tolist()

    print(str("starting " + str(len(ballsnaplist))))
    


    #currentDataLoc = tracking_data2.iloc[y]

    #Goes to each Ball Snap
    currentPlay = 0
    currentGame = 0


    gamelist = []

    for i in range(len(ballsnaplist)):

        if currentGame != tracking_data2.iloc[ballsnaplist[i]].gameId:
            #Updates current play
            currentGame = tracking_data2.iloc[ballsnaplist[i]].gameId
            #Creates new Play Object
            game = Game(currentGame, [])
            gamelist.append(game)
            print(game)

        if currentPlay != tracking_data2.iloc[ballsnaplist[i]].playId:
            #Updates current play
            currentPlay = tracking_data2.iloc[ballsnaplist[i]].playId
            #Creates new Play Object
            play = Play(currentPlay, [])
            game.playlist.append(play)

        frameindex = ballsnaplist[i] + 1

        farme = Play.Farme([])
        while tracking_data2.iloc[frameindex].event == 'None':
            play.farmelist.append(Play.Farme())
            playerlist.append(Play.Plyaer(tracking_data2.iloc[frameIndex].x, tracking_data2.iloc[frameIndex].y, tracking_data2.iloc[frameIndex].o, tracking_data2.iloc[frameIndex].dir))















#########################################################
        #Create Player object
        player = Player(tracking_data2['nflId'], [])
        #Get first frame of play
        frameIndex = ballsnaplist[i] + 1
        #Creating the list of frames for each snap
        while tracking_data2.iloc[frameIndex].event == 'None':
            #print(tracking_data2.iloc[frameIndex])
            #Add frame to Player's list of frames
            player.framelist.append(Frame(tracking_data2.iloc[frameIndex].x, tracking_data2.iloc[frameIndex].y, tracking_data2.iloc[frameIndex].o, tracking_data2.iloc[frameIndex].dir))
            frameIndex += 1
        #Adds Player to the Play
        play.playerlist.append(player)
        #Checks if new Game       

    algo.gamealgo(gamelist)

    end=time.time()
    print("Time: " + str(end - start))