import pandas as pd
import pickle

team_dict = {'8362dfecb7412f12a12713852d2ae566': 'CAVALIERS', 'cd45058739ed0ac8229849c6249aad48': 'WARRIORS', '0370a0d090da0d0edc6319f120187e0e': 'None', None: 'None',}


game1_dict = {'722a380c9b59ef42226e8d392824dcb9': 'George Hill', '7f438c18058290903c46dfe9d71bd68a': 'JR Smith',
                'fb64ca4b8beaf4c4c6e4575fe2f3abd7': 'LeBron James', '95920e4bf5b6c15ba8dffbf959b38ba5': 'Kevin Love',
                'ef8b068ab7ac9d387b256404acd24cd5':'Tristan Thompson', '1a6703883f8f47bb4daf09c03be3bda2': 'Stephen Curry',
                '31598ba01a3fff03ed0a87d7dea11dfe': 'Klay Thompson', '3626b893fc73a5cbd67d1ea48a5c7039': 'Kevin Durant',
                'a1591595c04d12e88e3cb427fb667618': 'Draymond Green', '6f6a807d57aae8f651222523dc82dc35': 'Kevon Looney',
                '3d75035d20b173a867d4bf32c8a58f0b': 'Jordan Bell', '0b978fcfa7f2ec839c563a755e345ff8': 'Nick Young',
                '52c6125836c465f4ac5232121dacb49d': 'Shaun Livingston', '821887f9a002be16b5f79729fae59e01': 'Pat McCaw',
                '255fe2a8be0ed5c06dd99969ab4fea55': 'David West', 'bfef77a3e57907855444410d490e7bfd': 'Javale McGee',
                '1dabb767e07d0aa702ee58d41c15eab1' : 'Jeff Green', 'e49b2cc3f9aacd500b11a35b1c57112d': 'Jordan Clarkson',
                '32c044aa84d75ccd78c3c9f2aeb33bd9' : 'Kyle Korver', '942a84f05f4ab956125f68ec0963481f': 'Larry Nance Jr.',
                '0370a0d090da0d0edc6319f120187e0e' : 'None', 'f5f0b0fd479d7c889872298f95c3d810': 'Quinn Cook', '22fab2ecad98e9fed46efe57558bc41f': 'Cavs Player',
                'fbcda0bcb861e4726ca8871b8965ede4': 'Warriors Player', '619d3e44dc84b366bd685de3e94b3bec': '2KGeneric',
                'c950aaad2e56c87e9ac7281016d37cb6': "2KGeneric", '36fdadf436b164ee29174c8e1fde7271': "2KGeneric",
              '8c7a7249d80b1489594b3a2a87f3f19d': '2KGeneric', 'f3d6e924c2736c9e5771b0784e31c2df': 'random',
              '18a823379f2bf4e4be8b419698cde91c': 'random', '94e99d76e87ee926faab66d382b3a955': 'random',
              'ff59dc439c6c323320bc355afe884fcb': 'random', '14de632b07100527b0ced12fd4eeffb7': 'random'
                }


lineup = pickle.load(open("gameid.pickle", "rb" ))
big = pickle.load(open("masterr_data.pickle", "rb"))

haha = []
for game in big:
    for team in big[game]:
        for player in big[game][team]:
            if player == 'fb64ca4b8beaf4c4c6e4575fe2f3abd7':
                if big[game][team][player]['off_count'] == 0:
                    off_rating = 0
                else:
                    off_rating = (big[game][team][player]['off_pnts']/big[game][team][player]['off_count'])*100
                    off_rating = round(off_rating, 2)

                if big[game][team][player]['def_count'] == 0:
                    def_rating = 0
                else:
                    def_rating = (big[game][team][player]['def_pnts']/big[game][team][player]['def_count'])*100
                    def_rating = round(def_rating,2)

                print(game, off_rating, def_rating)

haha.sort(reverse=True)
print(haha)


"""
for game in big:
    if game == '3ce947db2df86b08a40b7526e2faaccb':
        for team in big[game]:
            print("       " + team_dict[team])
            for player in big[game][team]:
                if big[game][team][player]['off_count'] == 0:
                    off_rating = 0
                else:
                    off_rating = (big[game][team][player]['off_pnts']/big[game][team][player]['off_count'])*100
                    off_rating = round(off_rating, 2)

                if big[game][team][player]['def_count'] == 0:
                    def_rating = 0
                else:
                    def_rating = (big[game][team][player]['def_pnts']/big[game][team][player]['def_count'])*100
                    def_rating = round(def_rating,2)
                if big[game][team][player]['off_count'] != 0:
                    print(game1_dict[player].upper() + ":   ORTG-  " + str(off_rating) + "    DRTG-  " + str(def_rating))
                    print(big[game][team][player])
"""

playbyp = pd.read_csv('Play_by_Play.txt', sep= "\t")


games = playbyp[['Game_id']]
games = games.dropna().values

num = playbyp[['Event_Num']]
num = num.dropna().values

period = playbyp[['Period']]
period = period.dropna().values

event = playbyp[['Event_Msg_Type']]
event = event.dropna().values

action = playbyp[['Action_Type']]
action = action.dropna().values

pctime = playbyp[['PC_Time']]
pctime = pctime.dropna().values

opt1 = playbyp[['Option1']]
opt1 = opt1.dropna().values

opt2 = playbyp[['Option2']]
opt2 = opt2.dropna().values

opt3 = playbyp[['Option3']]
opt3 = opt3.dropna().values

"""
for i in range(len(event)):
    if event[i][0] == 20 and games[i][0] == '3ce947db2df86b08a40b7526e2faaccb':
        print(num[i][0], event[i][0], pctime[i][0])
        print(num[i+1][0], event[i+1][0], pctime[i+1][0])
        print("")



opt2dic = {}
for i in range(len(event)):
    if games[i][0] == "2877e9e9980619126420db0163ee0779":
        if event[i][0] == 6 and action[i][0] == 11:
            print(games[i][0], num[i][0])

print(opt2dic)
reee = 0
unkdict = {}

yooyoo = ''
for i in range(len(event)):
    if period[i][0] == 5:
        if yooyoo != games[i][0]:
            yooyoo = games[i][0]
            print(games[i][0])



unkdict.sort()
#print(event[i-1][0],action[i-1][0])

team1_lineup = ['','','','','']
team2_lineup = ['','','','','']

for key in lineup[games[0][0]]:
    if lineup[games[0][0]][key][2] == 1:
        print("hi")
"""
