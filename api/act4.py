# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
#import json1l[
import yaml
#import re
import timeit
import _thread 

from threading import Thread

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return



vi= pd.read_csv('DATA_games_PLATINUM.csv')

#vi= vi.head(5)

#vi= vi[['metadata.matchaId', 'info.gameDuration']]\

#print(rows)
#for col in vi.columns:
#    print(col) ra
    
vi= vi[['metadata.matchId', 'info.gameDuration', 'info.gameId', 
        'info.gameVersion', 'info.participants', 'info.teams', 'tier', 'rank']]



def transcend(cait):
    cupcake= pd.DataFrame()
    violyn= pd.DataFrame()
    powder= pd.DataFrame()
    
    
    
    for index, series in cait.iterrows():
        #print(type(series))
        #vi_kiramman.append(series.to_frame())
        #for i in series['info.teams']:
            #print(i)
            #print(type(i))
            #vi_kiramman.append(json.loads(i))
            #.replace(';',' ')
            #vi_kiramman.append(i.replace('[', '{').replace(']','}'))
            #{'bans': [
            #vi_kiramman.append(i.replace('[', '').replace(']',''))
            #'], '
            
        cup= list(series['info.teams'].replace("{'bans': [", '☺').replace("], ", '☺').split('☺'))
        #cupcake= list(re.split("{'bans': [|], ",i))
        cup.pop(0)
        cup[1] = cup[1][:-2]
        cup[-1] = cup[-1][:-1]
        
        cup[1]= list(cup[1].replace("}, ", '}}, ').split('}, '))
        cup[-1]= list(cup[-1].replace("}, ", '}}, ').split('}, '))
        
        cup[0]= list(cup[0].replace("}, ", '}}, ').split('}, '))
        cup[2]= list(cup[2].replace("}, ", '}}, ').split('}, '))
        #vi_kiramman.append(cup)
        
        
        #bon.pop(0)
        idt='100'
        for j in cup[0::2]:
            #sweet=pd.DataFrame()
            
            for k in j:
                #c=yaml.load(k)
                cake= pd.DataFrame(yaml.load(k), index=[0])
                #dataf.loc[: ,'tier'] = series['tier'
                cake.loc[: ,'teamId'] = idt
                cake.loc[: ,'metadata.matchId'] = series['metadata.matchId']
                
                #print(cake)
                #sweet= pd.concat([sweet,cake], ignore_index=True)
                #cupcake= pd.concat([cupcake,sweet], ignore_index=True)   
                cupcake= pd.concat([cupcake,cake], ignore_index=True)
            idt='200'
                                    
            #sweet= sweet.pivot(index='metadata.matchId',olumns='pickTurn', values='championId')
            #cupcake= pd.concat([cupcake,sweet], ignore_index=True)            
            #, 'styles': [        
            #vi_kiramman.append(json.loads(i.replace('[', '{').replace(']','}')))
        #bom= series['info.participants'][1:-1]
        vio= list(series['info.participants'][1:-1].replace(", {'assists'", "◘{'assists'").split("◘"))
        print (len(vio))
        
        for j in cup[1::2]:
            j[0]= list(j[0].replace("'objectives': {", '☺').split('☺'))[1]
            j[5]= j[5][:-1]
            j[6]= "{"+j[6]

            for k in range(0,6):
                j[k]= list(j[k].replace(": {", '☺{').split('☺'))
                j[k][1]= cake= pd.DataFrame(yaml.load(j[k][1]), index=[0])
                #j[k][j[k][0]+'firts', j[k][1]+'kills']= cake['firts', 'kills']
                tagi= j[k][0][0:-1]
                j[k]= j[k][1].rename({'first':'first'+ tagi, 'kills':tagi +'Kills'}, axis=1)
            
            print(j)
            j[6]= pd.DataFrame(yaml.load(j[6]), index=[0])
            cake= pd.concat([j[0], j[1], j[2], j[3], j[4], j[5], j[6]], axis=1)
            cake.loc[: ,'metadata.matchId'] = series['metadata.matchId']
            cake.loc[: ,'eloRank'] = 'PLATINUM'
            powder= pd.concat([powder,cake], ignore_index=True)
            

        for j in vio:
            j= list(j.replace(" 'perks': ", '◘').replace("}]}, ", '◘').split("◘"))
            #print(j)
            #lyn= yaml.load(j[0]+j[2])
            lyn= pd.DataFrame(yaml.load(j[0]+j[2]), index=[0])
            lyn.loc[: ,'metadata.matchId'] = series['metadata.matchId']
            violyn= pd.concat([violyn, lyn], ignore_index= True)
            
    return [cupcake, violyn, powder]



#ACTI= vi[['metadata.matchId', 'info.teams', 'info.participants']]


vi_kiramman= '''
import pandas as pd
import _thread 

vi= pd.read_csv('DATA_games_IRON.csv')
vi= vi.head(100)

ACTI= vi[['metadata.matchId', 'info.teams', 'info.participants']]
transcend(ACTI)

#_thread.start_new_thread(transcend,(ACTI,))
'''

cait_kiramman= '''
import pandas as pd
import _thread 

vi= pd.read_csv('DATA_games_IRON.csv')
po= vi.tail(50)
vi= vi.head(50)



ACTI= vi[['metadata.matchId', 'info.teams', 'info.participants']]

ACTII= po[['metadata.matchId', 'info.teams', 'info.participants']]


_thread.start_new_thread(transcend,(ACTI,))
_thread.start_new_thread(transcend,(ACTII,))

'''
#transcend(ACTI)
#_thread.start_new_thread(thread_delay, ('t1', 1))

#print(timeit.timeit(vi_kiramman, "from __main__ import transcend",number=1))

#print(timeit.timeit(cait_kiramman, "from __main__ import transcend",number=1))


#print(timeit.timeit('output = 10*5'))

#print(timeit.timeit(stmt=vi_kiramman))

rows= int(vi.shape[0]/2)
print(rows)
#df_1 = df.iloc[:1000,:]
#df_2 = df.iloc[1001:,:]

#po= vi.tail(50)
#vi= vi.head(50)
'''
ACTI= vi.iloc[:500,:][['metadata.matchId', 'info.teams', 'info.participants']]
ACTII= vi.iloc[501:1000,:][['metadata.matchId', 'info.teams', 'info.participants']]

ACTIII= vi.iloc[1001:1500,:][['metadata.matchId', 'info.teams', 'info.participants']]
ACTIIII= vi.iloc[1501:2000,:][['metadata.matchId', 'info.teams', 'info.participants']]
'''


ACTI= vi.iloc[:1001,:][['metadata.matchId', 'info.teams', 'info.participants']]
ACTII= vi.iloc[1001:2001,:][['metadata.matchId', 'info.teams', 'info.participants']]

ACTIII= vi.iloc[2001:3001,:][['metadata.matchId', 'info.teams', 'info.participants']]
ACTIIII= vi.iloc[3001:4001,:][['metadata.matchId', 'info.teams', 'info.participants']]
#_thread.start_new_thread(transcend,(ACTI,))
#_thread.start_new_thread(transcend,(ACTII,))

print('raaaaaaa')

#ra= transcend(ACTI)

kada = ThreadWithReturnValue(target=transcend, args=(ACTI,))
jhin = ThreadWithReturnValue(target=transcend, args=(ACTII,))
lobo = ThreadWithReturnValue(target=transcend, args=(ACTIII,))
cordero = ThreadWithReturnValue(target=transcend, args=(ACTIIII,))

kada.start()
jhin.start()
lobo.start()
cordero.start()

Violet= [kada.join()[0], jhin.join()[0], lobo.join()[0], cordero.join()[0]]
Caitlyn=[kada.join()[1], jhin.join()[1], lobo.join()[1], cordero.join()[1]]
Powder=[kada.join()[2], jhin.join()[2], lobo.join()[2], cordero.join()[2]]

Violyn=[kada.join()[2]]

VioletKiramman= pd.DataFrame()
CaitlynKiramman=pd.DataFrame()
PowderKiramman=pd.DataFrame()

for i in Violet:
    VioletKiramman= pd.concat([VioletKiramman, i], ignore_index= True)
    
for i in Caitlyn:
    CaitlynKiramman= pd.concat([CaitlynKiramman, i], ignore_index= True)
    
for i in Powder:
    PowderKiramman= pd.concat([PowderKiramman, i], ignore_index= True)


CaitlynKiramman.to_csv('PLATINUM_GAMES_macth_data.csv')
VioletKiramman.to_csv('PLATINUM_GAMES_bans_data.csv')
PowderKiramman.to_csv('PLATINUM_GAMES_game_data.csv')


#print (twrv.join())   # 


#for col in violyn.columns:
#    print(col)
'''

for i in vi_kiramman:
    for j in i[0::2]:
        for k in j:
            cup=yaml.load(k)
            cake= pd.DataFrame(cup, index=[0])
            
            cupcake= pd.concat([cupcake,cake], ignore_index=True)
            #print(k)

#cup=yaml.load("{'championId': 63, 'pickTurn': 1}")

#cake= pd.DataFrame(cup, index=[0])
'''        
#violet_kiramman=[]
'''        
for i in vi_kiramman:
    print(type(i))
    for ind, seri in i.iterrows():
        print(seri.to_frame())
        violet_kiramman.append(seri.to_frame())
        
violetxcaitlyn=[]
for i in violet_kiramman:
    for ind, seri in i.iterrows():
        print(seri.to_frame())
        violetxcaitlyn.append(seri.to_frame())
'''

     
        

