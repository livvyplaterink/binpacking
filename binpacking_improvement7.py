from sorting_objects import *
from binpacking_heuristic9 import *
from item_bin2 import *
import sys
import random
import timeit
import cProfile
import pstats
import io

pr = cProfile.Profile()
pr.enable()

#defining cost/volume ratio for bins
for b in bin_objects:
    b.cv_ratio = b.cost / b.volume

#ordering bins in K according to non-decreasing order of the ratio c_j/V_j and non-decreasing order of V_j when the cost ratios c_j/V_j are equal
ordered_bins = bin_objects 
ordered_bins.sort(key = lambda x: (x.cv_ratio, -x.volume))  
#ordered_bins.sort(key = attrgetter('cv_ratio', 'volume'))
#ordered_bins = multisort(bin_objects, (('cv_ratio', False), ('volume', False)))

#ordering items in I according to non-increasing order of volume
ordered_items = item_objects
ordered_items.sort(key = attrgetter('volume'), reverse = True)

print(ordered_bins)
print(ordered_items)

start = timeit.default_timer()

base_result = packing_bins(ordered_items, ordered_bins)
base_cost = base_result.cost
base_num = len(base_result.filled_bins)

end = timeit.default_timer()

print(base_cost)
print(base_num)
#print(base_result)
print(end-start)
#sys.stdout = original_stdout

pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
ps.print_stats()

with open('test9_3000_10000_2.txt', 'w+') as f:
    f.write(s.getvalue())

with open('out92.txt', 'w') as f:
    sys.stdout = f
    print(base_result)

