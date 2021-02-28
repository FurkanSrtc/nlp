#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 23:51:10 2021

@author: ademoguzhanozdemir
"""

import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def most_words(data, head_txt: str, most_count = 15):
    token_list = []
    for word in data.tolist():
        token_list += [_word for _word in word.split(" ") if _word]
    token_list = [token for token in token_list if token_list]
    frequencies = Counter(token_list)
    frequencies_sorted = sorted(frequencies.items(), key=lambda k: k[1],
                                reverse=True)
    top_15 = dict(frequencies_sorted[:most_count])
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
    ax.set_title(f'{head_txt} Top-{most_count} Most used word')

    # return plt
    # for word in data.tolist():
    #     print(type(word).)
