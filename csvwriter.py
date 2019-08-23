import pandas as pd
import pickle
import csv

lineup = pickle.load(open("gameid.pickle", "rb" ))
big = pickle.load(open("masterr_data.pickle", "rb"))


goodData = []

headers = [['Game_ID', 'Player_ID', 'OffRtg', 'DefRtg']]




for game in big:
    for team in big[game]:
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


            row = [game, player, off_rating, def_rating]

            goodData.append(row)

with open('bigboy.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(headers)
    writer.writerows(goodData)
csvFile.close()
"""
with open('Valley_Boyz_Hackers_Q1_BBALL') as in_file:
    with open('bigboy.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if row:
                writer.writerow(row)
"""
