# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 07:52:31 2022

@author: UniverSapphireLotus
"""
import pandas as pd
import matplotlib.pyplot as ptl
import seaborn as sns


cup= pd.read_csv('Game Match\PLATINUM_GAMES_macth_data.csv')


cup1= pd.read_csv('Game Data\PLATINUM_GAMES_game_data.csv')
cup2= pd.read_csv('Bans\PLATINUM_GAMES_bans_data.csv')

#cup= cup.head(400)
#cup1= cup1.head(400)
#cup2= cup2.head(400)

def get_list_elo():
    return ['IRON', 'BRONZE', 'SILVER', 'GOLD', 'PLATINUM']

def get_list_champ():

    return cup.groupby('championName',as_index = False).size()['championName'].values.tolist()

def box_dens_corr_champ(champ, elo):
    #cake= cup.groupby('championName').size()

    champion= champ
    cup= pd.read_csv('Game Match\{}_GAMES_macth_data.csv'.format(elo))    
    cake= cup[['championName', 'totalDamageDealt','totalDamageTaken', 'totalHeal', 'totalHealsOnTeammates']]
    cake= cake.loc[cake['championName'].isin([champion])]
    
    violet= cup[['championName', 'totalDamageDealt','totalDamageTaken', 'totalHeal', 'totalHealsOnTeammates', 'kills', 'assists', 'deaths', 'goldEarned']]
    violet= violet.loc[violet['championName'].isin([champion])]
    
    data= cup.loc[cup['championName'].isin([champion])]
    
    total_game= data.shape[0] 
    total_wins= data.loc[data['win']==True].shape[0] /data.shape[0] 
    
    return [cake, violet, total_game, total_wins]


#valores= box_dens_corr_champ("Jhin")