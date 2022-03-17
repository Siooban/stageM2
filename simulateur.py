# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 09:23:32 2022

@author: Sioban
"""

import random
import numpy as np

class Simulateur(object):
    def __init__(self, POMDP):
        self.POMDP=POMDP
        self.currentState=None
        
        self.currentObservation=None
    
   
    def getObservation(self):
        return self.currentObservation
    
    def getCurrentState(self):
        return self.currentState
    def setCurrentState(self, newState):
        self.currentState=newState
    
    def makeTransition(self, action):
        possibleTransition=self.POMDP.transitionFunction(action, self.currentState)
        
        for state in possibleTransition:
            print(state)
            test=random.random()
            if test-possibleTransition[state]<=0:
                self.currentState=state
            else:
                test-=possibleTransition[state]
        
       
    def makeObservation(self):
        possibleObservationsData=self.POMDP.getObservation(self.currentState)
        possibleObservations=possibleObservationsData[0]
        test=random.random()
        probabilityArray=possibleObservationsData[1]
        for i in range(len(probabilityArray)):
            if test-probabilityArray[i]<=0:
                self.currentObservation=possibleObservations[i]
            else:
                test-=probabilityArray[i]
        self.currentObservation=possibleObservations[i]
    
"""def makeInitFunction():
    def initialize(POMDP):
        states=POMDP.getStates()
        shape=np.shape(states)
        t=[]
        result=np.zeros(shape)
        for i in range(shape[0]):
            for j in range(shape[1]):
                if states[i,j]==1:
                    t.append((i, j))
        value=random.randint(0, len(t)-1)
        result[t[value]]=1       
        return  t[value], result
    return initialize"""
        
        
        
      