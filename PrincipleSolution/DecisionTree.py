# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:15:40 2020

@author: Thomas
"""


from sklearn import tree
import random


"""
inputs: 
    size  weightHigh  availableRoute   batteryHigh   urgencyHigh   tooManyfailedAttempts
    [0,2] [0,1]          [0,1]           [0,1]        [0,1]           [0,1]
"""

def printPredict(clf, inArray):
    if(inArray[0]==0): print("Small")
    elif(inArray[0]==1): print("Medium")
    elif(inArray[0]==2): print("Large")
    
    if(inArray[1]==0): print("Light")
    elif(inArray[1]==1): print("Heavy")
   
    if(inArray[2]==0): print("No route available")
    elif(inArray[2]==1): print("Route available")
    
    if(inArray[3]==0): print("Battery low")
    elif(inArray[3]==1): print("Battery OK")
    
    if(inArray[4]==0): print("Not urgent")
    elif(inArray[4]==1): print("Urgent")
    
    if(inArray[5]==0): print("<= 3 failed attempts")
    elif(inArray[5]==1): print("> 3 failed attempts")
    
    if (clf.predict([inArray]) == [0]):
        print("--> Do it alone")
    else:
        print("--> Call for help")

X = [  [0, 0, 1, 1, 1, 1],      #1
       [0, 0, 1, 1, 0, 1],      #1
       [2, 1, 1, 1, 0, 0],      #0
       [1, 0, 0, 0, 1, 0],      #0
       [0, 1, 1, 1, 0, 0],      #0
       [2, 1, 0, 1, 0, 0],      #1
       [1, 1, 1, 1, 1, 1],      #1
       [0, 0, 0, 0, 0, 1],      #1
       [1, 1, 0, 0, 0, 0],      #1
       [1, 1, 1, 0, 0, 0],      #1
       [2, 0, 0, 1, 1, 0],      #0
       [0, 0, 1, 1, 1, 0],      #0
       [1, 1, 1, 1, 1, 0],      #1
       [2, 1, 1, 1, 1, 0],      #1
       [0, 1, 0, 1, 1, 0],      #0
       [2, 1, 1, 1, 0, 1],      #1
       [2, 0, 0, 0, 1, 1],      #1
       [1, 1, 1, 1, 0, 0]      #0
    ]
Y = [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)


inArray = [random.randint(0, 2), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
printPredict(clf, inArray)
#print(clf.predict([[1, 1, 1, 0, 0, 0]]))


tree.plot_tree(clf) 

