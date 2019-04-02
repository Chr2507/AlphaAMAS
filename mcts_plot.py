#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Apr  2 13:42:15 2019

@author: chris
"""
import numpy as np
from matplotlib import pyplot as pl

fileHandler= open("run_archive/tictactoe/run0001/logs/logger_tourney.log", 'r')


listOfLines=fileHandler.readlines()
fileHandler.close()

result=[]   

for i in range(len(listOfLines)):
    if listOfLines[i].find("DRAW") != -1:
        result.append(0)
    if listOfLines[i].find("WIN") != -1:
        result.append(1)
    if listOfLines[i].find("LOSE") != -1:
        result.append(-1)
    
fracDraw=[]
fracWin=[]
fracLose=[]    
countDraw=0
countWin=0
countLose=0
for i in range(len(result)):
    if result[i]==0:
        countDraw+=1
    elif result[i]==1:
        countWin+=1
    else:
        countLose+=1
    fracDraw.append(countDraw/(countDraw+countWin+countLose))
    fracWin.append(countWin/(countDraw+countWin+countLose))
    fracLose.append(countLose/(countDraw+countWin+countLose))

fig, ax=pl.subplots(1,1)

x=np.linspace(1,len(result),len(result))
ax.plot(x,fracDraw,label='Draw fraction')
ax.plot(x,fracWin,label='Win fraction')
ax.plot(x,fracLose,label='Lose fraction')
ax.set(xlabel='Evaluation Episodes',ylabel='Result Fraction')
ax.legend(prop={'size': 12})


fig.savefig('Draw2.png')