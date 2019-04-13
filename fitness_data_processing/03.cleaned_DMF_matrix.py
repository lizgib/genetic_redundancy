
import pandas as pd
import numpy as np
import sys

# go through the file and make a query {gene : SMF} dictionary

# also make an array {gene : SMF} dictionary

# merge these two dictionaries so for each gene in the dataset you have a full
# view of the SMF values
# ^^^ or alternatively to this couldn't I just read in the dataset that I made in the other
#     clean_matrix script?

f = open(sys.argv[1]) # files will be in /mnt/research/ShiuLab/20_Yeast_Redundancy/00_Raw_Data/
SMF_dict = pd.read_csv(sys.argv[2], sep = '\t', header = None) # this should be the clean_SMF_matrix.tab
filename = sys.argv[3]

SMF_dict = SMF_dict.set_index(0).T.to_dict(orient = 'list')

# then iterate through the file looking at each gene pair
# sort the gene pairs by which is greater first (ignore query and array)
# just alphabetize them
# this should give you two rows for each pair (the reciprocals)

# read the file
header = f.readline()
lines = f.readlines()


df = {}
DMF_dict = {}

for l in lines:
    ll = l.strip().split(',')
    query_gene = ll[1].split('_')[0]
    array_gene = ll[3].split('_')[0]
    query_SMF = ll[8]
    array_SMF = ll[9]
    DMF = ll[10]
    if query_gene < array_gene:
        gene1 = query_gene
        gene2 = array_gene
    else:
        gene1 = array_gene
        gene2 = query_gene
    try:
        SMF1 = SMF_dict[gene1]
        SMF2 = SMF_dict[gene2]
    except:
        pass

    pair = gene1 + '_' + gene2
    if pair not in DMF_dict.keys():
        DMF_dict[pair] = []
    DMF_dict[pair].append(float(DMF))


for l in lines:
    ll = l.strip().split(',')
    query_gene = ll[1].split('_')[0]
    array_gene = ll[3].split('_')[0]
    query_SMF = ll[8]
    array_SMF = ll[9]
    DMF = ll[10]
#    pair = set(query_gene, array_gene)
    if query_gene < array_gene:
        gene1 = query_gene
        gene2 = array_gene
    else:
        gene1 = array_gene
        gene2 = query_gene
    try:
        SMF1 = SMF_dict[gene1]
        SMF2 = SMF_dict[gene2]
    except:
        pass

    pair = gene1 + '_' + gene2
    if pair not in df.keys():
        df[pair] = []
    df[pair].append(gene1)
    df[pair].append(SMF1[0])
    df[pair].append(SMF1[1])
    df[pair].append(gene2)
    df[pair].append(SMF2[0])
    df[pair].append(SMF2[1])
    df[pair].append(DMF)
    df[pair].append(np.mean(DMF_dict[pair]))
    df[pair].append(len(DMF_dict[pair]))


outfile = open(filename, 'w')
outfile.write('Pair')
outfile.write('\t')
outfile.write('Gene1')
outfile.write('\t')
outfile.write('SMF1')
outfile.write('\t')
outfile.write('SMFvar1')
outfile.write('\t')
outfile.write('Gene2')
outfile.write('\t')
outfile.write('SMF2')
outfile.write('\t')
outfile.write('SMFvar2')
outfile.write('\t')
outfile.write('DMF')
outfile.write('\t')
outfile.write('DMFmean')
outfile.write('\t')
outfile.write('NumDMFs_averaged')
outfile.write('\n')


for p in df.keys():
    gene1 =str(df[p][0])
    SMF1 =str(df[p][1])
    SMFvar1 = str(df[p][2])
    gene2 = str(df[p][3])
    SMF2 = str(df[p][4])
    SMFvar2 = str(df[p][5])
    DMF = str(df[p][6])
    num = str(df[p][7])
    umwat = str(df[p][8])
    outfile.write(p)
    outfile.write('\t')
    outfile.write(gene1)
    outfile.write('\t')
    outfile.write(SMF1)
    outfile.write('\t')
    outfile.write(SMFvar1)
    outfile.write('\t')
    outfile.write(gene2)
    outfile.write('\t')
    outfile.write(SMF2)
    outfile.write('\t')
    outfile.write(SMFvar2)
    outfile.write('\t')
    outfile.write(DMF)
    outfile.write('\t')
    outfile.write(num)
    outfile.write('\t')
    outfile.write(umwat)
    outfile.write('\n')

f.close()
outfile.close()

# maybe put the gene pair and DMF in a dictionary

# for each pair, write out a row that has :
# gene1 (the greater one),  avg SMF1, var SMF1, gene2, avg SMF2, var SMF2, average DMF between the pair
# ^^^ look up the SMF in the merged dictionary
