from sorting_objects import *
from item_bin import *
from binpacking_heuristic import *
import sys
import random
import timeit

start = timeit.default_timer()

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
base_num = len(base_result.filled_bins) 

print("base result: " + str(base_result)) 
print("base cost: " + str(base_cost))

#checking that all of the items are packed into the bins 
bin_items = []
for b in base_result.filled_bins:
    for i in b.items_contained:
        bin_items.append(i)

for i in item_objects:
    if i not in bin_items:
        print("ERROR!!!! ISSUE WITH ITEMS IN BINS")
        print(i)

#defining p, number of permutations
p = 0.05
num_permutations = 2000
base_ordering = ordered_items.copy() 
num_improved = 0
replacements = []

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

    #print(base_ordering) 

    #creating a new ordering of items 
    while n > 0:
        for i in range(n): 
            choice = random.random()
            #print(choice)
            if choice <= p:
                #print("yes") 
                #print(base_ordering[i])
                new_item_order.append(base_ordering[i])
                base_ordering.remove(base_ordering[i])
                n-=1
                break
            else: 
                #print("no")
                continue 
    
    #print(new_item_order)

    #running heuristic on new ordering of items 
    new_result = packing_bins(new_item_order, ordered_bins)
    new_cost = new_result.cost
    new_filled_bins = new_result.filled_bins

    #print("new result " + str(new_result)) 
    #print("new cost " + str(new_cost)) 
    #print("new_filled_bins " + str(new_filled_bins)) 
    #print("base result " + str(base_result)) 
    #print("base cost: " + str(base_cost))
    #print("new item order " + str(new_item_order)) 

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
        num_improved += 1
        replacements.append(j) 
        #print(new_item_order)
        #print(new_filled_bins)
    
    #keeping the same base result if the new cost >= base cost 
    else: 
        base_ordering = current_base_ordering
        print(base_cost) 
        print(new_cost) 
        #print("base ordering end " + str(base_ordering))
        #print("current base ordering end " + str(current_base_ordering)) 
    print("---------------------------------")

final_num = len(base_result.filled_bins) 

print(base_num)
print(final_num)
print('number of replacements ', num_improved) 
print(replacements)

#printing off the results and storing them in binpacking_result.py to be used by visualization.py 
for b in ordered_bins:
    b.items_contained = []
    b.remaining_volume = b.volume
base_result = packing_bins(base_ordering, ordered_bins)
for b in ordered_bins: 
    if b not in base_result.filled_bins:
        base_result.filled_bins.append(b)
result = "filled_bins = ["
for b in base_result.filled_bins: 
    result += "bins('" + str(b.name) + "', " + str(b.volume) + ", " + str(b.remaining_volume) + ", " + str(b.cost) + ", " + str(b.cv_ratio) + ", ["
    for i in b.items_contained: 
        result += "items" + str(i) + ", " 
    result += "]), "
result += "]" 

stop = timeit.default_timer()

print("time: ", stop - start)

with open('binpacking_result.py', 'w') as f:
    sys.stdout = f
    print("from sorting_objects import *")
    print(result)

