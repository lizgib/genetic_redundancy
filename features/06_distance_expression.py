import sys,os
import pandas as pd
import numpy as np
import random
import scipy
from scipy.stats.stats import pearsonr
from scipy import stats
#from scipy.stats import chisqprob
import math
'''
    input1: FC or FPKM matrix
    input2: Class of positive and negative gene pairs

'''

inp = open(sys.argv[1],'r').readlines()[1:] # guess im only gonna do the duplicate genes json_file from genome_data/

#added this bit 3/21 to make compatible w my gene pairs file
gene_pairs = []
for l in inp:
    ll = l.strip()
    gene_pairs.append(ll)
inp = gene_pairs
print(inp)

file = sys.argv[2]
out = open(sys.argv[3], 'w')
df = pd.read_csv(file, sep='\t', index_col = 0, header = 0)  ### the first column as index, which equals rownames in R, the first row as header
print(df.head())
#get title
title = 'Gene_pair\tDistanceAcrossAllExprs\n'
out.write(title)
#get values of matrix and calculate distanceq
rowname = df.index.tolist()
print(rowname)
x = 0
while x <= len(inp)-1:
    inl = inp[x]
    if inl.startswith("gene"):
        pass
    else:
       gene1 = inl.split('\t')[0].split('_')[0]
       gene2 = inl.split('\t')[0].split('_')[1]
       if gene1 in rowname and gene2 in rowname:
           res = inl.strip()
           tot_dist = 0
           for sam in df.columns[2:]:
               value1 = df.loc[gene1,sam]
               value2 = df.loc[gene2,sam]
               if value1 != 0 or value2 != 0:
                   distance = abs((value1-value2)**2)
                   if distance != 1 and distance != 0:
                       distance = distance.round(3)
                   else:
                       distance = 0
               tot_dist += distance
               tot_dist = tot_dist**0.5
           res += '\t%s'%tot_dist
           out.write(res + '\n')
        #    res += '\t%s'%tot_dis
        # out.write(res + '\n')

    x += 1

out.close()
