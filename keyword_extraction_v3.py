"""
Created on Mon Mar 20 11:41:40 2017

@author: ZNevzz
"""

import pandas as pd
from collections import defaultdict


# read file
filenames=['labeled.csv','company_keyword.xlsx']
df = pd.read_csv(filenames[0])

print(df.describ(),df.head())


