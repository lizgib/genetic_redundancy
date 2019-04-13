'''
only the duplicate genes in the expression dataframe
'''

import sys, os
import pandas as pd
import datetime

#dup = open('data/genome_data/e10_dup_genes')
dup = open(sys.argv[1])
lines = dup.readlines()

dup_genes = set()
for l in lines:
    l = l.strip().split('_')
    dup_genes.add(l[0])
    dup_genes.add(l[1])
print(len(dup_genes))

#exprs = pd.read_csv('data/exprs_data/exprs_dat_04-02-2019.tab', sep = '\t', header = 0)
exprs = pd.read_csv(sys.argv[2], sep = '\t', header = 0)
newdf = exprs[exprs['gene'].isin(dup_genes)]
print(len(newdf.index))

d = datetime.datetime.today()
date = d.strftime('%m-%d-%Y')
newdf.to_csv(('data/exprs_data/exprs_dat_dup_genes%s.tab' %date), header=False, sep = '\t')
