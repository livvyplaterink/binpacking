from sorting_objects import *
from item_bin2 import *
from binpacking_heuristic9 import *
import sys
import random
import timeit
import cProfile
import pstats
import io

pr = cProfile.Profile()
pr.enable()

start = timeit.default_timer() 

#defining cost/volume ratio for bins
for b in bin_objects:
    b.cv_ratio = b.cost / b.volume

#ordering bins in K according to non-decreasing order of the ratio c_j/V_j and non-decreasing order of V_j when the cost ratios c_j/V_j are equal
ordered_bins = bin_objects.copy() 
#ordered_bins.sort(key = attrgetter('cv_ratio', 'volume'))
ordered_bins.sort(key = lambda x: (x.cv_ratio, -x.volume))
original_bin_list = ordered_bins.copy()

#ordering items in I according to non-increasing order of volume
ordered_items = sorted(item_objects, key = attrgetter('volume'), reverse = True)

print(ordered_bins)
print(ordered_items)

start1 = timeit.default_timer()

#running heuristic on ordered items
base_result = packing_bins(ordered_items, ordered_bins)
base_cost = base_result.cost
base_num = len(base_result.filled_bins)


end1 = timeit.default_timer()

print(base_result.filled_bins)
print(base_cost) 
print(end1 - start1) 

if base_cost == -1:
    sys.exit()

p = 0.05
num_permutations = 3
base_ordering = ordered_items.copy()
num_improved = 0
replacements = []

for j in range(num_permutations):
    print("-------------------------")
    n = len(item_objects)
    base_ordering_1000 = base_ordering[:1000]
    new_item_order = []
    counter = 1000

    #print("ordered bins before reset " , ordered_bins) 

    ordered_bins = original_bin_list.copy() 

    #print("ordered bins after reset " , ordered_bins) 

    #resetting the items contained and remaining volume in the bins
    for b in ordered_bins:
        b.items_contained = []
        b.remaining_volume = b.volume

    #print("ordered bins after item reset " , ordered_bins)

    
    start2 = timeit.default_timer()

    while n > 0:
        for i in range(n):
            if i > 1000: 
                print("error choosing new ordering!" )
            choice = random.random()
            if choice <= p: 
                if n > 1000:
                    #print(n)
                    #print(i) 
                    #print("yes1") 
                    #print("base ordering 10000: " , base_ordering_1000)
                    #print(base_ordering_1000[i]) 
                    new_item_order.append(base_ordering_1000[i])
                    base_ordering_1000.remove(base_ordering_1000[i])
                    base_ordering_1000.append(base_ordering[counter]) 
                    #print("new item order: " , new_item_order)
                    #print("base ordering: " , base_ordering)
                    #print("adding " , base_ordering[counter] , "to base_ordering_1000")
                    counter += 1
                    n-=1 
                    #print("new item order: " , new_item_order)
                    #print("base ordering: " , base_ordering) 
                    #print("adding " , base_ordering[counter] , "to base_ordering_1000")
                    break
                else: 
                    #print(n)
                    #print(i)
                    #print("yes2")
                    #print("base ordering 10000: " , base_ordering_1000)
                    #print(base_ordering_1000[i])
                    new_item_order.append(base_ordering_1000[i])
                    base_ordering_1000.remove(base_ordering_1000[i])
                    n-=1
                    #print("new item order: " , new_item_order)
                    break 
            else: 
                #print(n)
                #print(i) 
                #print("no") 
                #print(base_ordering_1000[i]) 
                #print(new_item_order)
                continue 
    
    end2 = timeit.default_timer()
    
    print(end2 - start2) 

    start3 = timeit.default_timer()

    #print(base_ordering)
    #print(new_item_order)
    #print(ordered_bins)

    new_result = packing_bins(new_item_order, ordered_bins)
    new_cost = new_result.cost
    new_filled_bins = new_result.filled_bins

    end3 = timeit.default_timer()
    
    print(end3 - start3)

    #print(base_result.filled_bins)
    #print(new_result.filled_bins)
    #print(base_cost)
    #print(new_cost) 

    bin_error = False
    if new_cost == -1:
        bin_error = True

    if new_cost < base_cost:
        if bin_error == True:
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

    else: 
        print(base_cost) 
        print(new_cost) 
        continue 

end = timeit.default_timer() 

final_num = len(base_result.filled_bins)

print(base_num)
print(final_num)
print('number of replacements ', num_improved)
print(replacements)

print(end - start) 

pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
ps.print_stats()

with open('testb_20000_40000.txt', 'w+') as f:
            f.write(s.getvalue())


