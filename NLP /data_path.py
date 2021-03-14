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


migros_path = "data/Migros/"
migros_raw_product_1 = pd.read_csv(fr"{migros_path}products1Yeni.csv",
                                   sep=sep, encoding=encoding)
migros_raw_product_2 = pd.read_csv(fr"{migros_path}products2Yeni.csv",
                                   sep=sep, encoding=encoding)
migros_raw_product_3 = pd.read_csv(fr"{migros_path}products3Yeni.csv",
                                   sep=sep, encoding=encoding)
migros_raw_product_4 = pd.read_csv(fr"{migros_path}products4Yeni.csv",
                                   sep=sep, encoding=encoding)

__frames = [migros_raw_product_1, migros_raw_product_2,
            migros_raw_product_3, migros_raw_product_4]
migros_raw_products = shuffle(pd.concat(__frames))


cagri_path = "data/CagriMarket/"
cagri_raw_procut_1 = pd.read_csv(fr"{cagri_path}BebekUrunleri.csv",
                                 encoding=encoding)
cagri_raw_procut_2 = pd.read_csv(fr"{cagri_path}DeterjanVeTemizlik.csv",
                                 encoding=encoding)
cagri_raw_procut_3 = pd.read_csv(fr"{cagri_path}EtTavukHindi.csv",
                                 encoding=encoding)
cagri_raw_procut_4 = pd.read_csv(fr"{cagri_path}EvVeYasamUrunleri.csv",
                                 encoding=encoding)
cagri_raw_procut_5 = pd.read_csv(fr"{cagri_path}GidaSekerleme.csv",
                                 encoding=encoding)
cagri_raw_procut_6 = pd.read_csv(fr"{cagri_path}KagitUrunleri.csv",
                                 encoding=encoding)
cagri_raw_procut_7 = pd.read_csv(fr"{cagri_path}KisiselBakimVeKozmetik.csv",
                                 encoding=encoding)
cagri_raw_procut_8 = pd.read_csv(fr"{cagri_path}MeyveSebze.csv",
                                 encoding=encoding)
cagri_raw_procut_9 = pd.read_csv(fr"{cagri_path}PetShopUrunleri.csv",
                                 encoding=encoding)
cagri_raw_procut_10 = pd.read_csv(fr"{cagri_path}SutveKahvalti.csv",
                                  encoding=encoding)
cagri_raw_procut_11 = pd.read_csv(fr"{cagri_path}icecekler.csv",
                                  encoding=encoding)

__frames = [cagri_raw_procut_1, cagri_raw_procut_2, cagri_raw_procut_3,
            cagri_raw_procut_4, cagri_raw_procut_5, cagri_raw_procut_6,
            cagri_raw_procut_7, cagri_raw_procut_8, cagri_raw_procut_9,
            cagri_raw_procut_10, cagri_raw_procut_11]

cagri_raw_products = shuffle(pd.concat(__frames))
