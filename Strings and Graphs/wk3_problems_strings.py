#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 18:08:43 2018

@author: lisaover
"""

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    #import numpy as np
    
    if (L == []):
        return float('nan')
    lengths = []
    for s in L:
        lengths.append(len(s))
        
    mu = sum(lengths)/len(lengths)
    
    sum_of_sq = 0
    for n in lengths:
        sum_of_sq += (n-mu)**2
        
    var = sum_of_sq/len(lengths)
        
    #return np.round(np.sqrt(var), 4)
    return var**0.5

'''
L = ['The','quick','brown','fox','jumped','over','the','lazy','dog']
L = ['a', 'z', 'p'] # returns 0
L = ['apples', 'oranges', 'kiwis', 'pineapples'] # returns 1.8708
L = []
stdev = stdDevOfLengths(L)
print(stdev)

import numpy as np
print(np.average([10, 4, 12, 15, 20, 5]))
print(np.std([10, 4, 12, 15, 20, 5]))
'''

def chooseThree():
    import random
    
    bucket = ['red','green','red','green','red','green']
    chosen = []
    desired = [['red','red','red'], ['green','green','green']]
        
    for j in range(3):
        # choose a ball
        b = random.choice(bucket)
        # add ball to chosen
        chosen.append(b)
        # remove choden balls from bucket
        bucket.remove(b)
          
    if chosen in desired:
        return 1
    else:
        return 0

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    
    if numTrials <= 0:
        return 0
        
    monoColor = 0
    for i in range(numTrials):
        monoColor += chooseThree()
    
    return monoColor/numTrials

numTrials = 5000
prob = noReplacementSimulation(numTrials)
print(prob)

'''
Below is answer code from MIT
'''
def oneTrial():
    '''
    Simulates one trial of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns True if all three balls are the same color,
    False otherwise.
    '''
    balls = ['r', 'r', 'r', 'g', 'g', 'g']
    chosenBalls = []
    for t in range(3):
        # For three trials, pick a ball
        ball = random.choice(balls)
        # Remove the chosen ball from the set of balls
        balls.remove(ball)
        # and add it to a list of balls we picked
        chosenBalls.append(ball)
    # If the first ball is the same as the second AND the second is the same as the third,
    #  we know all three must be the same color.
    if chosenBalls[0] == chosenBalls[1] and chosenBalls[1] == chosenBalls[2]:
        return True
    return False

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    numTrue = 0
    for trial in range(numTrials):
        if oneTrial():
            numTrue += 1

    return float(numTrue)/float(numTrials)

numTrials = 5000
prob = noReplacementSimulation(numTrials)
print(prob)


'''
MIT code with my modifications
'''
def oneTrial():
    '''
    Simulates one trial of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns True if all three balls are the same color,
    False otherwise.
    '''
    bucket = ['red', 'red', 'red', 'green', 'green', 'green']
    monoColor = [['red', 'red', 'red'],['green', 'green', 'green']]
    chosenBalls = []
    for t in range(3):
        # For three trials, pick a ball
        ball = random.choice(bucket)
        # Remove the chosen ball from the set of balls
        bucket.remove(ball)
        # and add it to a list of balls we picked
        chosenBalls.append(ball)
    # If the first ball is the same as the second AND the second is the same as the third,
    #  we know all three must be the same color.
    if chosenBalls in monoColor:
        return 1
    return 0

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    numTrue = 0
    for trial in range(numTrials):
            numTrue += oneTrial()

    return float(numTrue)/float(numTrials)

numTrials = 5000
prob = noReplacementSimulation(numTrials)
print(prob)
