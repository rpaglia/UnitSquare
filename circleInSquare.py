# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 18:26:51 2021

@author: Richard Paglia

"""
import numpy as np
import matplotlib.pyplot as plt
import random as rnd
unifRnd = rnd.uniform

def dist2Center(x,y):
    if abs(x)<=0.5 and abs(y) <= 0.5 :
        dist = np.sqrt(x**2 + y**2)
        return dist
    else:
        return None
   
def dist2Edge(x,y):
    if abs(x)<=0.5 and abs(y) <= 0.5 :
        dist = min(abs(0.5-x), abs(-0.5-x), abs(0.5-y),abs(-0.5-y))
    else:
        print('point {},{}, not in square'.format(x,y))
        return None
    return dist

while True:
    try:
        points = int(input("Enter how many points you would like to use (ex:1000): "))
        if points <= 0:
            print("\033[0;31;mNot a valid entry! Please try again ...\033[0;0;m")
        else:
            break
    except ValueError:
        print("\033[0;31;mNo valid integer! Please try again ...\033[0;0;m")
#n = 1000

squareArray = np.zeros(shape=(points,2))
for i in range(points):
    squareArray[i,0],squareArray[i,1]= unifRnd(-0.5,0.5),unifRnd(-0.5,0.5)

plt.figure(1)    
plt.plot(squareArray[:,0],squareArray[:,1],'k.')
plt.show()

minRad = 0
maxRad = 0.5

eps = 0.0001

while(1):
    testRad = (minRad+maxRad)/2
    
    distIn = []
    distOut = []

    for j in range(points):
        d2C = dist2Center(squareArray[j,0],squareArray[j,1])

        if d2C <= testRad:
            distIn.append(d2C)    
        else:
            d2E = dist2Edge(squareArray[j,0],squareArray[j,1])
            distOut.append(d2E)
            
            
    avgDistIn = np.mean(distIn)
    avgDistOut = np.mean(distOut)
    
    diffDist = abs(avgDistIn-avgDistOut)
    if diffDist <= eps: break

    if(avgDistIn>avgDistOut):
        maxRad = testRad
    else:
        minRad = testRad
        
        
print('Radius of circle: {}'.format(testRad))

plt.figure(2)  
plt.plot(squareArray[:,0],squareArray[:,1],'k.')
xVals = np.linspace(-testRad, testRad)
yVals = np.sqrt(testRad**2-xVals**2)
plt.plot(xVals,yVals,'r-')
plt.plot(xVals,-yVals,'r-')



    



    


