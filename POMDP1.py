# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 08:57:58 2022

@author: Sioban
"""
import random
import numpy as np

class POMDP(object):
    def __init__(self,states, actions, rewards):
        self.states=states
        self.actions=actions
        self.rewards=rewards
        """ parameter to iniate a simulator and an agent"""
        self.initialState=None
        self.b0=None
        
    """ getter"""
    def getStates(self):
        return self.states
    def getActions(self):
        return self.actions
    def getRewards(self,transition):
        return self.rewards(transition)
    def getRewardOnState(self, state):
        return self.rewards[state]
    def getObservationF(self, currentState):
        return self.ObservationF(self.states, currentState)
    def getTransitionF(self,action, currentState):
        return self.TransitionF(self.states,action,currentState)
    
    
    def displayBelief(self, belief):
        print(belief)
        
    
    def displayF(self):
        print(self.states)
    def initialization(self): 
        shape=np.shape(self.states)
        t=[]
        result=np.zeros(shape)
        for i in range(shape[0]):
            for j in range(shape[1]):
                if self.states[i,j]==1:
                    t.append((i, j))
        value=random.randint(0, len(t)-1)
        result[t[value]]=1
        self.initialState=t[value]
        self.b0=result
        
        
    """ return  the wall number surrounding a position with uncertainty"""
    def getObservation(self, currentState):
        """normal observation"""
        proba=[]
        wallDistributions=[]
        wallDistribution=[]
        stateUp=(currentState[0]-1, currentState[1])
        if self.states[stateUp[0], stateUp[1]]==0:
            wallDistribution.append(True)
        else:
            wallDistribution.append(False)
        stateDown=(currentState[0]+1,currentState[1])
        if self.states[stateDown[0],stateDown[1]]==0:
            wallDistribution.append(True)
        else:
            wallDistribution.append(False)
        stateLeft=(currentState[0], currentState[1]-1)
        if self.states[stateLeft[0], stateLeft[1]]==0:
            wallDistribution.append(True)
        else:
            wallDistribution.append(False)
        stateRight=(currentState[0], currentState[1]+1)
        if self.states[stateRight[0], stateRight[1]]==0:
            wallDistribution.append(True)
        else:
            wallDistribution.append(False)
        result=wallDistribution.copy()
        wallDistributions.append(result)
        proba.append(0.8)  
        """ other observation"""
        for i in range(0,4):
            value=wallDistribution.copy()
            if value[i]:
                value[i]=False
            else:
                value[i]=True
            wallDistributions.append(value)
            proba.append(0.05)
        
        return wallDistributions, proba
    
    """return the possible transitions and the probabilities of those transitions
    """
    def  transitionFunction(self,action, currentState):
        dictionnaire={}
        stateUp=(currentState[0]-1, currentState[1])
        stateDown=(currentState[0]+1,currentState[1])
        stateLeft=(currentState[0], currentState[1]-1)
        stateRight=(currentState[0], currentState[1]+1)
        
        if action=="up":
            value=0
            if self.states[stateUp[0], stateUp[1]]==1:
                dictionnaire[(stateUp)]=0.8
            else:
                value+=0.8
            if self.states[stateRight[0], stateRight[1]]==1:
                dictionnaire[(stateRight)]=0.1
            else:
                value+=0.1
            if self.states[stateLeft[0], stateLeft[1]]==1:
                dictionnaire[(stateLeft)]=0.1
            else:
                value+=0.1
            if value!=0:
                dictionnaire[(currentState)]=value
        if action=="bottom":
            value=0
            if self.states[stateDown[0], stateDown[1]]==1:
                dictionnaire[(stateDown)]=0.8
            else:
                value+=0.8
            if self.states[stateRight[0], stateRight[1]]==1:
                dictionnaire[(stateRight)]=0.1
            else:
                value+=0.1
            if self.states[stateLeft[0], stateLeft[1]]==1:
                dictionnaire[(stateLeft)]=0.1
            else:
                value+=0.1
            if value!=0:
                dictionnaire[(currentState)]=value
        if action=="left":
            value=0
            if self.states[stateLeft[0], stateLeft[1]]==1:
                dictionnaire[(stateLeft)]=0.8
            else:
                value+=0.8
            if self.states[stateUp[0], stateUp[1]]==1:
                dictionnaire[(stateUp)]=0.1
            else:
                value+=0.1
            if self.states[stateDown[0], stateDown[1]]==1:
                dictionnaire[(stateDown)]=0.1
            else:
                value+=0.1
            if value!=0:
                dictionnaire[(currentState)]=value
        if action=="right":
            value=0
            if self.states[stateRight[0], stateRight[1]]==1:
                dictionnaire[(stateRight)]=0.8
            else:
                value+=0.8
            if self.states[stateUp[0], stateUp[1]]==1:
                dictionnaire[(stateUp)]=0.1
            else:
                value+=0.1
            if self.states[stateDown[0], stateDown[1]]==1:
                dictionnaire[(stateDown)]=0.1
            else:
                value+=0.1
            if value!=0:
                dictionnaire[(currentState)]=value
        return dictionnaire
    
    
   
        
        
    def setBeliefAndInitialState(self,simulateur, agent):
        simulateur.setCurrentState(self.initialState)
        agent.setBelief(self.b0)
        
            
   



