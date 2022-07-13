# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 16:58:37 2022

@author: UniverSapphireLotus
"""

import pandas as pd
import matplotlib.pyplot as ptl
import seaborn as sns


cup= pd.read_csv('Game Match\PLATINUM_GAMES_macth_data.csv')


cup1= pd.read_csv('Game Data\PLATINUM_GAMES_game_data.csv')
cup2= pd.read_csv('Bans\PLATINUM_GAMES_bans_data.csv')

cup= cup.head(400)
cup1= cup1.head(400)
cup2= cup2.head(400)

cake= cup.groupby('championName').size()

champion= 'Jhin'

cake= cup[['championName', 'totalDamageDealt','totalDamageTaken', 'totalHeal', 'totalHealsOnTeammates']]
cake= cake.loc[cake['championName'].isin([champion])]

violet= cup[['championName', 'totalDamageDealt','totalDamageTaken', 'totalHeal', 'totalHealsOnTeammates', 'kills', 'assists', 'deaths', 'goldEarned']]
violet= violet.loc[violet['championName'].isin([champion])]

sweet= cup[['championId', 'championName', 'totalDamageDealt','totalDamageTaken', 'totalHeal', 'totalHealsOnTeammates', 'participantId','win', 'metadata.matchId']]
anabell= pd.crosstab(sweet['metadata.matchId'], sweet['participantId'])
#leonora= sweet.groupby(['metadata.matchId','participantId']).size().unstack('participantId', fill_value=0)
leye_wins= cup.loc[cup['win']==True].groupby(['championId'],as_index = False).agg(wins=('win', 'count')).merge(cup.groupby(['championId'],as_index = False).agg(total=('win', 'count')), on= 'championId', how = 'outer').fillna(0)
leye_wins['win_rate']= leye_wins['wins']/leye_wins['total']

leonora= sweet.pivot(index= 'metadata.matchId', columns='participantId', values= 'championId')

dici= pd.Series(leye_wins.win_rate.values,index=leye_wins.championId).to_dict()

leonora= sweet.pivot(index= 'metadata.matchId', columns='participantId', values= 'championId')

game_win_rate= leonora.iloc[:, :].replace(dici)

'''
#HITSO
fig=ptl.figure(figsize = (15,15))
ax=fig.gca()
cake.hist(ax=ax)
ptl.show()
#DENSIDAD
fig=ptl.figure(figsize = (15,15))
ax=fig.gca()
cake.plot(ax=ax, kind='density', subplots=True, layout=(2,2), sharex=False)
ptl.show()
'''
#DENSIDAD
f,axes = ptl.subplots(2,2, figsize=(15,15))
ordx= [0, 1, 0, 1]
ordy= [0, 0, 1, 1]
for column, ox, oy in zip(cake.iloc[:, 1:], ordx, ordy):
        sns.distplot(cake[column], ax=axes[ox, oy])
        
#CAJA
f,axes = ptl.subplots(2,2, figsize=(15,15))
ordx= [0, 1, 0, 1]
ordy= [0, 0, 1, 1]
for column, ox, oy in zip(cake.iloc[:, 1:], ordx, ordy):
        sns.boxplot(cake[column], ax=axes[ox, oy])
#CORR

correlation = violet.corr()
ptl.figure(figsize=(10,10))
ax=sns.heatmap(correlation, vmax=1, square=True, annot=True, cmap="viridis")
ptl.title("MATRIZ DE CORRELACIÓN")
ptl.show()



