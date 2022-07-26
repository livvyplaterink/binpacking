from sorting_objects import *
import sys
from operator import attrgetter

def packing_bins(item_list, bin_list): 
    filled_bins = []
    filled_bins2 = []
    for i in item_list:
        #print(bin_list)
        #print(filled_bins)
        #if S is empty, put the largest item i into the first bin in K that accomodates i
        if len(filled_bins) == 0: 
            for l in bin_list:
                #print("i: " + str(i.name))
                #print("l: " + str(l.name))
                if i.volume > l.remaining_volume:
                    #if i cannot be accomodated into any bin in K, return an empty filled bin list 
                    if l == bin_list[len(bin_list)-1]: 
                        cost = -1
                        result = filled_bin_list([], cost)
                        return(result)
                    else: 
                        continue
                #print("item volume: " + str(i.volume))
                #print("bin volume: " + str(l.remaining_volume))
                #print("item " + str(i.name) + " of volume " + str(i.volume) + " fits in bin " + str(l.name) + " with volume " + str(l.remaining_volume))
                l.items_contained.append(i)
                l.remaining_volume -= i.volume
                #if l's remaining volume is less than the volume of the smallest item, l is completely full  
                if l.remaining_volume < item_list[len(item_list)-1].volume:
                    #print(l.remaining_volume)
                    #print(item_list[len(item_list)-1])
                    filled_bins2.append(l)
                #otherwise, l is partially full 
                else: 
                    filled_bins.append(l) 
                bin_list.remove(l) 
                #print("filled bins " , filled_bins)
                break
        else: 
            #if S is not empty, and if i cannot be accomodated into a bin in S, then loop through the unfilled bins and place i into the first bin in K that can accomodate its volume  
            if i.volume > filled_bins[len(filled_bins)-1].remaining_volume:
                for j in bin_list:
                    #print("i: " + str(i.name))
                    #print("j: " + str(j.name))
                    #print("item volume: " + str(i.volume))
                    #print("new bin volume: " + str(j.remaining_volume))
                    if i.volume > j.remaining_volume:
                        #print("item " + str(i.name) + " of volume " + str(i.volume) + " too large for new bin " + str(j.name) + " with remaining volume " + str(j.remaining_volume))
                        if j == bin_list[len(bin_list)-1]:
                            cost = -1
                            result = filled_bin_list([], cost)
                            return(result)
                        else:
                            continue
                    #print("item " + str(i.name) + " of volume " + str(i.volume) + " fits in new bin " + str(j.name) + " with remaining volume " + str(j.remaining_volume))
                    j.items_contained.append(i)
                    j.remaining_volume -= i.volume
                    #if j's remaining volume is less than the volume of the smallest item, j is completely full
                    if j.remaining_volume < item_list[len(item_list)-1].volume:
                        filled_bins2.append(j)
                    #otherwise, j is partially full
                    else:
                        filled_bins.append(j)
                    bin_list.remove(j)

                    #ordering bins in S according to non-decreasing order of remaining volume and non-decreasing order of c_j/V_j when the remaining volumes are equal
                    #filled_bins.sort(key = attrgetter('remaining_volume', 'cost'))
                    filled_bins.sort(key = attrgetter('remaining_volume', 'cv_ratio'))
                    #filled_bins.sort(key = lambda x: (x.remaining_volume, x.volume))
                    
                    #filled_bins.sort(key = attrgetter('remaining_volume', 'volume'))
                    #filled_bins.sort(key = lambda x: (x.remaining_volume, x.cv_ratio))
                    #filled_bins = sorted(filled_bins, key = lambda x: (x.remaining_volume, x.cv_ratio))
                    #filled_bins = multisort(filled_bins, (('remaining_volume', False), ('cv_ratio', False)))
                    #print("filled bins " , filled_bins)

                    break 
            else:
                #if S is not empty and if i can be accomodated into a bin in S, then place i into the first bin in S that can accomodate its volume 
                #print(filled_bins)
                #print("i: " , i)
                b = binary_search(filled_bins, 0, len(filled_bins)-1, i)
                #print("b: " , b.name)
                b.items_contained.append(i) 
                b.remaining_volume -= i.volume

                #if b's remaining volume is less than the volume of the smallest item, b is completely full 
                if b.remaining_volume < item_list[len(item_list)-1].volume:
                    filled_bins2.append(b)    
                    filled_bins.remove(b) 
                
                #filled_bins.sort(key = attrgetter('remaining_volume', 'cost'))
                filled_bins.sort(key = attrgetter('remaining_volume', 'cv_ratio'))
                #filled_bins.sort(key = lambda x: (x.remaining_volume, x.volume))

                #filled_bins.sort(key = attrgetter('remaining_volume', 'volume'))

                #filled_bins.sort(key = lambda x: (x.remaining_volume, x.cv_ratio))
                #filled_bins = sorted(filled_bins, key = lambda x: (x.remaining_volume, x.cv_ratio))
                #filled_bins = multisort(filled_bins, (('remaining_volume', False), ('cv_ratio', False)))
                #print("filled bins " , filled_bins) 
    
    #ordering bins in S according to non-decreasing order of remaining volume and non-decreasing order of c_j/V_j when the remaining volumes are equal
    filled_bins += filled_bins2
    #filled_bins.sort(key = attrgetter('remaining_volume', 'cost'))
    filled_bins.sort(key = attrgetter('remaining_volume', 'cv_ratio'))
    #filled_bins.sort(key = lambda x: (x.remaining_volume, x.volume))

    #filled_bins.sort(key = attrgetter('remaining_volume', 'volume'))

    #filled_bins.sort(key = lambda x: (x.remaining_volume, x.cv_ratio))
    #filled_bins = sorted(filled_bins, key = lambda x: (x.remaining_volume, x.cv_ratio))
    #filled_bins = multisort(filled_bins, (('remaining_volume', False), ('cv_ratio', False)))

    #showing original cost before postprocessing step
    cost1 = 0 
    for b in filled_bins: 
        cost1+= b.cost 

    #ordering bins in K\S according to non-decreasing order of cost and non-increasing order of volume when costs are equal
    unfilled_bins = bin_list
    unfilled_bins.sort(key = lambda x: (x.cost, -x.volume))
    #num_replaced = 0 
    #unfilled_bins = multisort(bin_list, (('cost', False), ('volume', True)))
    for n in range(len(filled_bins)):
        b = filled_bins[n]
        v_b = 0
        for i in b.items_contained:
            v_b += i.volume
        for k in unfilled_bins:
            if (k.volume >= v_b) and (k.cost < b.cost):
                #print(b) 
                #print(k) 
                #print(b, " being replaced by " , k)
                k.items_contained = b.items_contained
                b.items_contained = []
                k.remaining_volume -= v_b
                b.remaining_volume = b.volume
                unfilled_bins.remove(k)
                unfilled_bins.append(b)
                filled_bins[n] = k
                unfilled_bins.sort(key = lambda x: (x.cost, -x.volume))
                #num_replaced += 1
                #unfilled_bins = sorted(unfilled_bins, key = lambda x: (x.cost, -x.volume))
                #unfilled_bins = multisort(unfilled_bins, (('cost', False), ('volume', True)))
                break

    cost = 0 
    for b in filled_bins:
        cost += b.cost 
    
    #print("num replaced " , num_replaced)

    result = filled_bin_list(filled_bins, cost) 

    return(result ) 
