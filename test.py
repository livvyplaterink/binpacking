import sys 
import random 
from sorting_objects import *

with open('item_bin.py', 'w') as f:
    sys.stdout = f
    #randomly choosing the number of items from a list
    item_number_list = [850, 700, 800, 900]
    item_number = random.choice(item_number_list)
    #randomly assigning volumes valued between 1 and 20 to the items
    item_objects = "item_objects = ["
    for i in range(item_number):
        i_volume = random.randint(1, 100)
        item_objects += ("items('i" + str(i+1) + "', " + str(i_volume) + "), ")
    item_objects += ("]")
    print("from sorting_objects import *")
    print(item_objects)

    #choosing the number of bins (number of items / 2)
    bin_number = int(item_number / 2)
    bin_objects = "bin_objects = ["
    for i in range(bin_number):
        b_volume = random.randint(200, 1000)
        b_cost = random.randint(1, 200)
        bin_objects += ("bins('b" + str(i+1) + "', " + str(b_volume) + ", " +  str(b_volume) + ", " +  str(b_cost) + ", 0, []), ")
    bin_objects += ("]")
    print(bin_objects)
