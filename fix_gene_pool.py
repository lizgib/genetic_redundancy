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


f = open(sys.argv[1])

lines = f.readlines()


# bins dictionary
original = {}
bins = {0.9: [], 0.8: [], 0.7: [], 0.6: [], 0.5: [], 0.4: [], 0.3: [], 0.2: [], 0.1: [], 0.0: []}
for l in lines:
    ll = l.strip().split(',')
    gene = ll[0]
    try:
        fitness = float(ll[1])
    except:
        pass
    if gene not in original.keys():
        original[gene] = []
    original[gene].append(fitness)
    original[gene].append(ll[2])
    if 1.0 > fitness > 0.9:
        bins[0.9].append(gene)
    if 0.9 > fitness > 0.8: 
        bins[0.8].append(gene)
    if 0.8 > fitness > 0.7: 
        bins[0.7].append(gene)
    if 0.7 > fitness > 0.6: 
        bins[0.6].append(gene)
    if 0.6 > fitness > 0.5:
        bins[0.5].append(gene)
    if 0.5 > fitness > 0.4:
        bins[0.4].append(gene)
    if 0.4 > fitness > 0.3:
        bins[0.3].append(gene)
    if 0.3 > fitness > 0.2:
        bins[0.2].append(gene)
    if 0.2 > fitness > 0.0:  # this one covers a greater range because there are less than 50 genes in each group
        bins[0.1].append(gene)


print(len(bins[0.9]))
print(len(bins[0.8]))
print(len(bins[0.7]))
print(len(bins[0.6]))
print(len(bins[0.5]))
print(len(bins[0.4]))
print(len(bins[0.3]))
print(len(bins[0.2]))
print(len(bins[0.1]))

gene_nums = [len(bins[0.9]), len(bins[0.8]), len(bins[0.7]), len(bins[0.6]), len(bins[0.5]), len(bins[0.4]), len(bins[0.3]), len(bins[0.2]), len(bins[0.1])]

newdf = {}
for k in bins.keys():    
    for v in bins[k][:50]:
        if v not in newdf.keys():
            newdf[v] = []
        newdf[v] = original[v]
        
        
print(len(newdf))
print(len(original))
original = pd.DataFrame.from_dict(original, orient = 'index')       
newdf = pd.DataFrame.from_dict(newdf, orient = 'index')



fit1 = original.iloc[:,0]
fit2 = newdf.iloc[:,0]

plt1 = fit1.hist(bins = 10)
plt1.set_xlabel('Fitness')
plt1.set_ylabel('Number of Genes')
plt1.set_title('Fitness Distribution')
fig1 = plt1.get_figure()
fig1.savefig('originalhistforclass.png')
plt2 = fit2.hist(bins = 10)
plt2.set_xlabel('Fitness')
plt2.set_ylabel('Number of Genes')
plt2.set_title('Fitness Distribution')
fig2 = plt2.get_figure()
fig1.savefig('newhistforclass.png')

newdf.to_csv('../data/even_genes.tsv', sep = '\t')

