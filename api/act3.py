# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 17:56:04 2021

@author: UniverSapphireLotus
"""


from pandas.io.json import json_normalize
import requests
import pandas as pd
import numpy as np
import time


my_api='RGAPI-884b56ef-0a40-4dbc-8836-603d4d4734a3'
vi= pd.read_csv('ID_games_IRON.csv')



#vi= vi[['puuid', 'tier', 'rank']]

print(vi)





cait= pd.DataFrame()

jinx=[]
for i, series in vi.iterrows():
    
    #https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/qkND6bt8PlMadELT_lVvTOu_l_bCUGFaT_dt3jX7KChm0lDNgquB_2IObwtxfDEY9DCPVetNCEN-RA/ids?type=ranked&start=0&count=20
    call= 'https://americas.api.riotgames.com/lol/match/v5/matches/'+series['IDgames']+'/?&api_key=' + my_api
    #req= requests.get(call)
    print(call)
    
    
    #print(req.status_code) 
    req= requests.get(call)
    print(req)
    
    
    print(req.status_code)
    if req.status_code==200:
        #print(req.json())
        #djson= json_normalize(req.json())
        #dataf= pd.DataFrame({'IDgames':req.json()})
        try:
            djson= json_normalize(req.json())
            dataf= pd.DataFrame(djson)
            #puuid.loc[:, 'tier'] = ga.at[0,'tier']
            dataf.loc[: ,'tier'] = series['tier']
            dataf.loc[: ,'rank'] = series['rank']
            cait= pd.concat([cait,dataf], ignore_index=True)
        except:
            time.sleep(2)
    else:
        jinx.append(series)
  
for series in jinx:
    #https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/qkND6bt8PlMadELT_lVvTOu_l_bCUGFaT_dt3jX7KChm0lDNgquB_2IObwtxfDEY9DCPVetNCEN-RA/ids?type=ranked&start=0&count=20
    call= 'https://americas.api.riotgames.com/lol/match/v5/matches/'+series['IDgames']+'/?&api_key=' + my_api
    #req= requests.get(call)
    print(call)
    
    
    #print(req.status_code) 
    req= requests.get(call)
    print(req)
    
    
    print(req.status_code)
    if req.status_code==200:
        #print(req.json())
        #djson= json_normalize(req.json())
        #dataf= pd.DataFrame({'IDgames':req.json()})
        try:
            djson= json_normalize(req.json())
            dataf= pd.DataFrame(djson)
            #puuid.loc[:, 'tier'] = ga.at[0,'tier']
            dataf.loc[: ,'tier'] = series['tier']
            dataf.loc[: ,'rank'] = series['rank']
            cait= pd.concat([cait,dataf], ignore_index=True)
        except:
            time.sleep(2)

        
  
    
    
cait.to_csv('DATA_games_IRON.csv')