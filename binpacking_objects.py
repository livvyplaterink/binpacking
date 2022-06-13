from sorting_objects import *
from operator import attrgetter
import random

#randomly choosing the number of items from a list
item_number_list = [500, 600, 700, 800, 900]
item_number = random.choice(item_number_list)
print(item_number)

#randomly assigning volumes valued between 1 and 20 to the items
item_objects = []
for i in range(item_number):
    i_volume = random.randint(1, 40)
    item_objects.append(items('i'+str(i+1), i_volume))
print(item_objects)

#choosing the number of bins (number of items / 2)
bin_number = int(item_number / 2)

bin_objects = []
for i in range(bin_number):
    b_volume = random.randint(50, 80)
    b_cost = random.randint(1, 20)
    bin_objects.append(bins('b' + str(i+1), b_volume, b_volume, b_cost, 0, []))
print(bin_objects)



b1 = bins('b1', 20, 20, 4, 0, [])
b2 = bins('b2', 70, 70, 3, 0, [])
b3 = bins('b3', 20, 20, 6, 0, [])
b4 = bins('b4', 70, 70, 5, 0, [])
b5 = bins('b5', 50, 50, 4, 0, [])
b6 = bins('b6', 20, 20, 3, 0, [])
b7 = bins('b7', 60, 60, 9, 0, [])
b8 = bins('b8', 200, 200, 40, 0, [])
b9 = bins('b9', 100, 100, 20, 0, [])
b10 = bins('b10', 30, 30, 2, 0, [])                                                                          
b11 = bins('b11', 80, 80, 7, 0, [])

i1 = items('i1', 50)
i2 = items('i2', 60)
i3 = items('i3', 30)                                                                                        
i4 = items('i4', 20)
i5 = items('i5', 60)
i6 = items('i6', 10)
i7 = items('i7', 15)


bin_objects = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]

print(bin_objects)

item_objects = [i1, i2, i3, i4, i5, i6, i7]

#calculating cost/volume ratio for each bin 
for b in bin_objects:
    b.cv_ratio = b.cost / b.volume

#ordering bins in K according to non-decreasing order of the ratio c_j/V_j and non-decreasing order of V_j when the cost ratios c_j/V_j are equal
ordered_bins = multisort(bin_objects, (('cv_ratio', False), ('volume', False)))
print(ordered_bins)

#ordering items in I according to non-increasing order of volume
ordered_items = sorted(item_objects, key = attrgetter('volume'), reverse = True)
print(ordered_items)

filled_bins = []

#placing items in bins
for i in ordered_items:
    #if S is empty, put the largest item i into the first bin in K that accomodates i
    if len(filled_bins) == 0: 
        for l in ordered_bins:
            print("i: " + str(i.name))
            print("l: " + str(l.name))
            if i.volume > l.remaining_volume:
                continue
            print("item volume: " + str(i.volume))
            print("bin volume: " + str(l.remaining_volume))
            print("item " + str(i.name) + " of volume " + str(i.volume) + " fits in bin " + str(l.name) + " with volume " + str(l.remaining_volume))
            filled_bins.append(l)
            l.items_contained.append(i)
            l.remaining_volume -= i.volume
            #ordering bins in S according to non-decreasing order of remaining volume and non-decreasing order of c_j/V_j when the remaining volumes are equal
            filled_bins = multisort(filled_bins, (('remaining_volume', False), ('cv_ratio', False)))
            print(filled_bins)
            break
    else: 
        #if S is not empty, and if i can be accomodated into a bin in S, then place it into the bin into the first bin in S that can accomodate i
        for b in filled_bins: 
            print("i: " + str(i.name))
            print("b: " + str(b.name))
            print("item volume: " + str(i.volume))
            print("bin volume: " + str(b.remaining_volume))
            if i.volume <= b.remaining_volume: 
                print("item " + str(i.name) + " of volume " + str(i.volume) + " fits in bin " + str(b.name) + " with remaining volume " + str(b.remaining_volume))
                b.items_contained.append(i)
                b.remaining_volume -= i.volume
                filled_bins = multisort(filled_bins, (('remaining_volume', False), ('cv_ratio', False)))
                print(filled_bins)
                break 
            #if S is not empty and if i cannot be accomodated into a bin in S, then place it into the first bin in K that can accommodate i
            if b == filled_bins[len(filled_bins)-1]: 
                if i.volume > b.remaining_volume: 
                    print("item " + str(i.name) + " of volume " + str(i.volume) + " too large for bin " + str(b.name) + " with remaining volume " + str(b.remaining_volume))
                    for j in ordered_bins: 
                        print("i: " + str(i.name))
                        print("j: " + str(j.name))
                        print("item volume: " + str(i.volume))
                        print("new bin volume: " + str(j.remaining_volume))
                        if j in filled_bins:
                            print(str(j.name) + " is in filled bins")
                            continue
                        if i.volume > j.remaining_volume: 
                            print("item " + str(i.name) + " of volume " + str(i.volume) + " too large for new bin " + str(j.name) + " with remaining volume " + str(j.remaining_volume))
                            continue
                        print("item " + str(i.name) + " of volume " + str(i.volume) + " fits in new bin " + str(j.name) + " with remaining volume " + str(j.remaining_volume))
                        filled_bins.append(j)
                        j.items_contained.append(i)
                        j.remaining_volume -= i.volume 
                        #ordering bins in S according to non-decreasing order of remaining volume and non-decreasing order of c_j/V_j when the remaining volumes are equal
                        filled_bins = multisort(filled_bins, (('remaining_volume', False), ('cv_ratio', False)))
                        print(filled_bins)
                        break 
                    break

filled_bins = multisort(filled_bins, (('remaining_volume', False), ('cv_ratio', False)))
print("filled_Bins: " + str(filled_bins))

cost1 = 0 
for b in filled_bins: 
    cost1+= b.cost 
print("cost after filling bins: " + str(cost1)) 

#defining unfilled bin set K\S
unfilled_bins = []
for j in ordered_bins: 
    if j not in filled_bins: 
        unfilled_bins.append(j) 

#ordering bins in K\S according to non-decreasing order of cost and non-increasing order of volume when costs are equal
unfilled_bins = multisort(unfilled_bins, (('cost', False), ('volume', True)))
for n in range(len(filled_bins)):
    b = filled_bins[n]
    print(n)
    print(b.name)
    v_b = 0
    for i in b.items_contained:
        v_b += i.volume
    for k in unfilled_bins:
        if (k.volume >= v_b) and (k.cost < b.cost):
            print("unfilled bin: " + str(k.name) + " volume " + str(k.volume))
            print("filled bin: " + str(b.name) + " item volume " + str(v_b))
            print("unfilled bin " + str(k.name) + " cost " + str(k.cost))
            print("filled bin: " + str(b.name) + " cost " + str(b.cost))
            k.items_contained = b.items_contained
            b.items_contained = []
            k.remaining_volume -= v_b
            b.remaining_volume = b.volume
            unfilled_bins.remove(k)
            unfilled_bins.append(b)
            filled_bins[n] = k
            unfilled_bins = multisort(unfilled_bins, (('cost', False), ('volume', True)))
            print(filled_bins)
            break

for b in filled_bins: 
    print(b.remaining_volume)

print("cost after filling bins: " + str(cost1))

cost = 0 
for b in filled_bins:
    cost += b.cost 
print("final cost: " + str(cost))

