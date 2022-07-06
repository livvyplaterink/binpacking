import numpy as np
import matplotlib.pyplot as plt
from sorting_objects import *
from item_bin import *
from itertools import accumulate
from binpacking_result import *
import matplotlib.cm as cm 

filled_bins2 = []

#putting bins in order of name 
for i in range(len(filled_bins)): 
    for b in filled_bins: 
        if b.name == 'b'+str(i+1): 
            filled_bins2.append(b)

#defining function that creates a stacked bar chart of bins and items 
def filled_bin_chart(filled_bins, bin_objects): 
    labels = []
    for b in filled_bins:
        labels.append(b.name)
    
    #getting the max number of items contained in any bin 
    len_items_contained = []
    for b in filled_bins:
        len_items_contained.append(len(b.items_contained)) 

    #category names are just the order in which an item is placed into a bin 
    category_names = []
    for l in range(max(len_items_contained)): 
        category_names.append(str(l+1))

    #creating dictionaries that hold items and item volumes contained in each bin and a list that holds the total bin volume 
    results = {} 
    result_items = {}
    total_volume = []
    for b in filled_bins: 
        results[b.name] = []
        result_items[b.name] = []
        total_volume.append(b.volume)
        for i in b.items_contained: 
            results[b.name].append(i.volume) 
            result_items[b.name].append(i.name)
    
    #adding zeros so that each list of items is the same length  
    for b in results: 
        while len(results[b]) < max(len_items_contained):
            results[b].append(0)
            result_items[b].append(" ")
    
    #creating lists of items in bins by index (for labelling purposes) 
    result_items_2 = []
    for k in range(max(len_items_contained)): 
        result_items_2.append([]) 
    for b in result_items: 
        for i in range(len(result_items[b])):
            result_items_2[i].append(result_items[b][i])

    #converting dictionary lists to arrays 
    data = np.array(list(results.values()), list)
    data_cum = data.cumsum(axis = 1)  

    #assigning colors to the items 
    category_colors = plt.colormaps['binary'](
        np.linspace(0.1, 0.15, data.shape[1]))
    #print(category_colors)

    #assigning colors to the bins based on cost 
    b_cost = [] 
    for b in filled_bins: 
        b_cost.append(b.cost) 
    cmap = cm.get_cmap('RdYlGn')
    bin_color = []
    for i in range(len(b_cost)): 
        bin_color.append(plt.colormaps['RdYlGn'](1-((b_cost[i]-min(b_cost)) / (max(b_cost)-min(b_cost)))))
    bin_color = np.array(bin_color) 
    #print(bin_color)

    #creating the plot
    fig, ax = plt.subplots(figsize=(18, 7))
    ax.yaxis.set_visible(False)
    ax.set_ylim(0, max(total_volume))
    ax.bar(labels, total_volume, width = 0.75, color = bin_color, edgecolor = bin_color, linewidth = 0.4)
    xticks = np.arange(len(labels))
    ax.set_xticks(xticks, labels, fontsize = 'xx-small', rotation = 'vertical')

    #plotting the bins and items as a stacked bar chart 
    for i, (colname, color, l) in enumerate(zip(category_names, category_colors, result_items_2)):
        heights = data[:, i]
        starts = data_cum[:, i] - heights
        rects = ax.bar(labels, heights, bottom=starts, width=0.75, label=colname, color=color)

        r, g, b, _ = color
        text_color = 'dimgray'
        ax.bar_label(rects, labels = l, label_type='center', color=text_color, fontsize = 'xx-small')
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')
    return fig, ax


filled_bin_chart(filled_bins2, bin_objects)
plt.show()
