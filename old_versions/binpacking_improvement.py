from sorting_objects import *
from binpacking_heuristic import *
from item_bin import *
import sys
import random
import timeit
import cProfile
import pstats
import io

#item_objects = [items('i1', 189), items('i2', 123), items('i3', 146), items('i4', 171), items('i5', 164), items('i6', 162), items('i7', 168), items('i8', 167), items('i9', 188), items('i10', 191), items('i11', 148), items('i12', 111)]


#bin_objects = [bins('b1', 351, 351, 160, 0, []), bins('b2', 255, 255, 78, 0, []), bins('b3', 381, 381, 126, 0, []), bins('b4', 540, 540, 66, 0, []), bins('b5', 458, 458, 113, 0, []), bins('b6', 519, 519, 195, 0, []), bins('b7', 533, 533, 105, 0, []), bins('b8', 552, 552, 147, 0, []), bins('b9', 428, 428, 107, 0, []), bins('b10', 430, 430, 63, 0, []), bins('b11', 444, 444, 87, 0, []), bins('b12', 366, 366, 104, 0, []), bins('b13', 252, 252, 64, 0, []), bins('b14', 205, 205, 85, 0, []), bins('b15', 229, 229, 68, 0, []), bins('b16', 294, 294, 86, 0, []), bins('b17', 295, 295, 52, 0, [])]

#pr = cProfile.Profile()
#pr.enable()

#defining cost/volume ratio for bins
for b in bin_objects:
    b.cv_ratio = b.cost / b.volume

#ordering bins in K according to non-decreasing order of the ratio c_j/V_j and non-decreasing order of V_j when the cost ratios c_j/V_j are equal
#ordered_bins = multisort(bin_objects, (('cv_ratio', False), ('volume', False)))
ordered_bins = multisort(bin_objects, (('cv_ratio', False), ('volume', True)))

#ordering items in I according to non-increasing order of volume
ordered_items = sorted(item_objects, key = attrgetter('volume'), reverse = True)

print(ordered_bins)
print(ordered_items)

start = timeit.default_timer()

#running heuristic on ordered items
base_result = packing_bins(ordered_items, ordered_bins)
base_cost = base_result.cost
base_num = len(base_result.filled_bins)

end = timeit.default_timer()

print(base_result.filled_bins)
print(base_result.cost)
print(end-start)

#pr.disable()
#s = io.StringIO()
#ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
#ps.print_stats()

#with open('test_10000_20000.txt', 'w+') as f:
#    f.write(s.getvalue())


with open('out.txt', 'w') as f:
    sys.stdout = f
    print(base_result)

#cProfile.run('packing_bins(ordered_items, ordered_bins)')
