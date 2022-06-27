from sorting_objects import *

def packing_bins(item_list, bin_list): 
    filled_bins = []
    for i in item_list:
        #if S is empty, put the largest item i into the first bin in K that accomodates i
        if len(filled_bins) == 0: 
            for l in bin_list:
                if i.volume > l.remaining_volume:
                    continue
                filled_bins.append(l)
                l.items_contained.append(i)
                l.remaining_volume -= i.volume
                #ordering bins in S according to non-decreasing order of remaining volume and non-decreasing order of c_j/V_j when the remaining volumes are equal
                filled_bins = multisort(filled_bins, (('remaining_volume', False), ('cv_ratio', False)))
                break
        else: 
            #if S is not empty, and if i can be accomodated into a bin in S, then place it into the bin into the first bin in S that can accomodate i
            for b in filled_bins: 
                if i.volume <= b.remaining_volume: 
                    b.items_contained.append(i)
                    b.remaining_volume -= i.volume
                    filled_bins = multisort(filled_bins, (('remaining_volume', False), ('cv_ratio', False)))
                    break 
                #if S is not empty and if i cannot be accomodated into a bin in S, then place it into the first bin in K that can accommodate i
                if b == filled_bins[len(filled_bins)-1]: 
                    if i.volume > b.remaining_volume: 
                        for j in bin_list: 
                            if j in filled_bins:
                                continue
                            if i.volume > j.remaining_volume: 
                                continue
                            filled_bins.append(j)
                            j.items_contained.append(i)
                            j.remaining_volume -= i.volume 
                            #ordering bins in S according to non-decreasing order of remaining volume and non-decreasing order of c_j/V_j when the remaining volumes are equal
                            filled_bins = multisort(filled_bins, (('remaining_volume', False), ('cv_ratio', False)))
                            break 
                        break
    
    #ordering bins in S according to non-decreasing order of remaining volume and non-decreasing order of c_j/V_j when the remaining volumes are equal
    filled_bins = multisort(filled_bins, (('remaining_volume', False), ('cv_ratio', False)))
    
    #showing original cost before postprocessing step
    cost1 = 0 
    for b in filled_bins: 
        cost1+= b.cost 

    #defining unfilled bin set K\S
    unfilled_bins = []
    for j in bin_list: 
        if j not in filled_bins: 
            unfilled_bins.append(j) 

    #ordering bins in K\S according to non-decreasing order of cost and non-increasing order of volume when costs are equal
    unfilled_bins = multisort(unfilled_bins, (('cost', False), ('volume', True)))
    for n in range(len(filled_bins)):
        b = filled_bins[n]
        v_b = 0
        for i in b.items_contained:
            v_b += i.volume
        for k in unfilled_bins:
            if (k.volume >= v_b) and (k.cost < b.cost):
                k.items_contained = b.items_contained
                b.items_contained = []
                k.remaining_volume -= v_b
                b.remaining_volume = b.volume
                unfilled_bins.remove(k)
                unfilled_bins.append(b)
                filled_bins[n] = k
                unfilled_bins = multisort(unfilled_bins, (('cost', False), ('volume', True)))
                break


    cost = 0 
    for b in filled_bins:
        cost += b.cost 

    result = filled_bin_list(filled_bins, cost) 

    return(result ) 
