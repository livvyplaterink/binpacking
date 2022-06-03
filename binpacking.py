
#defining item volume
item_volume = {
        "i1" : 2,
        "i2" : 6,
        "i3" : 20, 
        "i6" : 25, 
        "i7" : 72,
        "i8" : 44,
        "i9" : 26
        }

#defining bin volume
bin_volume = {
        "b1" : 60,
        "b2" : 80,
        "b3" : 100,
        "b4" : 120, 
        "b5" : 150
        }

#defining bin cost
bin_cost = {
        "b1" : 1, 
        "b2" : 3, 
        "b3" : 2,
        "b4" : 8, 
        "b5" : 13
        }



#defining ordered item list
ordered_items = []

for key in item_volume:
    ordered_items.append(key)



#sorting items according to non-increasing order of volume
def partition_1(volume_dict, item_list, start, end): 
    pivot = volume_dict[item_list[start]]
    low = start + 1
    high = end 
    while True: 
        while low <= high and volume_dict[item_list[high]] <= pivot:
            high = high - 1
        while low <= high and volume_dict[item_list[low]] >= pivot: 
            low = low + 1
        if low <= high: 
            item_list[low], item_list[high] = item_list[high], item_list[low] 
        else:
            break
    item_list[start], item_list[high] = item_list[high], item_list[start]
    return high

def quick_sort_1(volume_dict, item_list, start, end): 
    if start >= end: 
        return 

    p = partition_1(volume_dict, item_list, start, end)
    quick_sort_1(volume_dict, item_list, start, p-1) 
    quick_sort_1(volume_dict, item_list, p+1, end)

quick_sort_1(item_volume, ordered_items, 0, len(ordered_items)-1) 
#print("ordered items: " + str(ordered_items))



#defining ordered bins list 
ordered_bins = []
cv_ratio = {} 

for key in bin_volume: 
    ordered_bins.append(key)
    cv_ratio[key] = bin_cost[key] / bin_volume[key]



#defining ordering function for set K: this order the bins according to non-decreasing order of the ratio c_j/V_j and non-decreasing order of V_j when the cost ratios c_j/V_j are equal 
def partition_2(cv_dict, volume_dict, bin_list, start, end): 
    pivot_cv = cv_dict[bin_list[start]]
    pivot_v = volume_dict[bin_list[start]]
    low = start + 1
    high = end 
    while True: 
        while low <= high and ((cv_dict[bin_list[high]] > pivot_cv) or ((cv_dict[bin_list[high]] == pivot_cv) and (volume_dict[bin_list[high]] >= pivot_v))):
            high = high - 1
        while low <= high and ((cv_dict[bin_list[low]] < pivot_cv) or ((cv_dict[bin_list[low]] == pivot_cv) and (volume_dict[bin_list[low]] <= pivot_v))): 
            low = low + 1
        if low <= high:
            bin_list[low], bin_list[high] = bin_list[high], bin_list[low]
        else: 
            break
    bin_list[start], bin_list[high] = bin_list[high], bin_list[start]
    return high 

def quick_sort_2(cv_dict, volume_dict, bin_list, start, end): 
    if start >= end: 
        return
    p = partition_2(cv_dict, volume_dict, bin_list, start, end) 
    quick_sort_2(cv_dict, volume_dict, bin_list, start, p-1)
    quick_sort_2(cv_dict, volume_dict, bin_list, p+1, end) 

quick_sort_2(cv_ratio, bin_volume, ordered_bins, 0, len(ordered_bins)-1)
#print("cv ratio: " + str(cv_ratio))
#print("ordered bins " + str(ordered_bins))



#defining ordering function for set S: this orders the bins according to non-increasing order of the volume V_j and non-decreasing order of c_j/V_j when the volumes are equal 
def partition_3(cv_dict, volume_dict, bin_list, start, end): 
    pivot_cv = cv_dict[bin_list[start]]
    pivot_v = volume_dict[bin_list[start]]
    low = start + 1
    high = end 
    while True: 
        while low <= high and ((volume_dict[bin_list[high]] < pivot_v) or ((volume_dict[bin_list[high]] == pivot_v) and (cv_dict[bin_list[high]] >= pivot_cv))):
            high = high - 1
        while low <= high and ((volume_dict[bin_list[low]] > pivot_v) or ((volume_dict[bin_list[low]] == pivot_v) and (cv_dict[bin_list[low]] <= pivot_cv))):
            low = low + 1
        if low <= high: 
            bin_list[low], bin_list[high] = bin_list[high], bin_list[low]
        else: 
            break 
    bin_list[start], bin_list[high] = bin_list[high], bin_list[start] 
    return high 

def quick_sort_3(cv_dict, volume_dict, bin_list, start, end): 
    if start >= end: 
        return 
    p = partition_3(cv_dict, volume_dict, bin_list, start, end) 
    quick_sort_3(cv_dict, volume_dict, bin_list, start, p-1)
    quick_sort_3(cv_dict, volume_dict, bin_list, p+1, end)



#defining filled bins set (S)
filled_bins = {}
filled_bin_volume = {}
ordered_filled_bins = []
#print("initial ordered filled bins: " + str(ordered_filled_bins))
#print("initial bin volumes: " + str(filled_bin_volume))

print(ordered_items)
print(ordered_bins)



#placing items in bins
for i in ordered_items: 
    print(ordered_filled_bins)
    if len(ordered_filled_bins) == 0: 
        for l in ordered_bins:
            print("i: " + str(i))
            print("l: " + str(l))
            if item_volume[i] > bin_volume[l]:
                print("item volume:  " + str(item_volume[i]))
                print("bin volume: " + str(bin_volume[l]))
                print("item " + str(i) + " of volume " + str(item_volume[i]) + " too large for bin " + str(l) + " with volume " + str(bin_volume[l]))
                continue 
            print("item volume:  " + str(item_volume[i]))
            print("bin volume: " + str(bin_volume[l]))
            print("item " + str(i) + " of volume " + str(item_volume[i]) + " fits in bin " + str(l) + " with volume " + str(bin_volume[l]))
            filled_bins[l] = [i]
            filled_bin_volume[l] = bin_volume[l] - item_volume[i]
            ordered_filled_bins.append(l)
            quick_sort_3(cv_ratio, filled_bin_volume, ordered_filled_bins, 0, len(ordered_filled_bins) - 1)
            print("filled bins: " + str(filled_bins))
            print("ordered filled bins: " + str(ordered_filled_bins))
            print("filled bin volume: " + str(filled_bin_volume))
            break
    else: 
        for b in ordered_filled_bins:
            print("i: " + str(i))
            print("b: " + str(b))
            print("item volume:  " + str(item_volume[i]))
            print("bin volume: " + str(filled_bin_volume[b]))
            if item_volume[i] <= filled_bin_volume[b]:
                print("item " + str(i) + " of volume " + str(item_volume[i]) + " fits in bin " + str(b) + " with remaining volume " + str(filled_bin_volume[b]))
                filled_bins[b].append(i)
                filled_bin_volume[b] = filled_bin_volume[b] - item_volume[i]
                quick_sort_3(cv_ratio, filled_bin_volume, ordered_filled_bins, 0, len(ordered_filled_bins) - 1)
                print("filled bins: " + str(filled_bins))
                print("ordered filled bins: " + str(ordered_filled_bins))
                print("filled bin volume: " + str(filled_bin_volume))
                break 
            if b == ordered_filled_bins[len(ordered_filled_bins)-1]:
                if item_volume[i] > filled_bin_volume[b]:
                    print("item " + str(i) + " of volume " + str(item_volume[i]) + " too large for bin " + str(b) + " with remaining volume " + str(filled_bin_volume[b]))
                    for j in ordered_bins:
                        print("i: " + str(i))
                        print("j: " + str(j))
                        print("item volume " + str(item_volume[i]))
                        print("new bin volume " + str(bin_volume[j]))
                        if j in filled_bins: 
                            print(str(j) + " is in filled_bins")
                            continue
                        if item_volume[i] > bin_volume[j]: 
                            print("item " + str(i) + " of volume " + str(item_volume[i]) + " too large for new bin " + str(j) + " with volume " + str(bin_volume[j]))
                            continue
                        print("item " + str(i) + " of volume " + str(item_volume[i]) + " fits in new bin " + str(j) + " with volume " + str(bin_volume[j]))
                        filled_bins[j] = [i]
                        filled_bin_volume[j] = bin_volume[j] - item_volume[i]
                        ordered_filled_bins.append(j)
                        quick_sort_3(cv_ratio, filled_bin_volume, ordered_filled_bins, 0, len(ordered_filled_bins) - 1) 
                        print("filled bins: " + str(filled_bins))
                        print("ordered filled bins: " + str(ordered_filled_bins))
                        print("filled bin volume: " + str(filled_bin_volume))
                        break
                    break
print(filled_bins)
cost = 0
for b in filled_bins:
    cost+=bin_cost[b]
print(cost)
#print(ordered_bins)
#print(ordered_filled_bins)


unfilled_bins = [] 
for j in ordered_bins: 
    if j not in ordered_filled_bins: 
        unfilled_bins.append(j)
#print(unfilled_bins)
#print(item_volume)


for b in ordered_filled_bins: 
    v_b = 0 
    for i in filled_bins[b]: 
        v_b += item_volume[i]
#    print(v_b)
    for k in unfilled_bins:
#        print( "k: " + str(k) + " volume: " + str(bin_volume[k]))
#        print( "b: " + str(b) + " volume: " + str(bin_volume[b]))
#        print(v_b)
#        print( "k: " + str(k) + " bin cost: " + str(bin_cost[k]))
#        print( "b: " + str(b) + " bin cost: " + str(bin_cost[b]))
        if (bin_volume[k] >= v_b) and (bin_cost[k] < bin_cost[b]): 
            filled_bins[k] = filled_bins[b] 
            filled_bin_volume[k] = bin_volume[k] - v_b
            ordered_filled_bins.append(k)
            del filled_bins[b]
            del filled_bin_volume[b] 
            ordered_filled_bins.remove(b)

#print(filled_bins)
#print(filled_bin_volume)
#print(ordered_filled_bins)
cost = 0
for b in filled_bins: 
    cost += bin_cost[b]
#print(cost)

