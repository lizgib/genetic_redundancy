'''
so we got some weird results for the first machine learning run.
there was a big clustered blob near fitness = 1 for the regression output

what I think is happening is that there are way to many genes that havve a fitness
close to one that the model is focusing too much on fitting to them and doesnt represnet
the variation in other fitness levels

this script makes 10 bins of fitness level ranges with the same number of genes in
them. want to see if having a more linear distribution of data

'''
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


f = open(sys.argv[1])
header = f.readline()
lines = f.readlines()


# bins dictionary

bins = {1: [], 0.9: [], 0.8: [], 0.7: [], 0.6: [], 0.5: [], 0.4: [], 0.3: [], 0.2: [], 0.1: [], 0.0: [], -1.0 : []}
for l in lines:
    ll = l.strip().split('\t')
    gene = ll[0]
    gr_calc = float(ll[1])
    if 10 >= gr_calc > 1: # getting a list of genes that fall into the redun score threshold
        bins[1].append(gene)
    if 0.9 > gr_calc > 0.8:
        bins[0.9].append(gene)
    if 0.8 > gr_calc > 0.7:
        bins[0.8].append(gene)
    if 0.7 > gr_calc > 0.6:
        bins[0.7].append(gene)
    if 0.6 > gr_calc > 0.5:
        bins[0.6].append(gene)
    if 0.5 > gr_calc > 0.4:
        bins[0.5].append(gene)
    if 0.4 > gr_calc > 0.3:
        bins[0.4].append(gene)
    if 0.3 > gr_calc > 0.2:
        bins[0.3].append(gene)
    if 0.2 > gr_calc > 0.1:  # this one covers a greater range because there are less than 50 genes in each group
        bins[0.2].append(gene)
    if 0.1 > gr_calc > 0.05:
        bins[0.1].append(gene)
    if 0.05 > gr_calc > -0.05:
        bins[0.0].append(gene)
    if -0.05 > gr_calc >= -10:
        bins[-1.0].append(gene)
f.close()

grab_genes = []
for k in bins.keys():
    chosen_ones = np.random.choice(bins[k], 50)
    grab_genes.extend(chosen_ones)

df = pd.read_csv(sys.argv[1], sep = '\t')
newdf = df.loc[grab_genes]
newdf.to_csv('redistributed_feature_table.tab', sep = '\t')

#
#
# print(len(newdf))
# print(len(original))
# original = pd.DataFrame.from_dict(original, orient = 'index')
# newdf = pd.DataFrame.from_dict(newdf, orient = 'index')
#

#
# fit1 = original.iloc[:,0]
# fit2 = newdf.iloc[:,0]
#
# plt1 = fit1.hist(bins = 10)
# plt1.set_xlabel('Fitness')
# plt1.set_ylabel('Number of Genes')
# plt1.set_title('Fitness Distribution')
# fig1 = plt1.get_figure()
# fig1.savefig('originalhistforclass.png')
# plt2 = fit2.hist(bins = 10)
# plt2.set_xlabel('Fitness')
# plt2.set_ylabel('Number of Genes')
# plt2.set_title('Fitness Distribution')
# fig2 = plt2.get_figure()
# fig1.savefig('newhistforclass.png')

# newdf.to_csv('../data/even_genes.tsv', sep = '\t')
