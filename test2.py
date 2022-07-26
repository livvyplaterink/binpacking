#this file creates another file called item_bin.py which contains the volumes and costs of the items and bins 
import sys 
import random 
from sorting_objects import *

original_stdout = sys.stdout
f = open('item_bin2.py', 'w')
sys.stdout = f

quantity = [18000, 26000, 32000, 42000, 49000, 51000, 45000, 34000, 17000, 4500, 1000]
volume = [(1, 2), (2, 4), (4, 8), (8, 16), (16, 32), (32, 64), (64, 128), (128, 256), (256, 512), (512, 1024), (1024, 2048)]
item_objects = "item_objects = ["
counter = 0
for q in range(len(quantity)): 
    item_number = quantity[q]
    for i in range(item_number): 
        i_volume = random.uniform(volume[q][0], volume[q][1])
        #print(i_volume)
        counter += 1 
        item_objects += ("items('i" + str(counter) + "', " + str(i_volume) + "), ")
item_objects += ("]")
print("from sorting_objects import *")
print(item_objects)

bin_number = int(counter / 2)
bin_objects = "bin_objects = [" 
for b in range(bin_number): 
    b_volume = random.uniform(20000, 40000) 
    b_cost = random.randint(100, 600) 
    #b_cost = b_volume / 5
    bin_objects += ("bins('b" + str(b+1) + "', " + str(b_volume) + ", " +  str(b_volume) + ", " +  str(b_cost) + ", 0, []), ")
bin_objects += "]" 
print(bin_objects) 

#with open('item_bin.py', 'w') as f:
#    sys.stdout = f
    #randomly choosing the number of items from a list
#    item_number_list = [50000]
    #item_number_list = [2000, 2100, 2200, 2300]
    #item_number_list = [100, 200, 300, 350]
    #item_number_list = [10, 11, 12, 13, 14]
    #item_number_list = [40, 50, 60, 70]
#    item_number = random.choice(item_number_list)
    #randomly assigning volumes valued between 1 and 20 to the items
#    item_objects = "item_objects = ["
#    for i in range(item_number-1):
#        i_volume = random.randint(100, 500)
#        item_objects += ("items('i" + str(i+1) + "', " + str(i_volume) + "), ")
#    i_volume = random.randint(100, 500)
#    item_objects += ("items('i" + str(item_number) + "', " + str(i_volume) + ")]")
#    print("from sorting_objects import *")
#    print(item_objects)

    #choosing the number of bins (number of items / 2)
#    bin_number = int(item_number / 2)
#    bin_objects = "bin_objects = ["
#    for i in range(bin_number-1):
#        b_volume = random.randint(2000, 4000)
#        b_cost = random.randint(50, 600)
#        bin_objects += ("bins('b" + str(i+1) + "', " + str(b_volume) + ", " +  str(b_volume) + ", " +  str(b_cost) + ", 0, []), ")
#    b_volume = random.randint(2000, 4000)
#    b_cost = random.randint(50, 600) 
#    bin_objects += ("bins('b" + str(bin_number) + "', " + str(b_volume) + ", " +  str(b_volume) + ", " +  str(b_cost) + ", 0, [])]")
#    print(bin_objects)
