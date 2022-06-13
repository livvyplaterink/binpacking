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
