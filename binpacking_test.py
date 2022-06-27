#this script applies the heuristic first to the items according to non-increasing order of volume, and then according to permutations of that ordering according to the BubbleSearch algorithm  

from sorting_objects import *
from item_bin import *
from binpacking_heuristic import *
import sys

#defining cost/volume ratio for bins 
for b in bin_objects:
        b.cv_ratio = b.cost / b.volume

#ordering bins in K according to non-decreasing order of the ratio c_j/V_j and non-decreasing order of V_j when the cost ratios c_j/V_j are equal
ordered_bins = multisort(bin_objects, (('cv_ratio', False), ('volume', False)))

#ordering items in I according to non-increasing order of volume
ordered_items = sorted(item_objects, key = attrgetter('volume'), reverse = True)

base_result = packing_bins(ordered_items, ordered_bins)
base_cost = base_result.cost
base_filled_bins = base_result.filled_bins

print("base cost: " + str(base_cost))
print("base filled_bins: " + str(base_filled_bins))

#looping through the various p-values for the decision vectors
for p in dvector_dict: 
    dvector_list = dvector_dict[p]
    
    #looping thorugh the various decision vectors for each p value 
    for o in dvector_list: 
        ordered_items = sorted(item_objects, key = attrgetter('volume'), reverse = True)
        new_cost = 0
        new_item_order = []
        
        #resetting the items contained and remaining volume in the bins 
        for b in ordered_bins: 
            b.items_contained = [] 
            b.remaining_volume = b.volume 

        #adding items to the new ordering and removing them from the original ordering according to the decision vector 
        while len(ordered_items) > 0: 
            for i in o: 
                new_item_order.append(ordered_items[i]) 
                ordered_items.remove(ordered_items[i]) 

        #print(o) 
        #print(sorted(item_objects, key = attrgetter('volume'), reverse = True))
        #print(new_item_order)
        new_result = packing_bins(new_item_order, ordered_bins)
        new_cost = new_result.cost
        new_filled_bins = new_result.filled_bins
        #print(new_cost)

        #showing results if the new cost is better than the original cost 
        if new_cost < base_cost:
            print(p)
            print(new_cost)
            better_filled_bins = new_filled_bins
            print("NEW COST < BASE COST")
            print(o)
            print(new_filled_bins)
        if new_cost == 386: 
            print(o)
#print(ordered_bins)
