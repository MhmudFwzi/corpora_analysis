import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns

import sys
import excel_data

try:
    data = sys.argv[1]
    data = excel_data.__dict__[data]
    print(data)
except:
    print("Data Not Found")
    exit()

def shiftedColorMap(cmap, start=0, midpoint=0.5, stop=1.0, name='shiftedcmap'):
    cdict = {
        'red': [],
        'green': [],
        'blue': [],
        'alpha': []
    }
    reg_index = np.linspace(start, stop, 257)
    shift_index = np.hstack([
        np.linspace(0.0, midpoint, 128, endpoint=False), 
        np.linspace(midpoint, 1.0, 129, endpoint=True)
    ])
    for ri, si in zip(reg_index, shift_index):
        r, g, b, a = cmap(ri)

        cdict['red'].append((si, r, r))
        cdict['green'].append((si, g, g))
        cdict['blue'].append((si, b, b))
        cdict['alpha'].append((si, a, a))

    newcmap = matplotlib.colors.LinearSegmentedColormap(name, cdict)
    plt.register_cmap(cmap=newcmap)
    return newcmap
    
#chosen_cmap = sns.diverging_palette(145, 300, as_cmap=True)
chosen_cmap = sns.color_palette("coolwarm", as_cmap=True)
shifted_cmap = shiftedColorMap(chosen_cmap, start= 0, midpoint = 0.05, stop = 1)

df = pd.DataFrame(data, index=["1850","1800","1750","1700"])
sns_object = sns.heatmap(df, cmap=shifted_cmap, vmax=1, vmin=0)
# plt.title(sys.argv[1])
figure = sns_object.get_figure()
figure.savefig(sys.argv[1] + ".png")
