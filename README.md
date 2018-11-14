# MITxCompThinkDataSci
This repository contains scripts related to the course _Introduction to Computational Thinking and Data Science_ by MITx on edX. In all projects, MITx provides the skeleton code (function wrappers) and some helper functions (functionality outside the scope of the course).

I completed this course in September 2018. [View my certificate!](https://courses.edx.org/certificates/574783ec7fa84ccd91859d6f63905e0b)

## Brute Force Space Cows
This program implements a brute force algorithm to find the minimum number of trips needed to take all cows across the universe in the function brute_force_cow_transport. The function returns a list of lists, where each inner list represents a trip and contains the names of cows taken on that trip.

* The _ps1.py_ script contains the brute force algorithm.  
* The _ps1_cow_data.txt_ file contains cow names and weights in tons.  
* The _ps1_partition.py_ script is a helper function provided by MITx that fetches all of the available 
partitions to use for the brute force algorithm.  

## Power Set Generators
The files in this folder are power set generators. The _power set_ aspect means the code generates all possible combinations of a list of items. The _generator_ aspect means the codes generates the lists as you go along - it does not generate and store all of the combinations. This is helpful because all combinations of a large list is extremely large - 2^n where n is the number of items in the original list.

* The _brute_force_generator.py_ script contains a generator that returns every arrangement of items from a list such that each is in one or none of two different bags. Each combination is given as a tuple of two lists, the first being the items in bag1, and the second being the items in bag2. 
* The _wk1_powerSet.py_ script contains two power set generators that each generate all combinations of N items.  

## Random Walk Simuation

This program simulates the time it takes a group of vacuum cleaner robots to clean the floor of a room. Two different strategies are developed and compared: 1) a standard robot with a standard movement strategy and 2) a random walk robot with a stochastic movement strategy.

* The _ps2.py_ script contains the class assignments and simulation code for the program.  
* The _ps2_visualize.py_ file contains a helper function provided by MITx for visualizing the robots vacuuming.  
* The _ps2_verify_movement35.pyc_ and _ps2_verify_movement36.pyc_ files provided by MITx contain supporting code for the visualization.  

## Virus Reproduction

This program uses pylab to implement a stochastic simulation of patient and virus population dynamics. Two scenarios are developed: 1) patient and simple virus and 2) treated patient and resistant virus. Finally, conclusions are drawn about treatment regimens based on the simulation results.

* The _ps3b.py_ script contains the class assignments and simulation code for the program.  
* The _ps3b_precompiled_35.pyc_ and _ps3b_precompiled_36.pyc_ files provided by MITx contain supporting code for the simulation.  

## Climate Change

This program models the climate of different areas with regression and tries to find evidence of global warming. Models are created to analyze and visualize climate change in terms of temperature. 

* The _ps4.py_ file contains the source code.
* The _data.csv_ file contains the data used in the regression analysis.

## Strings and Graphs
This folder contains miscellaneous exercises.

* The _wk1_student_swaps_graphs.py_ file contains a WeightedEdge class extends Edge (povided by MITx). The WeightedEdge constructor requires a weight parameter, as well as the parameters from Edge. It also includes a getWeight method.  
* The _wk3_problems_strings.py_ file contains string manipulation exercises.
