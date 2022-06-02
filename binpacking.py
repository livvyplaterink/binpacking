
#defining item volume
item_volume = {
        "i1" : 5,
        "i2" : 15,
        "i3" : 4,
        "i4" : 8,
        }

#defining bin volume
bin_volume = {
        "b1" : 5,
        "b2" : 20,
        "b3" : 7,
        "b4" : 10,
        "b5" : 9,
        }

#defining bin cost
bin_cost = {
        "b1" : 1, 
        "b2" : 4, 
        "b3" : 2,
        "b4" : 2,
        "b5" : 1, 
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

#sorting bins according to non-decreasing order of the ratio c_j/V_j and non-increasing order of V_j when the unit costs c_j are equal 
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

filled_bins = {}
filled_bin_volume = {}
ordered_filled_bins = []

k = ordered_bins[0]
filled_bins[k] = [] 
filled_bin_volume[k] = bin_volume[k]
ordered_filled_bins.append(k)


quick_sort_1(filled_bin_volume, ordered_filled_bins, 0, len(ordered_filled_bins)-1)
print("initial ordered filled bins: " + str(ordered_filled_bins))
print("initial bin volumes: " + str(filled_bin_volume))

print(ordered_items)
print(ordered_bins)

for i in ordered_items:
    for b in ordered_filled_bins:
        print("b: " + str(b))
        if item_volume[i] <= filled_bin_volume[b]:
            print("no new bins added")
            print("item " + str(i) + " of volume " + str(item_volume[i]) + " fits in bin " + str(b) + " of volume " + str(filled_bin_volume[b]))
            filled_bins[b].append(i)
            filled_bin_volume[b] = filled_bin_volume[b] - item_volume[i]
            quick_sort_1(filled_bin_volume, ordered_filled_bins, 0, len(ordered_filled_bins)-1)
            break
        if b == ordered_filled_bins[len(ordered_filled_bins)-1]:
            if item_volume[i] > filled_bin_volume[ordered_filled_bins[len(ordered_filled_bins)-1]]:
                print("item " + str(i) + " of volume " + str(item_volume[i]) + " too large for bin " + str(b) + " with remaining volume " + str(filled_bin_volume[b]))
                for j in ordered_bins:
                    print(i)
                    print(j)
                    if j in filled_bins:
                        continue
                    else:
                        filled_bins[j] = []
                        filled_bin_volume[j] = bin_volume[j]
                        ordered_filled_bins.append(j)
                        quick_sort_1(filled_bin_volume, ordered_filled_bins, 0, len(ordered_filled_bins)-1)
                        if item_volume[i] <= filled_bin_volume[j]: 
                            print("item " + str(i) + " of volume " + str(item_volume[i]) + " fits in bin " + str(j) + " of volume " + str(filled_bin_volume[j]))
                            filled_bins[j].append(i)
                            filled_bin_volume[j] = filled_bin_volume[j] - item_volume[i]
                            quick_sort_1(filled_bin_volume, ordered_filled_bins, 0, len(ordered_filled_bins)-1)
                            break
        break
print(filled_bins)


#    if (len(ordered_filled_bins) == 0) or (item_volume[i] > filled_bin_volume[ordered_filled_bins[len(ordered_filled_bins)-1]]):
#        print(i)
#        for j in ordered_bins:
#            if j in filled_bins: 
#                continue
#            else:
#                filled_bins[j] = []
#                filled_bin_volume[j] = bin_volume[j]
#                ordered_filled_bins.append(j)
#                print(ordered_filled_bins)
#                print(i)
#                print(j)
#                quick_sort_1(filled_bin_volume, ordered_filled_bins, 0, len(ordered_filled_bins)-1)
#            if item_volume[i] <= filled_bin_volume[j]:
#                print(item_volume[i])
#                print(filled_bin_volume[j])
#                filled_bins[j].append(i)
#                filled_bin_volume[j] = filled_bin_volume[j] - item_volume[i]
#                quick_sort_1(filled_bin_volume, ordered_filled_bins, 0, len(ordered_filled_bins)-1)
#                break
#    else: 
#        for b in ordered_filled_bins: 
#            if item_volume[i] <= filled_bin_volume[b]:
#                print(ordered_filled_bins)
#                print(i)
#                print(b)
#                filled_bins[b].append(i)
#                filled_bin_volume[b] = filled_bin_volume[b] - item_volume[i]
#                quick_sort_1(filled_bin_volume, ordered_filled_bins, 0, len(ordered_filled_bins)-1)
#                break

   

#    if len(ordered_filled_bins) == 0:
#        filled_bins[ordered_bins[0]] = []
#        filled_bin_volume[ordered_bins[0]] = bin_volume[ordered_bins[0]]
#        ordered_filled_bins.append(ordered_bins[0])
#        del(ordered_bins[0])
#        print(filled_bins)
#        print(filled_bin_volume)
#        print(ordered_filled_bins)
#        print(ordered_bins)
#    else:
#        for b in ordered_filled_bins: 
#            if item_volume[i] <= filled_bin_volume[b]: 
#                filled_bins[b].append(i)
#                filled_bin_volume[b] = filled_bin_volume[b] - item_volume[i] 
#                quick_sort_1(filled_bin_volume, ordered_filled_bins, 0, len(ordered_filled_bins)-1)           
#                print("reordered bins: " + str(ordered_filled_bins))
#                print("new bin volume: " + str(filled_bin_volume))
#                break
#            if b == ordered_filled_bins[len(ordered_filled_bins)-1]:
#                if item_volume[i] > filled_bin_volume[ordered_filled_bins[len(ordered_filled_bins)-1]]:
#                    print("item too large")
#                    for j in ordered_bins:
#                        print("j: " + str(j))
#                        filled_bins[j] = []
#                        filled_bin_volume[j] = bin_volume[j]
#                        ordered_filled_bins.append(j)
#                        print(filled_bins)
#                        print(filled_bin_volume)
#                        print(ordered_filled_bins)
##                        if item_volume[i] <= filled_bin_volume[j]: 
#                            filled_bins[ordered_bins[0]].append(i)
#                            filled_bin_volume[j] = filled_bin_volume[j] - item_volume[i]
#                            quick_sort_1(filled_bin_volume, ordered_filled_bins, 0, len(ordered_filled_bins)-1)
#                            print("reordered bins: " + str(ordered_filled_bins))
#                            print("new bin volume: " + str(filled_bin_volume))
#                            break
                    

#                    quick_sort_1(filled_bin_volume, ordered_filled_bins, 0, len(ordered_filled_bins)-1)
#                    del(ordered_bins[0])
#                    print("reordered bins: " + str(ordered_filled_bins))
#                    print("new bin volume: " + str(filled_bin_volume))
#                    print("ordered bins (not filled): " + str(ordered_bins))
#                    break
            #print("last filled bin volume: " + str(filled_bin_volume[filled_bins[len(filled_bins)]]))
            #elif item_volume[i] > filled_bin_volume[len(filled_bins)] 
print(filled_bins)




