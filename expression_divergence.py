'''
expression divergence
10/19/18

looks at each gene pair and determines what the level of expression difference is 
by calculating the PCC between every condition in the dataset betweent the two 
genes in the pair 
'''

# okeee,  so we have the problem of genes having unequal numbers of expression datasets 
# associated with them. Going to fix this by randomly selecting a subset of the expression 
# data for the genes that have more values than other genes and iterating multiple times
# then from that look at the different PCCs generated to come up with value 


from scipy import stats
import sys
import numpy as np

'''
read in the data 
'''

dat = open(sys.argv[1]) # this should be an expression data matrix 
#dat = open('/Users/elizabethgibbons/Documents/FS18/PLB498/table2.tsv')
header = dat.readline()
lines = dat.readlines()


exprs_data = {}
for l in lines: 
    ll = l.strip().split('\t')
    gene = ll[0]
    exprs = ll[1:]
    if gene not in exprs_data.keys():
        exprs_data[gene] = []
    for i in exprs: 
        try:
            num = float(i)
        except: # apparently there are a lot of NAs in this dataset that I can't work w :( passing them for now
            pass
        exprs_data[gene].append(num)
    try:
        np.array(exprs_data[gene]).astype(np.float)
    except: 
        print(exprs_data[gene])

print(len(exprs_data))
remove_these = []
for g in exprs_data.keys():
    if len(exprs_data[g]) < 227: 
        remove_these.append(g)

for g in remove_these: # this gets rid of any genes that didn't have any expression data in them 
    exprs_data.pop(g, None)
print(len(exprs_data))



'''
functions 
'''

def expression_divergence(gene1, gene2):
    PCC = stats.pearsonr(gene1, gene2)
    exp_div = 1 - PCC[0]
    return exp_div



'''
calculate expression divergence 
'''
    
# go through each gene in the dataset
exprs_div_dict = {}
num_bois = 0

outfile = open('../data/myprecious2.txt', 'w')
for i in exprs_data.keys(): 
    for j in exprs_data.keys(): 
        minlen = min([len(exprs_data[i]), len(exprs_data[j])])
       # ed = stats.pearsonr(exprs_data[i], exprs_data[j])  # these need to be the same length ughhhh
        ed = expression_divergence(exprs_data[i],exprs_data[j])
    pair = i + '_' + j
    exprs_div_dict[pair] = ed
    num_bois += 1
    outfile.write(i + '_' + j)
    outfile.write('\t')
    outfile.write(str(ed))
    outfile.write('\n')

print(num_bois)
dat.close()
outfile.close()

# calculate its expression divergence against every other gene 

#### What about things that potentially are in bigger groups than pairs?? 
######## for example a group of 3 genes that are redundant of each other? this is limited

# plot/compare the level of expression divergence to the redundancy data 
## how well correlated are they (highly redundnat == low expression divergence?)




