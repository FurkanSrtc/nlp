#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 22:45:08 2021

@author: ademoguzhanozdemir
"""

import pandas as pd
from sklearn.utils import shuffle

encoding = "utf-8"
sep = ";"
path = "data/Migros/"

migros_raw_product_1 = pd.read_csv(fr"{path}products1Yeni.csv", sep=sep,
                                  encoding=encoding)
migros_raw_product_2 = pd.read_csv(fr"{path}products2Yeni.csv", sep=sep,
                                  encoding=encoding)
migros_raw_product_3 = pd.read_csv(fr"{path}products3Yeni.csv", sep=sep,
                                  encoding=encoding)
migros_raw_product_4 = pd.read_csv(fr"{path}products4Yeni.csv", sep=sep,
                                  encoding=encoding)

__frames = [migros_raw_product_1, migros_raw_product_2,
            migros_raw_product_3, migros_raw_product_4]
migros_raw_products = shuffle(pd.concat(__frames))

