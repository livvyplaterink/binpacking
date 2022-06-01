
#defining item volume
item_volume = {
        "i1" : 5,
        "i2" : 15,
        "i3" : 4,
        "i4" : 8,
        "i5" : 13,
        "i6" : 8,
        }

#defining bin volume
bin_volume = {
        "b1" : 5,
        "b2" : 20,
        "b3" : 7,
        "b4" : 10,
        "b5" : 9,
        "b6" : 22, 
        "b7" : 28,
        "b8" : 24
        }

#defining bin cost
bin_cost = {
        "b1" : 1, 
        "b2" : 4, 
        "b3" : 2,
        "b4" : 2,
        "b5" : 1, 
        "b6" : 5, 
        "b7" : 6, 
        "b8" : 4
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
print("ordered items: " + str(ordered_items))

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
print("cv ratio: " + str(cv_ratio))
print("ordered bins " + str(ordered_bins))

#filled_bins = {}
#filled_bin_volume = {}
#ordered_filled_bins = []

filled_bins = {} 
filled_bin_volume = {
        "b11" : 6,
        "b22" : 30, 
        "b33" : 22,
        }
ordered_filled_bins = ["b11", "b22", "b33"] 

quick_sort_1(filled_bin_volume, ordered_filled_bins, 0, len(ordered_filled_bins)-1)
print("initial ordered filled bins: " + str(ordered_filled_bins))
print("initial bin volumes: " + str(filled_bin_volume))

for i in ordered_items: 
    for b in ordered_filled_bins: 
        if item_volume[i] <= filled_bin_volume[b]: 
            if b in filled_bins:
                filled_bins[b].append(i)
            else: 
                filled_bins[b] = []
                filled_bins[b].append(i)
            filled_bin_volume[b] = filled_bin_volume[b] - item_volume[i] 
            quick_sort_1(filled_bin_volume, ordered_filled_bins, 0, len(ordered_filled_bins)-1)           
            print("reordered bins: " + str(ordered_filled_bins))
            print("new bin volume: " + str(filled_bin_volume))
            break
        elif item_volume[i] > filled_bin_volume[len(filled_bins)] 
print(filled_bins)





#filled_bins = {}
#filled_bin_volume = bin_volume
#
#for b in ordered_bins: 
#    filled_bins[b]  = []
#
#for i in ordered_items:
#    for b in filled_bins: 
#        if item_volume[i] <= filled_bin_volume[b]:
#            filled_bins[b].append(i)
#
#    for b in ordered_bins:  
#        if item_volume[i] <= filled_bin_volume[b]:
#            filled_bins[b].append(i)
#            filled_bin_volume[b] = filled_bin_volume[b] - item_volume[i]
#            break

#print("filled bins : " + str(filled_bins))
