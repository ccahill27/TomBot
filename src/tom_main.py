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


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

filename = '../images/distracted_sm.png'


team = 'borussia-dortmund'
team_upper = 'Borussia Dortmund'
#team = 'norway'
#team_upper = 'Norway'
player = 'Haaland'
#home_url = 'https://www.goal.com/en-us/results/2021-08-14'

#team = 'antwerp'
#team_upper = 'Antwerp'
#player = 'Frey'
home_url = 'https://www.goal.com/en-us/live-scores'
url_save_list = []




sys.path.insert(1, '../functions')

from checker import main_page_check, game_page_check, game_checker
from clock_t import time_start
from tweeter import tweeter


while True:
    print('beginning loop')
    print('checking url')
    print(team_upper,player)
    game_url = main_page_check(team,home_url,headers)
    if game_url==None:
        print('no URL')
    else:
        print(game_url)
    if (game_url!=None):
        req = requests.get(game_url, headers)
        main_soup = BeautifulSoup(req.content, 'html.parser')

        if str(main_soup.find_all('div', attrs={'class': 'widget-match-header__state'})).split(' ')[2].replace('<span>','').replace('</span>','')=='Today':
            started='NO'
        else:
            started='YES'

        if str(main_soup.find_all('div', attrs={'class': 'widget-match-header__state'})).split(' ')[2].replace('<span>','').replace('</span>','')=='FT':
            game_finished='YES'
        else:
            game_finished='NO'

        team_a = [x.replace(' Live Commentary','') for x in str(main_soup.find_all(["h1"])).split('"')[1].split(',')[0].split(' v ')][0]
        team_b = [x.replace(' Live Commentary','') for x in str(main_soup.find_all(["h1"])).split('"')[1].split(',')[0].split(' v ')][1]
        team_a = team_a.replace('Match Preview','')
        team_b = team_b.replace('Match Preview','')
        
        if team_a == str(team_upper):
            enemy = team_b
            home_away = 'home'
        else:
            enemy = team_a
            home_away = 'away'

        print(team_a)
        print(team_b)
        print(enemy)
        print(home_away)
        
        if game_finished=='NO':
            if started=='NO':
                hr_start,min_start = time_start(game_url,headers)
                print('Waiting until '+str(hr_start)+':'+str(min_start))
                today = datetime.date.today()        
                pause.until(datetime.datetime(int(str(pd.to_datetime(today))[0:4]),\
                                            int(str(pd.to_datetime(today))[5:7]),\
                                            int(str(pd.to_datetime(today))[8:10]),
                                            hr_start,min_start))
                
                print('Game Started')
                print(datetime.datetime.now())
            else:
                print('Game Started')
                print(datetime.datetime.now())        
            game_checker(game_url,headers,player,game_over=False)
        else:
            print('game over')
            print(datetime.datetime.now())
            now = datetime.datetime.now()
            manana0 = datetime.datetime.now()+timedelta(days=1)
            manana = datetime.datetime(int(manana0.year),int(manana0.month),int(manana0.day),6,20)
            print('sleeping until '+str(manana))
            print((manana-now).seconds)
            time.sleep((manana-now).seconds)
        
    else:
        print('no game today')
        print(datetime.datetime.now())
        now = datetime.datetime.now()
        manana0 = datetime.datetime.now()+timedelta(days=1)
        manana = datetime.datetime(int(manana0.year),int(manana0.month),int(manana0.day),6,20)
        print('sleeping until '+str(manana))
        print((manana-now).seconds)
        time.sleep((manana-now).seconds)
        #del game_url
        #del main_soup

        print(datetime.datetime.now())

        
        #sys.stdout = old_stdout