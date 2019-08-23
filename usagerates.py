from bs4 import BeautifulSoup
from urllib import request
import requests
from urllib.error import HTTPError
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt


url = 'https://www.basketball-reference.com/teams/GSW/2019.html'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

column_headers = [th.text for th in soup.findAll('tr', limit=2)[0].findAll('th')]
#print(column_headers)

data_rows = soup.findAll('tr')[1:]
#print(data_rows)

player_data = []  # create an empty list to hold all the data

for i in range(len(data_rows)):
    player_row = []

    for td in data_rows[i].findAll('td'):
        player_row.append(td.text)


    player_data.append(player_row)
print(player_data)
