#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 23:51:10 2021

@author: ademoguzhanozdemir
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter


def most_15_words(data):
    token_list = []
    for word in data.tolist():
        token_list += word.split(" ")
    frequencies=Counter(token_list)
    frequencies_sorted=sorted(frequencies.items(), key=lambda k: k[1],reverse=True)
    top_15=dict(frequencies_sorted[0:15])
    plt.rcdefaults()
    fig, ax = plt.subplots()
    
    
    ngram = top_15.keys()
    y_pos = np.arange(len(ngram))
    performance = top_15.values()
    
    
    ax.barh(y_pos, performance, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(ngram)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Counts')
    ax.set_title('Top-15 Most used word')
    
    # return plt
    # for word in data.tolist():
    #     print(type(word).)
