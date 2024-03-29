#this file defines the item and bin classes and defines a multi sort function which allows you to sort lists of objects based on multiple attributes 

from operator import attrgetter 

#defining item class: this contains the names and volumes of the items 
class items: 
    def __init__(self, name, volume):
        self.name = name 
        self.volume = volume 
    def __repr__(self): 
        return repr((self.name, self.volume))

#defining the bin class: this containes the name, volume, remaining volume, cost, cost/volume ratio, and item list of the bins 
class bins: 
    def __init__(self, name, volume, remaining_volume, cost, cv_ratio, items_contained):
        self.name = name
        self.volume = volume
        self.remaining_volume = remaining_volume
        self.cost = cost 
        self.cv_ratio = cv_ratio
        self.items_contained = items_contained 
    def __repr__(self): 
        return repr((self.name, self.volume, self.remaining_volume, self.cost, self.cv_ratio, self.items_contained))

#defining the multisort function: this allows you to sort the lists of objects according to different attributes. The specs should be a list of tuples that say the attribute and whether or not the sorting should be in reverse. The first spec in the list will be the primary sorting of the list of objects and the second spec will be the secondary sorting for when values for the first spec are equal. If reverse == False, then the ordering will be in non decreasing order and if reverse == True then the ordering will be in non-increasing order 
def multisort(input_list, specs):
    for key, reverse in reversed(specs): 
        input_list.sort(key = attrgetter(key), reverse = reverse) 
    return input_list

class filled_bin_list: 
    def __init__(self, filled_bins, cost):
        self.filled_bins = filled_bins
        self.cost = cost  
    def __repr__(self):
        return repr((self.filled_bins, self.cost))

def kt_dist(list1, list2):
    print(list1)
    print(list2)
    d = 0
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            if list2.index(list1[i]) > list2.index(list1[j]):
                d += 1
    return d

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        #print("high " , high)
        #print("low " , low)
        #print("mid ", mid)
        if (arr[low].remaining_volume >= x.volume or high == low):
            #print("1") 
            return arr[low]
        elif arr[mid].remaining_volume < x.volume:
            #print(mid)
            if arr[mid + 1].remaining_volume > x.volume:
                #print("2")
                return arr[mid + 1]
            else:
                return binary_search(arr, mid + 1, high, x)
        else:
            #print(mid)
            if arr[mid-1].remaining_volume < x.volume:
                #print("3")
                return arr[mid]
            else:
                return binary_search(arr, low, mid - 1, x)

def insort(arr, low, high, x):
    if high >= low:
        #print("high " , arr[high])
        #print("low " , arr[low])
        mid = (high + low) // 2
        #print("mid " , arr[mid])
        if arr[mid].remaining_volume == x.remaining_volume:
            if (high == low) or (arr[mid].cv_ratio <= x.cv_ratio and ((arr[mid + 1].remaining_volume > x.remaining_volume) or (arr[mid + 1].remaining_volume == x.remaining_volume and arr[mid + 1].cv_ratio >= x.cv_ratio))):
                return arr[:mid + 1] + [x] + arr[mid + 1:]
            elif arr[mid].cv_ratio < x.cv_ratio and (arr[mid+1].remaining_volume == x.remaining_volume and arr[mid+1].cv_ratio < x.cv_ratio):
                #print("1")
                return insort(arr, mid + 1, high, x)
            else:
                #print("2")
                return insort(arr, low, mid - 1, x)
        elif arr[mid].remaining_volume < x.remaining_volume:
            if (high == low) or arr[mid + 1].remaining_volume > x.remaining_volume:
                return arr[:mid + 1] + [x] + arr[mid + 1:]
            else:
                #print("3")
                return insort(arr, mid + 1, high, x)
        else:
            if high == low or arr[mid - 1].remaining_volume < x.remaining_volume:
                return arr[:mid] + [x] + arr[mid:]
            else:
                #print("4")
                return insort(arr, low, mid - 1, x)

def insort2(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid].remaining_volume == x.remaining_volume:
            if (high == low) or (arr[mid].cv_ratio <= x.cv_ratio and arr[mid + 1].cv_ratio >= x.cv_ratio):
                return arr[:mid + 1] + [x] + arr[mid + 1:]
            elif arr[mid].cv_ratio < x.cv_ratio and arr[mid + 1].cv_ratio < x.cv_ratio:
                return insort(arr, mid + 1, high, x)
            else:
                return insort(arr, low, mid - 1, x)
        elif arr[mid].remaining_volume < x.remaining_volume:
            if high == low or arr[mid + 1].remaining_volume > x.remaining_volume:
                return arr[:mid + 1] + [x] + arr[mid + 1:]
            else:
                return insort(arr, mid + 1, high, x)
        else:
            if high == low or arr[mid - 1].remaining_volume < x.remaining_volume:
                return arr[:mid] + [x] + arr[mid:]
            else:
                return insort(arr, low, mid - 1, x)

