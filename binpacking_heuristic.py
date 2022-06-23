from sorting_objects import *

def packing_bins(ordered_items, ordered_bins): 
    filled_bins = []
    for i in ordered_items:
        #if S is empty, put the largest item i into the first bin in K that accomodates i
        if len(filled_bins) == 0: 
            for l in ordered_bins:
                #print("i: " + str(i.name))
                #print("l: " + str(l.name))
                if i.volume > l.remaining_volume:
                    continue
                #print("item volume: " + str(i.volume))
                #print("bin volume: " + str(l.remaining_volume))
                #print("item " + str(i.name) + " of volume " + str(i.volume) + " fits in bin " + str(l.name) + " with volume " + str(l.remaining_volume))
                filled_bins.append(l)
                l.items_contained.append(i)
                l.remaining_volume -= i.volume
                #ordering bins in S according to non-decreasing order of remaining volume and non-decreasing order of c_j/V_j when the remaining volumes are equal
                filled_bins = multisort(filled_bins, (('remaining_volume', False), ('cv_ratio', False)))
                #print(filled_bins)
                break
        else: 
            #if S is not empty, and if i can be accomodated into a bin in S, then place it into the bin into the first bin in S that can accomodate i
            for b in filled_bins: 
                #print("i: " + str(i.name))
                #print("b: " + str(b.name))
                #print("item volume: " + str(i.volume))
                #print("bin volume: " + str(b.remaining_volume))
                if i.volume <= b.remaining_volume: 
                    #print("item " + str(i.name) + " of volume " + str(i.volume) + " fits in bin " + str(b.name) + " with remaining volume " + str(b.remaining_volume))
                    b.items_contained.append(i)
                    b.remaining_volume -= i.volume
                    filled_bins = multisort(filled_bins, (('remaining_volume', False), ('cv_ratio', False)))
                    #print(filled_bins)
                    break 
                #if S is not empty and if i cannot be accomodated into a bin in S, then place it into the first bin in K that can accommodate i
                if b == filled_bins[len(filled_bins)-1]: 
                    if i.volume > b.remaining_volume: 
                        #print("item " + str(i.name) + " of volume " + str(i.volume) + " too large for bin " + str(b.name) + " with remaining volume " + str(b.remaining_volume))
                        for j in ordered_bins: 
                            #print("i: " + str(i.name))
                            #print("j: " + str(j.name))
                            #print("item volume: " + str(i.volume))
                            #print("new bin volume: " + str(j.remaining_volume))
                            if j in filled_bins:
                                #print(str(j.name) + " is in filled bins")
                                continue
                            if i.volume > j.remaining_volume: 
                                #print("item " + str(i.name) + " of volume " + str(i.volume) + " too large for new bin " + str(j.name) + " with remaining volume " + str(j.remaining_volume))
                                continue
                            #print("item " + str(i.name) + " of volume " + str(i.volume) + " fits in new bin " + str(j.name) + " with remaining volume " + str(j.remaining_volume))
                            filled_bins.append(j)
                            j.items_contained.append(i)
                            j.remaining_volume -= i.volume 
                            #ordering bins in S according to non-decreasing order of remaining volume and non-decreasing order of c_j/V_j when the remaining volumes are equal
                            filled_bins = multisort(filled_bins, (('remaining_volume', False), ('cv_ratio', False)))
                            #print(filled_bins)
                            break 
                        break
    return(filled_bins)                         
