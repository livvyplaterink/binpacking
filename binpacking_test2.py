from sorting_objects import *
from item_bin import *
from binpacking_heuristic import *
import sys
import random

#defining cost/volume ratio for bins
for b in bin_objects:
    b.cv_ratio = b.cost / b.volume

#ordering bins in K according to non-decreasing order of the ratio c_j/V_j and non-decreasing order of V_j when the cost ratios c_j/V_j are equal
ordered_bins = multisort(bin_objects, (('cv_ratio', False), ('volume', False)))

#ordering items in I according to non-increasing order of volume
ordered_items = sorted(item_objects, key = attrgetter('volume'), reverse = True)

print(ordered_bins)
print(ordered_items)

#running heuristic on ordered items 
base_result = packing_bins(ordered_items, ordered_bins)
base_cost = base_result.cost
base_filled_bins = base_result.filled_bins


print("base cost: " + str(base_cost))
print("base filled_bins: " + str(base_filled_bins))

#defining p, number of permutations
p = 0.05
num_permutations = 100
yes_no = [1, 0] 
prob = [p, 1-p]
base_ordering = ordered_items.copy() 

#iterating over the number of permutations 
for j in range(num_permutations):
    #make a copy of the base ordering list because as a new ordering is created, items from the base ordering are removed 
    current_base_ordering = base_ordering.copy()
    n = len(item_objects)
    new_item_order = []

    #resetting the items contained and remaining volume in the bins 
    for b in ordered_bins:
        b.items_contained = []
        b.remaining_volume = b.volume
    
    #creating a new ordering of items 
    while n > 0:
        for i in range(n): 
            choice = (random.choices(yes_no, prob))[0]
            if choice == 1: 
                new_item_order.append(base_ordering[i])
                base_ordering.remove(base_ordering[i])
                n-=1
                break
            else: 
                continue 
    
    #running heuristic on new ordering of items 
    new_result = packing_bins(new_item_order, ordered_bins)
    new_cost = new_result.cost
    new_filled_bins = new_result.filled_bins

    #checking that all items are packed 
    bin_items = [] 
    bin_error = False 
    for b in new_filled_bins: 
        for i in b.items_contained: 
            bin_items.append(i)
    for i in item_objects: 
        if i not in bin_items: 
            bin_error = True  
            print("ERROR!!!! ISSUE WITH ITEMS IN BINS")
            break
    print(bin_error) 

    #redefining base result if the new cost < base cost 
    if new_cost < base_cost: 
        if bin_error == True: 
            base_ordering = current_base_ordering
            print(base_cost)
            print(new_cost)
            print("getting rid of incorrect ordering") 
            continue 
        print(base_cost)
        print(new_cost) 
        print("NEW COST < BASE COST") 
        base_ordering = new_item_order.copy()
        base_result = new_result 
        base_cost = new_result.cost 
        base_filled_bins = new_filled_bins.copy()
        print(new_item_order)
        print(new_filled_bins)
        print(base_filled_bins)
        #print("base ordering end " + str(base_ordering))
        #print("current base ordering end " + str(current_base_ordering))
    
    #keeping the same base result if the new cost >= base cost 
    else: 
        base_ordering = current_base_ordering
        print(base_cost) 
        print(new_cost) 
        #print("base ordering end " + str(base_ordering))
        #print("current base ordering end " + str(current_base_ordering)) 
    print("---------------------------------")


for b in ordered_bins:
    b.items_contained = []
    b.remaining_volume = b.volume
base_result = packing_bins(base_ordering, ordered_bins)
for b in ordered_bins: 
    if b not in base_result.filled_bins:
        base_result.filled_bins.append(b)
print(base_result)
print(base_filled_bins)
print(base_result.filled_bins)
result = "filled_bins = ["
for b in base_result.filled_bins: 
    result += "bins('" + str(b.name) + "', " + str(b.volume) + ", " + str(b.remaining_volume) + ", " + str(b.cost) + ", " + str(b.cv_ratio) + ", ["
    for i in b.items_contained: 
        result += "items" + str(i) + ", " 
    result += "]), "
result += "]" 
print(result)
