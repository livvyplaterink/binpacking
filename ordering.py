from sorting_objects import *
from item_bin import *
import random
from itertools import permutations

item_objects = [items('i1', 86), items('i2', 24), items('i3', 91), items('i4', 52), items('i5', 67)]

ordered_items = sorted(item_objects, key = attrgetter('volume'), reverse = True)

print("ordered items: " + str(ordered_items))

order_list = list(permutations(ordered_items))
print("list of permutations: " + str(order_list))
prob_list = []
order_prob_list = []

for o in order_list:
    d = kt_dist(ordered_items, o)
    print("kt dist: " + str(d))
    prob = (1-0.6)**d
    print("probability: " + str(prob))
    prob_list.append(prob)
    order_prob_list.append(permutation(o, prob)) 

print("list of permutations with probability: " + str(order_prob_list))
choice = (random.choices(order_list, prob_list))[0]
print(choice)
for o in order_prob_list: 
    if o.ordering == choice: 
        print(o.probability)


