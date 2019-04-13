'''
grab only the duplicate genes
this script will work for both the expression data and the fitness data
4/12/19
'''

import sys, os
import pandas as pd

df = pd.read_csv(sys.argv[1], sep = '\t') # file with all gene pairs
dup = pd.read_csv(sys.argv[2], sep = '\t', header = None, index_col = False, squeeze = True) # duplicate gene pair file
print(df.index)
newdf = df.loc[dup]
newdf.to_csv(sys.argv[3], sep = '\t')
