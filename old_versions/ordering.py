#this file makes a dictionary that contains lists of decision vectors that are created with various p-values according to the algorithm in the BubbleSearch paper 

from sorting_objects import *
from item_bin import *
import random
import sys

p_list = [0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9]
dvector_dict = {}

#looping through p-values in increments of 0.1 from 0.1 - 0.9 
for q in p_list: 
    p = q/10
    print(p)
    yes_no = [1, 0] 
    prob = [p, 1-p]
    dvector_dict[p] = [] 
    
    #choosing the number of permutations
    num_permutations = 100
    for j in range(num_permutations):
        print(j)
        dvector = []
        n = len(item_objects)
        
        #creating decision vectors by randomly choosing an index of the ordered item list according to probability p 
        while n>0: 
            for i in range(n): 
                #print("i " + str(i))
                choice = (random.choices(yes_no, prob))[0]
                if choice == 1: 
                    print(i)
                    dvector.append(i)
                    n-=1
                    break 
                else: 
                    continue

        #adding decision vector to probability list only if it is not already in the list 
        if dvector in dvector_dict[p]:
            print(str(dvector) + " already in list")
        if dvector not in dvector_dict[p]: 
            print(str(dvector) + " being added to list")
            dvector_dict[p].append(dvector)

#writing decision vector dictionary to item_bin.py
with open('item_bin.py', 'a') as f:
    sys.stdout = f
    print("dvector_dict = " + str(dvector_dict))
                        
