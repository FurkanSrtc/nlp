#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 22:45:08 2021

@author: ademoguzhanozdemir
"""

import pandas as pd

raw_prodcuts1 = pd.read_csv(r"/content/drive/MyDrive/Veri/Migros/products1Yeni.csv", encoding="utf-8", sep =";")
raw_prodcuts2 = pd.read_csv(r"/content/drive/MyDrive/Veri/Migros/products2Yeni.csv", encoding="utf-8", sep =";")
raw_prodcuts3 = pd.read_csv(r"/content/drive/MyDrive/Veri/Migros/products3Yeni.csv", encoding="utf-8", sep =";")
raw_prodcuts4 = pd.read_csv(r"/content/drive/MyDrive/Veri/Migros/products4Yeni.csv", encoding="utf-8", sep =";")

raw_prodcuts5 = pd.read_csv(r"/content/drive/MyDrive/Veri/CagriMarket/csv_veri/BebekUrunleri.csv", encoding="utf-8")
raw_prodcuts6 = pd.read_csv(r"/content/drive/MyDrive/Veri/CagriMarket/csv_veri/DeterjanVeTemizlik.csv", encoding="utf-8")
raw_prodcuts7 = pd.read_csv(r"/content/drive/MyDrive/Veri/CagriMarket/csv_veri/EtTavukHindi.csv", encoding="utf-8")
raw_prodcuts8 = pd.read_csv(r"/content/drive/MyDrive/Veri/CagriMarket/csv_veri/EvVeYasamUrunleri.csv", encoding="utf-8")
raw_prodcuts9 = pd.read_csv(r"/content/drive/MyDrive/Veri/CagriMarket/csv_veri/GidaSekerleme.csv", encoding="utf-8")
raw_prodcuts10 = pd.read_csv(r"/content/drive/MyDrive/Veri/CagriMarket/csv_veri/KagitUrunleri.csv", encoding="utf-8")
raw_prodcuts11 = pd.read_csv(r"/content/drive/MyDrive/Veri/CagriMarket/csv_veri/KisiselBakimVeKozmetik.csv", encoding="utf-8")
raw_prodcuts12 = pd.read_csv(r"/content/drive/MyDrive/Veri/CagriMarket/csv_veri/MeyveSebze.csv", encoding="utf-8")
raw_prodcuts13 = pd.read_csv(r"/content/drive/MyDrive/Veri/CagriMarket/csv_veri/PetShopUrunleri.csv", encoding="utf-8")
raw_prodcuts14 = pd.read_csv(r"/content/drive/MyDrive/Veri/CagriMarket/csv_veri/SutveKahvalti.csv", encoding="utf-8")
raw_prodcuts15 = pd.read_csv(r"/content/drive/MyDrive/Veri/CagriMarket/csv_veri/icecekler.csv", encoding="utf-8")