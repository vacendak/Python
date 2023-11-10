#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 23:04:28 2023

@author: Sergio Sanz
"""

from math import factorial
from datetime import date
import time
import random
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Polynomial as P
from scipy.stats import norm

URL = 'https://docs.google.com/spreadsheets/d/e/' \
      '2PACX-1vRy91wfK2JteoMi1ZOhGm0D1RKJfDTbEOj6rfnrB6' \
      '-X7n2Q1nfFwBZBpcivHRdg3pSwxSQgLA3KpW7v/pub?output=csv'

# Crear Data Frame
df = pd.read_csv(URL)


# Eliminar columna sin datos
df = df.drop('Unnamed: 6', axis=1)

# Cambiar nombres de las columnas
new_names = ['FECHA', 'N1', 'N2', 'N3', 'N4', 'N5', 'E1', 'E2']
df.columns = new_names
inv_df = df.iloc[::-1].reset_index(drop=True)
inv_df_nofecha = inv_df.drop(['FECHA'], axis=1)

# Eliminar las columnas de estrellas
dfnums = df.drop(['FECHA', 'E1', 'E2'], axis=1)
inv_dfnums = dfnums.iloc[::-1].reset_index(drop=True)

# Eliminar las columnas de números
dfestr = df.drop(['FECHA', 'N1', 'N2', 'N3', 'N4', 'N5'], axis=1)
inv_dfestr = dfestr.iloc[::-1].reset_index(drop=True)
print(inv_df)
