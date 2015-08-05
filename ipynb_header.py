from __future__ import print_function
from collections import defaultdict
import datetime
import json
import math
from operator import itemgetter
import os
import time

import brewer2mpl
from IPython.display import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import scipy.stats
import sklearn


dd_colors = ["#3399cc", "#927fb9", "#edbe01", "#81c0df", "#ab8fc7", "#ffd528",
             "#99cce5", "#3399cc", "#bba4d1", "#927fb9", "#ffeda3", "#ffcc00",
             "#e0f3db", "#ccebc5", "#a8ddb5", "#7bccc4", "#4eb3d3", "#2b8cbe",
             "#0868ac", "#084081",
             "#ffeda0", "#fed976", "#feb24c", "#fd8d3c", "#fc4e2a", "#e31a1c",
             "#bd0026", "#800026",
             "#efedf5", "#dadaeb", "#bcbddc", "#9e9ac8", "#807dba", "#6a51a3",
             "#54278f", "#3f007d",
             "#deebf7", "#c6dbef", "#9ecae1", "#6baed6", "#4292c6", "#2171b5",
             "#08519c", "#08306b",
             "#e5f5e0", "#c7e9c0", "#a1d99b", "#74c476", "#41ab5d", "#238b45",
             "#006d2c", "#00441b",
             "#fee6ce", "#fdd0a2", "#fdae6b", "#fd8d3c", "#f16913", "#d94801",
             "#a63603", "#7f2704",
             "#fee0d2", "#fcbba1", "#fc9272", "#fb6a4a", "#ef3b2c", "#cb181d",
             "#a50f15", "#67000d",
             "#f0f0f0", "#d9d9d9", "#bdbdbd", "#969696", "#737373", "#525252",
             "#252525", "#000000", ]
set312 = brewer2mpl.get_map('Set3', 'Qualitative', 12)
set28 = brewer2mpl.get_map('Set2', 'Qualitative', 8)
set19 = brewer2mpl.get_map('Set1', 'Qualitative', 9)
brewer_colors = list(set28.mpl_colors + set19.mpl_colors + set312.mpl_colors)
# colors = brewer_colors
colors = dd_colors
font = {'family': 'Bitstream Vera Sans',
        'weight': 'bold',
        'size': 14}


def show_brewer_colors():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i, color in enumerate(brewer_colors):
        ax.add_patch(mpl.patches.Rectangle((i, 0), 1, 1,
                                           color=brewer_colors[i]))
    fig.set_size_inches(14, 1)
    ax.set_yticklabels([])
    plt.xlim([0, len(brewer_colors)])
    plt.show()


def show_dd_colors(start, finish):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i, color in enumerate(dd_colors[start:finish]):
        ax.add_patch(mpl.patches.Rectangle((start+i, 0), 1, 1,
                                           color=dd_colors[start+i]))
    ax.set_yticklabels([])
    plt.xlim([start, finish])
    fig.set_size_inches(14, 1)
    plt.show()


def show_colors():
    show_brewer_colors()
    show_dd_colors(0, len(dd_colors)/2)
    show_dd_colors(len(dd_colors)/2, len(dd_colors))

modern_pandas = True

if(modern_pandas):
    pd.set_option('display.max_columns', 15)
    pd.set_option('display.width', 400)
    pd.set_option('display.mpl_style', 'default')

plt.style.use('ggplot')

mpl.rcParams['axes.color_cycle'] = colors
mpl.rcParams['figure.figsize'] = (14, 7)
mpl.rc('font', **font)
