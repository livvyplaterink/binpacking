from sorting_objects import *
from item_bin import *
from binpacking_heuristic7 import *
import sys
import random
import timeit
import cProfile
import pstats
import io

#start = timeit.default_timer()

pr = cProfile.Profile()
pr.enable()

#defining cost/volume ratio for bins
for b in bin_objects:
    b.cv_ratio = b.cost / b.volume

#ordering bins in K according to non-decreasing order of the ratio c_j/V_j and non-decreasing order of V_j when the cost ratios c_j/V_j are equal
original_bin_list = bin_objects.copy()
#original_bin_list.sort(key = attrgetter('cv_ratio', 'volume'))
original_bin_list.sort(key = lambda x: (x.cv_ratio, x.volume))
ordered_bins = original_bin_list.copy()

#ordering items in I according to non-increasing order of volume
ordered_items = sorted(item_objects, key = attrgetter('volume'), reverse = True)

print(ordered_items)
print(ordered_bins)

start1 = timeit.default_timer()

#running heuristic on ordered items 
base_result = packing_bins(ordered_items, ordered_bins)
base_cost = base_result.cost
base_num = len(base_result.filled_bins) 

end1 = timeit.default_timer()

print("base result: " + str(base_result.filled_bins)) 
print("base cost: " + str(base_cost))
print(len(base_result.filled_bins))
print(end1-start1)

#sys.exit()

if base_cost == -1: 
    sys.exit() 

#defining p, number of permutations
p = 0.05
num_permutations = 600
base_ordering = ordered_items.copy() 
num_improved = 0
replacements = []

#iterating over the number of permutations 
for j in range(num_permutations):
    #make a copy of the base ordering list because as a new ordering is created, items from the base ordering are removed 
    current_base_ordering = base_ordering.copy()
    n = len(item_objects)
    new_item_order = []

    ordered_bins = original_bin_list.copy()

    #resetting the items contained and remaining volume in the bins 
    for b in ordered_bins:
        b.items_contained = []
        b.remaining_volume = b.volume
    #print(ordered_bins)

    #print(base_ordering) 
    
    start4 = timeit.default_timer()

    #creating a new ordering of items 
    while n > 0:
        for i in range(n): 
            choice = random.random()
            #print(choice)
            if choice <= p:
                #print("yes") 
                #print(base_ordering[i])
                new_item_order.append(base_ordering[i])
                #base_ordering[:] = [x for x in base_ordering if not base_ordering[i]]
                #base_ordering = base_ordering[0:i] + base_ordering[i+1:]
                base_ordering.remove(base_ordering[i])
                #del base_ordering[i]
                #base_ordering2 = base_ordering[:i] + base_ordering[i+1:]
                #base_ordering = base_ordering2
                #print(len(base_ordering))
                n-=1
                #print(n)
                break
            else: 
                #print("no")
                continue 
    
    end4 = timeit.default_timer()

    print(end4-start4)

    #print(new_item_order)

    start2 = timeit.default_timer()

    #running heuristic on new ordering of items 
    new_result = packing_bins(new_item_order, ordered_bins)
    new_cost = new_result.cost
    new_filled_bins = new_result.filled_bins

    end2 = timeit.default_timer()


    #checking that all items are packed 
    bin_items = []
    bin_error = False
    if new_cost == -1: 
        bin_error = True 
    #for b in new_filled_bins: 
    #    bin_items += b.items_contained
    #for i in item_objects: 
    #    if i not in bin_items: 
    #        bin_error = True  
    #        print("ERROR!!!! ISSUE WITH ITEMS IN BINS")
    #        break
    #print(bin_error)

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
    print(end2-start2)
    print("---------------------------------")

final_num = len(base_result.filled_bins) 

print(base_num)
print(final_num)
print('number of replacements ', num_improved) 
print(replacements)

pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
ps.print_stats()

with open('testb_20000_40000.txt', 'w+') as f:
        f.write(s.getvalue())

#printing off the results and storing them in binpacking_result.py to be used by visualization.py 
#for b in ordered_bins:
#    b.items_contained = []
#    b.remaining_volume = b.volume
#base_result = packing_bins(base_ordering, ordered_bins)
#for b in ordered_bins: 
#    if b not in base_result.filled_bins:
#        base_result.filled_bins.append(b)
#result = "filled_bins = ["
#for b in base_result.filled_bins: 
#    result += "bins('" + str(b.name) + "', " + str(b.volume) + ", " + str(b.remaining_volume) + ", " + str(b.cost) + ", " + str(b.cv_ratio) + ", ["
#    for i in b.items_contained: 
#        result += "items" + str(i) + ", " 
#    result += "]), "
#result += "]" 

#stop = timeit.default_timer()

#print("time: ", stop - start)

#with open('binpacking_result.py', 'w') as f:
#    sys.stdout = f
#    print("from sorting_objects import *")
#    print(result)

