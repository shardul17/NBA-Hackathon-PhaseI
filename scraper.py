import pandas as pd
import pickle

data = pd.read_csv('Game_Lineup.txt', sep= "\t")



player = data[['Person_id']]
player = player.dropna().values

period = data[['Period']]
period = period.dropna().values

teamid = data[['Team_id']]
teamid = teamid.dropna().values

status = data[["status"]]
status = status.dropna().values

gameid = data[["Game_id"]]
gameid = gameid.dropna().values

bigdict = {}
biggerdict = {}


team1 = ''
team2 = ''
for i in range(len(gameid)):
    if gameid[i][0] not in biggerdict:
        team1 = teamid[i][0]
        j = i
        if teamid[i+1][0] == teamid[i][0]:
            for j in range(2, 10):
                if teamid[i+j][0] != teamid[i][0]:
                    team2 = teamid[i+j][0]
                    break
                else:
                    continue
        else:
            team2 = teamid[i+1][0]
        biggerdict[gameid[i][0]] = {0:{team1:[player[i][0]],team2:[]}, 1:{team1:[],team2:[]}, 2:{team1:[],team2:[]}, 3:{team1:[],team2:[]}, 4:{team1:[],team2:[]}, 5:{team1:[],team2:[]}}
    else:
        #biggerdict[gameid[i][0]][player[i][0]] = [status[i][0], teamid[i][0], period[i][0]]
        biggerdict[gameid[i][0]][period[i][0]][teamid[i][0]].append(player[i][0])

print(biggerdict)

with open('gameid.pickle', 'wb') as handle:
    pickle.dump(biggerdict, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('gameid.pickle', 'rb') as handle:
    b = pickle.load(handle)

print(biggerdict == b)

print(len(biggerdict))



"""
for i in range(len(player)):
    if player[i][0] not in bigdict:
        bigdict[player[i][0]] = {gameid[i][0]:[status[i][0], teamid[i][0], period[i][0]]}
    else:
        bigdict[player[i][0]][gameid[i][0]] = [status[i][0], teamid[i][0], period[i][0]]
"""
