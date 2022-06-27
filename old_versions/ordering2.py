from sorting_objects import *
from item_bin import *
import random
import sys
from itertools import permutations

#item_objects = [items('i1', 86), items('i2', 24), items('i3', 91), items('i4', 52), items('i5', 67)]
#item_objects = [items('i1', 86), items('i2', 24), items('i3', 91)]
p = 0.8

ordered_items = sorted(item_objects, key = attrgetter('volume'), reverse = True)
ordered_items2 = sorted(item_objects, key = attrgetter('volume'), reverse = True)

print("ordered items: " + str(ordered_items))

#creates new ordering by assigning a probability to each item and making a weighted selection to add to the order 
new_ordering = [] 
while len(ordered_items2) > 0: 
    total_weight = 0
    rank = {} 
    weight = {} 
    probability = {} 
    probability_list = [] 
    #assigning rank and weight to each item 
    for i in range(len(ordered_items2)):
        child = ordered_items2[i] 
        rank[child] = i+1 #the paper uses positive integers for rank... should I use i instead of i+1? it does not seem to make a difference... 
        weight[child] = (1-p)**(rank[child]) #should this be rank or -rank or i or -i?? the BubbleSearch paper says -i but that means that if 0<p<1, then the items that have a lower score (ranking) are weighted more heavily 
        total_weight += weight[child] 
        print("child " + str(child)) 
        print("weight " + str(weight))
        print("total weight " + str(total_weight))
    #calculating probability for each item 
    for child in ordered_items2: 
        probability[child] = weight[child] / total_weight 
        print("probability " + str(probability)) 
        probability_list.append(weight[child] / total_weight)
    #choosing the item and adding it to the new ordering and deleting it from the original ordering 
    choice = (random.choices(ordered_items2, probability_list))[0]
    ordered_items2.remove(choice)
    new_ordering.append(choice)
    print(choice)
    print(ordered_items2)
    print(new_ordering)

#calculates the kendall tau distance between the new ordering and the original ordering 
print("kendall tau distance: " + str(kt_dist(ordered_items, new_ordering)))

with open('item_bin.py', 'a') as f:
    sys.stdout = f
    printout = "item_objects_permutation = ["
    for i in range(len(new_ordering)-1): 
        printout+=("items" +str(new_ordering[i]) + ", ") 
    printout+=("items" + str(new_ordering[len(new_ordering)-1]) + "]") 
    print(printout)
