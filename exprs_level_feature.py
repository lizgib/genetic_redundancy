'''
processing expression level data feature for 
yeast fitness prediction 
'''

import sys
import pandas as pd
import re

df = pd.read_csv(sys.argv[1], sep = '\t')
pubmed_ID1 = '17163986' # DNA damage from antibiotic treatment
pubmed_ID2 = '12875747' # aging in yeast
pubmed_ID3 = '11102521' # cayla abiotic stress
pubmed_ID4 = '11179418' # cayla abiotic stress 
pubmed_ID5 = '18281432' # hakim growth metabolism 
pubmed_ID6 = '18422925' # hakim growth metabolism 
newdf = pd.DataFrame()
header_list = list(df.columns.values)
genes =pd.DataFrame(df['gene'])

frames = []
col = pd.DataFrame(genes)
frames.append(col)
for i in header_list:
    if pubmed_ID1 in i: # enter the specific pubmed IDs you want to look at here 
        col = pd.DataFrame(df[i])
        frames.append(col)
    if pubmed_ID2 in i:
        col = pd.DataFrame(df[i])
        frames.append(col)
    if pubmed_ID3 in i:
        col = pd.DataFrame(df[i])
        frames.append(col)
    if pubmed_ID4 in i:
        col = pd.DataFrame(df[i])
        frames.append(col)
    if pubmed_ID5 in i:
        col = pd.DataFrame(df[i])
        frames.append(col)
    if pubmed_ID6 in i:
        col = pd.DataFrame(df[i])
        frames.append(col)

newdf = pd.concat(frames, axis = 1)
new_header = []
for i in list(newdf.columns.values):
    new = re.sub('\W', '_', i)
    new_header.append(new)
    
newdf.columns = new_header
newdf = newdf.set_index('gene')
newdf.to_csv('final_combined_exprs_level.tsv', sep = '\t')


