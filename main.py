# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 09:09:55 2022

@author: Sioban
"""
import POMDP
import numpy as np
import simulateur
import agent




class main(object):
    def __init__(self, POMDP, agent, simulateur):
        self.POMDP=POMDP
        self.simulateur=simulateur
        self.agent=agent
        
        
    def run(self):
        print( self.POMDP.getActions())
        self.POMDP.initialization()
        self.POMDP.setBeliefAndInitialState(self.simulateur, self.agent)
        print(self.agent.getBelief())
        while True:
            self.agent.choseAction()
            print(self.agent.getAction())
            self.simulateur.makeTransition(self.agent.action)
            self.simulateur.makeObservation()
            newObservation=self.simulateur.getObservation()
            self.agent.updateBelief(newObservation, self.agent.getAction())
            print(self.agent.getBelief())
            if self.POMDP.getRewardOnState(self.simulateur.getCurrentState())==10:
                print("Victory")
                return
            if self.POMDP.getRewardOnState(self.simulateur.getCurrentState())==-100:
                print("Defeat")
                return
    

#creation du plateau 
grille=np.zeros([5, 9])

#0 pour un mur 1 pour un passage

grille[1,1]=1
grille[2,1]=1
grille[3,1]=1

grille[1,2]=1

grille[1,3]=1
grille[2,3]=1
grille[3,3]=1

grille[1,4]=1

grille[1,5]=1
grille[2,5]=1
grille[3,5]=1

grille[1,6]=1

grille[1,7]=1
grille[2,7]=1
grille[3,7]=1

rewardExample=np.zeros([5, 9])
rewardExample[3,3]=10
rewardExample[3,5]=-100

actionsExample=["up","bottom", "left", "right"]
test={}
print(test.get((1,1)))
mazeExample=POMDP.POMDP(grille, actionsExample, rewardExample)
simu1=simulateur.Simulateur(mazeExample)
agent1=agent.Agent(mazeExample,agent.makeUpdateFunction())


main1=main(mazeExample, agent1, simu1)
main1.run()
        
            
        
#print(mazeExample.getStates())
#print(mazeExample.getActions())
#print(mazeExample.getObservationF((3,7)))

