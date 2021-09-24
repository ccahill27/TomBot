import requests
from bs4 import BeautifulSoup
import time
import pause
import pandas as pd
import sys
import tweepy

import datetime
from datetime import timezone
from datetime import timedelta, date

def time_start(game_url,headers):
    req = requests.get(game_url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    am_pm = str(soup.find_all('div', attrs={'class': 'widget-match-header__status'})).split(' ')[3].replace('<span>','').replace('</span>','')
    kickoff = str(soup.find_all('div', attrs={'class': 'widget-match-header__status'})).split(' ')[2].replace('<span>','').replace('</span>','')
    print('kickoff',kickoff)
    print('am_pm',am_pm)

    if (am_pm =='PM') & (int(kickoff.split(':')[0]) != 12):
        kickoff = str(int(kickoff.split(':')[0])-3+12)+':'+str(kickoff.split(':')[1])
    elif (am_pm =='PM') & (int(kickoff.split(':')[0]) == 12):
        kickoff = str(int(kickoff.split(':')[0])-3)+':'+str(kickoff.split(':')[1])
        am_pm = 'AM'
    else:
        kickoff = str(int(kickoff.split(':')[0])-3)+':'+str(kickoff.split(':')[1])
    print('kickoff',kickoff)
    print('am_pm',am_pm)
        
    hr_start = int(kickoff.split(':')[0])
    min_start = int(kickoff.split(':')[1])
    print(hr_start)
        
    return hr_start, min_start