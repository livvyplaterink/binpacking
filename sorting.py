#this file defines ordering functions that are used in binpacking2

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

def item_sort(volume_dict, item_list, start, end):
    if start >= end: 
        return 
    p = partition_1(volume_dict, item_list, start, end)
    item_sort(volume_dict, item_list, start, p-1) 
    item_sort(volume_dict, item_list, p+1, end)

#defining ordering function  for set K: this orders the bins according to non-decreasing order of the ratio c_j/V_j and non-decreasing order of V_j when the cost ratios c_j/V_j are equal
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

def bin_sort_cv(cv_dict, volume_dict, bin_list, start, end): 
    if start >= end: 
        return
    p = partition_2(cv_dict, volume_dict, bin_list, start, end) 
    bin_sort_cv(cv_dict, volume_dict, bin_list, start, p-1)
    bin_sort_cv(cv_dict, volume_dict, bin_list, p+1, end)

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

def bin_sort_volume(cv_dict, volume_dict, bin_list, start, end): 
    if start >= end: 
        return 
    p = partition_3(cv_dict, volume_dict, bin_list, start, end) 
    bin_sort_volume(cv_dict, volume_dict, bin_list, start, p-1)
    bin_sort_volume(cv_dict, volume_dict, bin_list, p+1, end)

#alternate sorting for S
def partition_6(cv_dict, volume_dict, bin_list, start, end):
    pivot_cv = cv_dict[bin_list[start]]
    pivot_v = volume_dict[bin_list[start]]
    low = start + 1
    high = end
    while True:
        while low <= high and ((volume_dict[bin_list[high]] > pivot_v) or ((volume_dict[bin_list[high]] == pivot_v) and (cv_dict[bin_list[high]] >= pivot_cv))):
            high = high - 1
        while low <= high and ((volume_dict[bin_list[low]] < pivot_v) or ((volume_dict[bin_list[low]] == pivot_v) and (cv_dict[bin_list[low]] <= pivot_cv))):
            low = low + 1
        if low <= high:
            bin_list[low], bin_list[high] = bin_list[high], bin_list[low]
        else:
            break
    bin_list[start], bin_list[high] = bin_list[high], bin_list[start]
    return high

def bin_sort_volume2(cv_dict, volume_dict, bin_list, start, end):
    if start >= end:
        return
    p = partition_6(cv_dict, volume_dict, bin_list, start, end)
    bin_sort_volume2(cv_dict, volume_dict, bin_list, start, p-1)
    bin_sort_volume2(cv_dict, volume_dict, bin_list, p+1, end)

#orders unfilled bins by non-decreasing order of cost and non-increasing order of volume when the costs are equal 
def partition_4(cost_dict, volume_dict, bin_list, start, end): 
    pivot_c = cost_dict[bin_list[start]]
    pivot_v = volume_dict[bin_list[start]]
    low = start + 1
    high = end 
    while True: 
        while low <= high and ((cost_dict[bin_list[high]] > pivot_c) or ((cost_dict[bin_list[high]] == pivot_c) and (volume_dict[bin_list[high]] <= pivot_v))): 
            high = high -1
        while low <= high and ((cost_dict[bin_list[low]] < pivot_c) or ((cost_dict[bin_list[low]] == pivot_c) and (volume_dict[bin_list[low]] >= pivot_v))): 
            low = low + 1
        if low <= high: 
            bin_list[low], bin_list[high] = bin_list[high], bin_list[low]
        else: 
            break
    bin_list[start], bin_list[high] = bin_list[high], bin_list[start]
    return high 

def bin_sort_cost(cost_dict, volume_dict, bin_list, start, end): 
    if start >= end: 
        return
    p = partition_4(cost_dict, volume_dict, bin_list, start, end)
    bin_sort_cost(cost_dict, volume_dict, bin_list, start, p-1)
    bin_sort_cost(cost_dict, volume_dict, bin_list, p+1, end)

#orders unfilled bins by non-decreasing order of cost and non-decreasing order of volume when the costs are equal
def partition_5(cost_dict, volume_dict, bin_list, start, end):
    pivot_c = cost_dict[bin_list[start]]
    pivot_v = volume_dict[bin_list[start]]
    low = start + 1
    high = end
    while True:
        while low <= high and ((cost_dict[bin_list[high]] > pivot_c) or ((cost_dict[bin_list[high]] == pivot_c) and (volume_dict[bin_list[high]] >= pivot_v))):
            high = high -1
        while low <= high and ((cost_dict[bin_list[low]] < pivot_c) or ((cost_dict[bin_list[low]] == pivot_c) and (volume_dict[bin_list[low]] <= pivot_v))):
            low = low + 1
        if low <= high:
            bin_list[low], bin_list[high] = bin_list[high], bin_list[low]
        else:
            break
    bin_list[start], bin_list[high] = bin_list[high], bin_list[start]
    return high

def bin_sort_cost2(cost_dict, volume_dict, bin_list, start, end):
    if start >= end:
        return
    p = partition_5(cost_dict, volume_dict, bin_list, start, end)
    bin_sort_cost2(cost_dict, volume_dict, bin_list, start, p-1)
    bin_sort_cost2(cost_dict, volume_dict, bin_list, p+1, end)
