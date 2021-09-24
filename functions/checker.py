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

def main_page_check(team,url,headers):
    req = requests.get(home_url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    
    game_url = None

    for a in soup.find_all('a', href=True):
        if a['href'].find(team) > 0:
            game_url = str(a).split(' ')[2][6:-2]

            game_url = 'https://www.goal.com/'+str(game_url)
            
    
    
    return game_url

def game_page_check(game_url,headers,player,home_away):
    req = requests.get(game_url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    
    if home_away=='home':
        goal_list = [x.replace('</div>','') for x in str(soup.find_all('div', attrs={'class': 'widget-match-header__scorers-names widget-match-header__scorers-names--home'})).split('<div>')[1:]]
    else:
        goal_list = [x.replace('</div>','') for x in str(soup.find_all('div', attrs={'class': 'widget-match-header__scorers-names widget-match-header__scorers-names--away'})).split('<div>')[1:]]

    
    return goal_list

def game_checker(game_url,headers,player,game_over=False):
    req = requests.get(game_url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    
    goal_list_compare = []
    #goal_list = game_page_check(game_url,headers,player)
    #print(goal_list);print(len(goal_list))

    print(str(soup.find_all('div', attrs={'class': 'widget-match-header__state'})).split(' ')[2].replace('<span>','').replace('</span>',''))

    while str(soup.find_all('div', attrs={'class': 'widget-match-header__state'})).split(' ')[2].replace('<span>','').replace('</span>','') != 'FT':
        #print(goal_list);print(goal_list_compare)

        print(str(soup.find_all('div', attrs={'class': 'widget-match-header__state'})).split(' ')[2].replace('<span>','').replace('</span>',''))
        
        goal_list = game_page_check(game_url,headers,player,home_away)


        if len(goal_list)==len(goal_list_compare):
            #goal_list = []
            print('same')
            del soup
            time.sleep(30)
            req = requests.get(game_url, headers)
            soup = BeautifulSoup(req.content, 'html.parser')
            
        elif goal_list[-1].split(' ')[1]==player:
            goal_list_compare = goal_list.copy()

            print('GOAL!!!!!')
            goal_time = goal_list[-1].split(' ')[2].replace('(','').replace(')','')+str("'")
            
            tweeter(filename,enemy,goal_time)
            print(filename,enemy,goal_time)
            #goal_list = []
            del soup
            time.sleep(60)
            req = requests.get(game_url, headers)
            soup = BeautifulSoup(req.content, 'html.parser')
            
        else:
            #goal_list = []
            goal_list_compare = goal_list.copy()
            print('same')
            del soup
            time.sleep(30)
            req = requests.get(game_url, headers)
            soup = BeautifulSoup(req.content, 'html.parser')