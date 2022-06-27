#this file creates another file called item_bin.py which contains the volumes and costs of the items and bins 
import sys 
import random 
from sorting_objects import *

with open('item_bin.py', 'w') as f:
    sys.stdout = f
    #randomly choosing the number of items from a list
    #item_number_list = [1000, 1200, 1300, 1400]
    item_number_list = [600, 700, 800, 900, 1000]
    #item_number_list = [10, 11, 12, 13, 14]
    item_number = random.choice(item_number_list)
    #randomly assigning volumes valued between 1 and 20 to the items
    item_objects = "item_objects = ["
    for i in range(item_number-1):
        i_volume = random.randint(1, 100)
        item_objects += ("items('i" + str(i+1) + "', " + str(i_volume) + "), ")
    i_volume = random.randint(1, 100)
    item_objects += ("items('i" + str(item_number) + "', " + str(i_volume) + ")]")
    print("from sorting_objects import *")
    print(item_objects)

    #choosing the number of bins (number of items / 2)
    bin_number = int(item_number / 2)
    bin_objects = "bin_objects = ["
    for i in range(bin_number-1):
        b_volume = random.randint(200, 700)
        b_cost = random.randint(50, 100)
        bin_objects += ("bins('b" + str(i+1) + "', " + str(b_volume) + ", " +  str(b_volume) + ", " +  str(b_cost) + ", 0, []), ")
    b_volume = random.randint(200, 1000)
    b_cost = random.randint(1, 200) 
    bin_objects += ("bins('b" + str(bin_number) + "', " + str(b_volume) + ", " +  str(b_volume) + ", " +  str(b_cost) + ", 0, [])]")
    print(bin_objects)
