# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 11:03:46 2022

@author: Sioban
"""
import numpy as np

class Agent(object):
    def __init__(self, POMDP,updateF):
        self.POMDP=POMDP
        self.newObservation=None
        self.belief=None
        self.updateF=updateF
        self.action=None
        
    def updateBelief(self,newObservation, action):
       
        newBelief=np.copy(self.updateF(self.POMDP, self.belief,newObservation, action))
        self.belief=newBelief
       
    def getBelief(self):
        return self.belief
    
    def setBelief(self,newBelief):
        self.belief=newBelief
        
    def getAction(self):
        return self.action
        
    def choseAction(self):
        while True:
            x=input("action choice:up, bottom, right, left")
            if x=="up":
                self.action="up"
                return
            if x=="bottom":
                self.action="bottom"
                return
            if x=="right":
                self.action="right"
                return
            if x=="left":
                self.action="left"
                return
    
                
        
    def displayBelief(self):
        print(self.belief)


    def updateFunction(POMDP, oldBelief, newObservation, action):
        #shape=np.shape(POMDP.getStates())
        """ new observation is an observation followed by the probability for this 
        observation to occur"""
        #result=np.zeros(shape)
        newBelief={}
        """alpha is the normalisation factor"""
        alpha=0
        
        """ for all states"""
        for state in oldBelief: #oldBelief is a dictionnary each state is associated with its belief value
        #for i in range(shape[0]):
            #for j in range(shape[1]):
                #if oldBelief[i,j]!=0:
            if oldBelief[state]:
                newPossiblePosition=POMDP.getTransitionF(action, state)
                    #newPossiblePosition=POMDP.transitionFunction(action,(i,j))
                for key in newPossiblePosition:
                    testObservations=POMDP.getObservation(key)
                    possibleObservation=testObservations[0]
                    observationProba=testObservations[1]
                    for k in range(len(possibleObservation)):
                        if compare(possibleObservation[k],newObservation):
                            value=newPossiblePosition[key]*oldBelief[state]*observationProba[k]
                            newBelief[key]+=value
                            alpha+=value
        """ normalization"""
        """for i in range(shape[0]):
            for j in range(shape[1]):
                result[i,j]/=alpha"""
        for state in newBelief:
            newBelief[state]/=alpha
                
        return newBelief
    
        
def compare(obs1, obs2):
    for i in range(len(obs1)):
        if obs1[i]!=obs2[i]:
            return False
    return True
        