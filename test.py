#this file creates another file called item_bin.py which contains the volumes and costs of the items and bins 
import sys 
import random 
from sorting_objects import *

with open('item_bin.py', 'w') as f:
    sys.stdout = f
    #randomly choosing the number of items from a list
    #item_number_list = [350000]
    item_number_list = [2000, 2100, 2200, 2300]
    #item_number_list = [100, 200, 300, 350]
    #item_number_list = [10, 11, 12, 13, 14]
    #item_number_list = [40, 50, 60, 70]
    item_number = random.choice(item_number_list)
    #randomly assigning volumes valued between 1 and 20 to the items
    item_objects = "item_objects = ["
    for i in range(item_number-1):
        i_volume = random.randint(100, 200)
        item_objects += ("items('i" + str(i+1) + "', " + str(i_volume) + "), ")
    i_volume = random.randint(100, 200)
    item_objects += ("items('i" + str(item_number) + "', " + str(i_volume) + ")]")
    print("from sorting_objects import *")
    print(item_objects)

    #choosing the number of bins (number of items / 2)
    bin_number = int(item_number)
    bin_objects = "bin_objects = ["
    for i in range(bin_number-1):
        b_volume = random.randint(200, 600)
        #b_cost = b_volume / 5
        b_cost = random.randint(20, 100)
        bin_objects += ("bins('b" + str(i+1) + "', " + str(b_volume) + ", " +  str(b_volume) + ", " +  str(b_cost) + ", 0, []), ")
    b_volume = random.randint(200, 600)
    #b_cost = b_volume / 5
    b_cost = random.randint(20, 100) 
    bin_objects += ("bins('b" + str(bin_number) + "', " + str(b_volume) + ", " +  str(b_volume) + ", " +  str(b_cost) + ", 0, [])]")
    print(bin_objects)
