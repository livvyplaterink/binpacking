import numpy as np
import matplotlib.pyplot as plt
from sorting_objects import *
from item_bin import *
from itertools import accumulate


#filled_bins = [bins('b14', 631, 3, 57, 0.09033280507131537, [items('i4', 410), items('i3', 218)]), bins('b9', 501, 7, 64, 0.1277445109780439, [items('i1', 494)]), bins('b16', 470, 7, 61, 0.12978723404255318, [items('i2', 463)]), bins('b15', 482, 8, 52, 0.1078838174273859, [items('i10', 474)]), bins('b2', 670, 11, 51, 0.07611940298507462, [items('i13', 309), items('i8', 350)]), bins('b24', 623, 45, 77, 0.12359550561797752, [items('i11', 376), items('i12', 202)]), bins('b20', 518, 67, 58, 0.11196911196911197, [items('i5', 451)]), bins('b4', 562, 106, 73, 0.1298932384341637, [items('i7', 456)]), bins('b7', 517, 108, 59, 0.11411992263056092, [items('i6', 409)]), bins('b11', 603, 114, 60, 0.09950248756218906, [items('i9', 489)])]

filled_bins = [bins('b27', 588, 1, 51, 0.08673469387755102, [items('i10', 364), items('i8', 223), ]), bins('b23', 667, 6, 62, 0.09295352323838081, [items('i17', 407), items('i4', 254), ]), bins('b22', 660, 8, 63, 0.09545454545454546, [items('i6', 414), items('i15', 238), ]), bins('b7', 678, 32, 73, 0.10766961651917405, [items('i7', 351), items('i21', 295), ]), bins('b16', 623, 52, 64, 0.10272873194221509, [items('i19', 297), items('i9', 274), ]), bins('b41', 464, 62, 52, 0.11206896551724138, [items('i27', 402), ]), bins('b47', 634, 65, 65, 0.10252365930599369, [items('i23', 318), items('i20', 251), ]), bins('b33', 561, 67, 53, 0.0944741532976827, [items('i14', 494), ]), bins('b43', 597, 88, 61, 0.10217755443886097, [items('i5', 263), items('i3', 246), ]), bins('b17', 534, 51, 71, 0.13295880149812733, [items('i1', 483), ]), bins('b30', 550, 100, 54, 0.09818181818181818, [items('i24', 450), ]), bins('b18', 458, 5, 66, 0.14410480349344978, [items('i16', 453), ]), bins('b54', 580, 101, 72, 0.12413793103448276, [items('i22', 479), ]), bins('b6', 619, 147, 73, 0.11793214862681745, [items('i2', 472), ]), bins('b53', 363, 15, 54, 0.1487603305785124, [items('i26', 348), ]), bins('b4', 671, 156, 55, 0.08196721311475409, [items('i12', 235), items('i11', 280), ]), bins('b35', 502, 8, 55, 0.10956175298804781, [items('i13', 494), ]), bins('b50', 586, 92, 73, 0.12457337883959044, [items('i18', 494), ]), bins('b40', 664, 187, 55, 0.08283132530120482, [items('i25', 477), ]), bins('b39', 621, 621, 79, 0.12721417069243157, []), bins('b26', 675, 675, 86, 0.1274074074074074, []), bins('b46', 661, 661, 85, 0.12859304084720122, []), bins('b20', 571, 571, 74, 0.1295971978984238, []), bins('b24', 635, 635, 83, 0.13070866141732285, []), bins('b31', 687, 687, 90, 0.13100436681222707, []), bins('b48', 562, 562, 74, 0.13167259786476868, []), bins('b3', 607, 607, 81, 0.13344316309719934, []), bins('b9', 689, 689, 92, 0.13352685050798258, []), bins('b5', 695, 695, 93, 0.13381294964028778, []), bins('b14', 598, 598, 81, 0.1354515050167224, []), bins('b25', 673, 673, 94, 0.13967310549777118, []), bins('b2', 581, 581, 84, 0.14457831325301204, []), bins('b15', 388, 388, 57, 0.14690721649484537, []), bins('b19', 465, 465, 69, 0.14838709677419354, []), bins('b1', 345, 345, 54, 0.1565217391304348, []), bins('b42', 394, 394, 62, 0.15736040609137056, []), bins('b32', 368, 368, 58, 0.15760869565217392, []), bins('b34', 480, 480, 82, 0.17083333333333334, []), bins('b37', 311, 311, 55, 0.17684887459807075, []), bins('b12', 428, 428, 80, 0.18691588785046728, []), bins('b21', 507, 507, 99, 0.1952662721893491, []), bins('b49', 293, 293, 63, 0.2150170648464164, []), bins('b38', 303, 303, 67, 0.22112211221122113, []), bins('b52', 259, 259, 58, 0.22393822393822393, []), bins('b45', 262, 262, 62, 0.2366412213740458, []), bins('b36', 382, 382, 91, 0.23821989528795812, []), bins('b8', 385, 385, 92, 0.23896103896103896, []), bins('b29', 347, 347, 88, 0.25360230547550433, []), bins('b11', 319, 319, 81, 0.25391849529780564, []), bins('b13', 291, 291, 82, 0.281786941580756, []), bins('b44', 268, 268, 84, 0.31343283582089554, []), bins('b51', 216, 216, 73, 0.33796296296296297, []), bins('b28', 215, 215, 80, 0.37209302325581395, []), bins('b10', 217, 217, 84, 0.3870967741935484, []), ]


category_names = ["1", "2", "3"]

filled_bins2 = []

for i in range(len(filled_bins)): 
    for b in filled_bins: 
        if b.name == 'b'+str(i+1): 
            filled_bins2.append(b)
print(filled_bins2)

def filled_bin_chart(filled_bins, bin_objects): 
    labels = []
    for b in filled_bins:
        labels.append(b.name)
    print(labels) 
    
    len_items_contained = []
    for b in filled_bins:
        len_items_contained.append(len(b.items_contained)) 
    print(len_items_contained)

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
    
    for b in results: 
        while len(results[b]) < max(len_items_contained):
            results[b].append(0)
            result_items[b].append(" ")
    print(results) 
    print(result_items)
    
    result_items_2 = []
    for k in range(max(len_items_contained)): 
        result_items_2.append([]) 
    for b in result_items: 
        for i in range(len(result_items[b])):
            result_items_2[i].append(result_items[b][i])
    print("!!!!!!!!!" + str(result_items_2))

    data = np.array(list(results.values()), list)
    data_cum = data.cumsum(axis = 1)  
    category_colors = plt.colormaps['RdYlGn'](
        np.linspace(0.15, 0.85, data.shape[1]))
    fig, ax = plt.subplots(figsize=(16, 7))
    ax.yaxis.set_visible(False)
    ax.set_ylim(0, max(total_volume))
    ax.bar(labels, total_volume, width = 0.75, color = 'white', edgecolor = 'black', linewidth = 0.4)
    xticks = np.arange(len(labels))
    ax.set_xticks(xticks, labels, fontsize = 'x-small')

    for i, (colname, color, l) in enumerate(zip(category_names, category_colors, result_items_2)):
        heights = data[:, i]
        #print(heights)
        starts = data_cum[:, i] - heights
        #print(starts)
        rects = ax.bar(labels, heights, bottom=starts, width=0.75, label=colname, color=color)

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        print(l)
        ax.bar_label(rects, labels = l, label_type='center', color=text_color, fontsize = 'xx-small')
        #ax.bar_label(rects, labels = result_items[l], label_type='center', color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')
    return fig, ax


filled_bin_chart(filled_bins2, bin_objects)
plt.show()
