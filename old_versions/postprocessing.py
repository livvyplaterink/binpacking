#from binpacking import partition_1, quick_sort_1, partition_2, quick_sort_2, partition_3, quick_sort_3
from sorting import *
import random 

item_number_list = [100, 200, 300, 400, 500] 
item_number = random.choice(item_number_list)
#print(item_number)
item_volume = {}
for i in range(item_number): 
    item_volume["i" + str(i+1)] = random.randint(1, 20)
#print(item_volume)

bin_number = int(item_number / 2)
bin_volume = {}
bin_cost = {} 
for i in range(bin_number):
    bin_volume["b" + str(i+1)] = random.randint(20, 60) 
    bin_cost["b" + str(i+1)] = random.randint(1, 10) 
#print(bin_volume) 
#print(bin_cost)

#n = random.randint(0, 22) 
#print(n)



item_volume = {
        "i1" : 50, 
        "i2" : 60, 
        "i3" : 30,
        "i4" : 20,
        "i5" : 25, 
        "i6" : 10, 
        "i7" : 30, 
        "i8" : 50,
        "i9" : 14
        }
bin_volume = {
        "b1" : 130,
        "b2" : 80,
        "b3" : 100,
        "b4" : 120, 
        "b5" : 120, 
        "b6" : 80,
        "b7" : 100
        }
bin_cost = {
        "b1" : 3, 
        "b2" : 3, 
        "b3" : 3,
        "b4" : 3, 
        "b5" : 3, 
        "b6" : 3,
        "b7" : 3
        }

item_volume = { "i1" : 50, "i2" : 60, "i3" : 30, "i4" : 20, "i5" : 25, "i6" : 10, "i7" : 30, "i8" : 50, "i9" : 14}
bin_volume = {"b1" : 60, "b2" : 80, "b3" : 100, "b4" : 120, "b5" : 120, "b6" : 80, "b7" : 100}
bin_cost = {"b1" : 3, "b2" : 4, "b3" : 3, "b4" : 8, "b5" : 6, "b6" : 5.5, "b7" : 4}

ordered_items = [] 

for key in item_volume: 
    ordered_items.append(key)

item_sort(item_volume, ordered_items, 0, len(ordered_items)-1)
print(ordered_items)

cv_ratio = {}
ordered_bins = [] 

for key in bin_volume: 
    ordered_bins.append(key)
    cv_ratio[key] = bin_cost[key] / bin_volume[key]

bin_sort_cv(cv_ratio, bin_volume, ordered_bins, 0, len(ordered_bins) -1)
#print (bin_volume) 
#print (cv_ratio)
print (ordered_bins)


filled_bins = {
        "b4" : ["i1", "i2"],
        "b3" : ["i7", "i6"],
        "b5" : ["i3", "i4"],
        "b6" : ["i5", "i8"]
        } 
filled_bin_volume = {
        "b4" : 120,
        "b3" : 100,
        "b5" : 120,
        "b6" : 80
        } 
ordered_filled_bins = ["b4", "b3", "b5", "b6"]
for b in ordered_filled_bins: 
    for i in filled_bins[b]: 
        filled_bin_volume[b] -= item_volume[i]
print("filled bin volumes: " + str(filled_bin_volume))
print("bin volumes: " + str(bin_volume))
print("bin costs: " + str(bin_cost))
bin_sort_volume2(cv_ratio, filled_bin_volume, ordered_filled_bins, 0, len(ordered_filled_bins)-1)
print("ordered filled bins: " + str(ordered_filled_bins))


cost = 0
for b in filled_bins: 
    cost += bin_cost[b] 
print("original cost: " + str(cost))


unfilled_bins = []
for j in ordered_bins: 
    if j not in ordered_filled_bins: 
        unfilled_bins.append(j) 

print(unfilled_bins)
bin_sort_cost(bin_cost, bin_volume, unfilled_bins, 0, len(unfilled_bins) -1)
print(ordered_filled_bins)
print(unfilled_bins)

for n in range(len(ordered_filled_bins)): 
    print(n)
    b = ordered_filled_bins[n]
    print(b)
    v_b = 0
    for i in filled_bins[b]:
        v_b += item_volume[i]
    for k in unfilled_bins: 
        print("k: " + str(k) + " volume: " + str(bin_volume[k]))
        print( "bin: " + str(b) + " item volume: " + str(v_b))
        print( "k: " + str(k) + " bin cost: " + str(bin_cost[k]))
        print( "b: " + str(b) + " bin cost: " + str(bin_cost[b]))
        if (bin_volume[k] >= v_b) and (bin_cost[k] < bin_cost[b]):
            filled_bins[k] = filled_bins[b]
            filled_bin_volume[k] = bin_volume[k] - v_b
            del filled_bins[b]
            del filled_bin_volume[b]
            unfilled_bins.append(b)
            unfilled_bins.remove(k)
            print(filled_bins) 
            print(filled_bin_volume)
            ordered_filled_bins[n] = k 
            print(ordered_filled_bins) 
            bin_sort_cost(bin_cost, bin_volume, unfilled_bins, 0, len(unfilled_bins) -1)
            print(unfilled_bins)
            break

print(filled_bins)
print(filled_bin_volume)
print(ordered_filled_bins)
cost = 0
for b in filled_bins:
    cost += bin_cost[b]
print("final cost: " + str(cost))

for n in range(len(ordered_filled_bins)):
    print(n)
    b = ordered_filled_bins[n]
    print(b)
    v_b = 0
    for i in filled_bins[b]:
        v_b += item_volume[i]
    for k in unfilled_bins:
        print("k: " + str(k) + " volume: " + str(bin_volume[k]))
        print( "bin: " + str(b) + " item volume: " + str(v_b))
        print( "k: " + str(k) + " bin cost: " + str(bin_cost[k]))
        print( "b: " + str(b) + " bin cost: " + str(bin_cost[b]))
        if (bin_volume[k] >= v_b) and (bin_cost[k] < bin_cost[b]):
            filled_bins[k] = filled_bins[b]
            filled_bin_volume[k] = bin_volume[k] - v_b
            del filled_bins[b]
            del filled_bin_volume[b]
            unfilled_bins.append(b)
            unfilled_bins.remove(k)
            print(filled_bins)
            print(filled_bin_volume)
            ordered_filled_bins[n] = k
            print(ordered_filled_bins)
            bin_sort_cost(bin_cost, bin_volume, unfilled_bins, 0, len(unfilled_bins) -1)
            print(unfilled_bins) 
            break

print(filled_bins)
print(filled_bin_volume)
print(ordered_filled_bins)
cost = 0
for b in filled_bins:
    cost += bin_cost[b]
print("final cost: " + str(cost))

for i in item_volume:
    for b in ordered_filled_bins:
        if i in filled_bins[b]:
            break
        if b == ordered_filled_bins[len(ordered_filled_bins)-1]:
            if i not in filled_bins[b]:
                print(i)

print(cv_ratio)

item_sort(item_volume, ordered_items, 0, len(ordered_items)-1)
print(ordered_items)
bin_sort_cv(cv_ratio, bin_volume, ordered_bins, 0, len(ordered_bins)-1)
print(ordered_bins)
bin_sort_volume(cv_ratio, bin_volume, ordered_bins, 0, len(ordered_bins)-1)
print(ordered_bins)
bin_sort_cost(bin_cost, bin_volume, ordered_bins, 0, len(ordered_bins)-1)
print(ordered_bins)
bin_sort_cost2(bin_cost, bin_volume, ordered_bins, 0, len(ordered_bins) -1)
print(ordered_bins)
