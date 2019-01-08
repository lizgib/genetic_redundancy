'''
making a pretty fitness table 
# first generated a table for the class 
cols: 
    gene    SMF fitness(average between array and query)    variance
# next I need to modify this for the project 
cols: 
    gene1   SMF1    variance1   gene2   SMF2    variance2   DMF 

# get gene 1 and 2 by sorting each pair and only counting them once (so the query and 
array are reciprocal)

doing this for the 26 dataset and the 30 

11/11/18
'''

import pandas as pd
import numpy as np
import sys
from math import isnan

f = open(sys.argv[1]) # files will be in /mnt/research/ShiuLab/20_Yeast_Redundancy/00_Raw_Data/
filename = sys.argv[2] # for saving the file, which dataset was it 

# read the file 
header = f.readline()
lines = f.readlines()

# get all the genes and make them dictionary keys 
gene_fitness = {}
all_genes = set()
for l in lines:
    ll = l.strip().split(',')
    query_gene = ll[1]
    array_gene = ll[3]    
    query_gene = query_gene.split('_')[0]
    array_gene = array_gene.split('_')[0]
    all_genes.add(query_gene)
    all_genes.add(array_gene)

all_genes = sorted(all_genes)
for g in all_genes:
    gene_fitness[g] = []


for l in lines:
    ll = l.strip().split(',')
    query_gene = ll[1]
    array_gene = ll[3]    
    query_gene = query_gene.split('_')[0]
    array_gene = array_gene.split('_')[0]
    query_SMF = ll[8]
    array_SMF = ll[9]
    try:
        query_SMF = float(query_SMF)
    except ValueError:
        query_SMF = 'NA'
    try:
        array_SMF = float(array_SMF)
    except ValueError:
        array_SMF = 'NA'
    if query_gene in gene_fitness.keys():
        if query_SMF != 'NA':
            gene_fitness[query_gene].append(query_SMF)
    if array_gene in gene_fitness.keys():
        if array_SMF != 'NA':
            gene_fitness[array_gene].append(array_SMF)

# next we gonna calculate the mean and variance
gene_values = {}
for g in gene_fitness.keys():
    if g not in gene_values.keys():
        gene_values[g] = []
    fitness_np = np.asarray(gene_fitness[g])
    try:
        mean_fit = np.mean(fitness_np)
    except:
        mean_fit = 'NA'
    try:
        var_fit = np.var(fitness_np)
    except:
        var_fit = 0.0
    gene_values[g].append(mean_fit)
    gene_values[g].append(var_fit)

clean_dict = {k: gene_values[k] for k in gene_values if not isnan(gene_values[k][0])}
df = pd.DataFrame.from_dict(data=clean_dict, orient='index')
df.columns = ['SMF', 'Variance']
df.to_csv(('../data/fitness_data/clean/clean_redundancy_matrix%s.csv' %filename), header=True, sep = ',')
f.close()

# OK! 12/5 this looks good for sure (havent checked with any one esle but it looks like
# averaage aand variance are being computed correctly and the NAs are being dropped)


