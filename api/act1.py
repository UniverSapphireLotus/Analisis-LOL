# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 12:58:34 2021

@author: UniverSapphireLotus
"""
from pandas.io.json import json_normalize
import requests
import pandas as pd
import numpy as np
import time


elo=['IRON', 'BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'DIAMOND']
rank=['IV', 'III', 'II','I']

elo=['IRON']
#rank=['IV']



my_api = 'R'

#chall = 'https://la1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key=' + my_api



data=[]

#ITERAR ELO EN PAGES, USEN 4
for i in elo:
    dat= pd.DataFrame()
    for j in rank:
        for k in range (1,2):
            call= 'https://la1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/'+str(i)+'/'+str(j)+'?page='+str(k)+'&api_key=' + my_api
            req= requests.get(call)
            djson= json_normalize(req.json())
            dataf= pd.DataFrame(djson)
            dat= pd.concat([dat,dataf])
            
            pass
    data.append(dat)
    
    dat.to_csv('summoner_IREON.csv')
            
            
'''
chall = 'https://la1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/DIAMOND/II?page=2&api_key=' + my_api

chali = 'https://la1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/DIAMOND/II?page=3&api_key=' + my_api

req = requests.get(chall)
challenger_df = json_normalize(req.json())
df = pd.DataFrame(challenger_df)
print(df)

join
'''


#challenger_df = challenger_df.sort_values('leaguePoints',ascending = False)

'''
print(data)
for i in data:
    print(i)
'''
data_summoners=[]

time.sleep(1)


for i in data:
    ga=i[['summonerName', 'tier','rank']]
    con=0
    #puuid=[]
    puuid= pd.DataFrame(columns=['puuid','summonerName', 'tier','rank'])
    
    error=[]
    for index, serie in ga.iterrows():
        call='https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+serie['summonerName']+'/?api_key=' + my_api
        req= requests.get(call)
        
        
        print(req.status_code)
        
        djson= json_normalize(req.json())
        dataf= pd.DataFrame(djson)
        
        #print(dataf.at[0,'puuid'])
        #puuid.append(dataf[['puuid']])
        #puuid.append(dataf.at[0,'puuid'])
        if req.status_code==200:
             #puuid.append(dataf)
            #pd.concat([puuid,dataf.at[0,'puuid']])
            #pd.concat([puuid,dataf[['puuid']]])
            #puuid= puuid.append({'puuid':dataf.at[0,'puuid']},ignore_index=True)
            puuid= puuid.append({'puuid':dataf.at[0,'puuid'],'summonerName':serie['summonerName'], 'tier':serie['tier'], 'rank':serie['rank']},ignore_index=True)
            #puuid= puuid.append({'puuid':dataf.at[0,'puuid'],'summonerName':serie['summonerName']},ignore_index=True)
        else:
            error.append(serie)
        
    print('gaaaaaaaa')
    print(error)
    for e in error:
        call='https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+e['summonerName']+'/?api_key=' + my_api
        req= requests.get(call)
        djson= json_normalize(req.json())
        dataf= pd.DataFrame(djson)
        
        if req.status_code==200:
            #puuid.append(dataf)
            #puuid.append(dataf.at[0,'puuid'])
            puuid= puuid.append({'puuid':dataf.at[0,'puuid'],'summonerName':e['summonerName'], 'tier':serie['tier'], 'rank':serie['rank']},ignore_index=True)
            
    
    
    #puuid['tier']='IRON'
    #puuid.loc[:, 'tier'] = ga.at[0,'tier']
    #puuid['rank']='IV'
    #puuid.loc[:, 'rank'] = ga.at[0,'rank']
    
    
    
       
        #print(len(puiid))
        
    #ga.join(dataf[[]])
    print(puuid)
        
        
    
    data_summoners.append(ga)
    #elohell= ga.get_value(0,'tier')
    #ga.to_scv('game'+elohell+'.csv')

    
print(data_summoners)

#vi.to_csv('elo_IREON.csv')
puuid.to_csv('elo_IREON.csv')

