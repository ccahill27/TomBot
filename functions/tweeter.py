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

def tweeter(filename,enemy,goal_time):
    #filename = 'C:/Users/chris/Documents/dortmond/images/distracted_sm.png'

    key_list = pd.read_csv('../src/API_info.csv')
    
    API_key = str(key_list.API_key[0])
    API_secret_key = str(key_list.API_secret_key[0])
    Bearer_token = str(key_list.Bearer_token[0])
    ACCESS_TOKEN = str(key_list.ACCESS_TOKEN[0])
    ACCESS_TOKEN_SECRET = str(key_list.ACCESS_TOKEN_SECRET[0])
    
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(API_key, API_secret_key)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        out = "Authentication OK"
    except:
        out = "Error during authentication"
        
    #api.update_with_media(filename, status='GOAL!!! Haaland goal vs. '+str(enemy)+ ' at '+str(goal_time))
    api.update_with_media(filename, status='GOAL!!! Haaland goal vs. '+str(enemy)+ ' at '+str(goal_time)+ ' @tgrant20 @PhillyPJ @cahillmath')
    
    return out