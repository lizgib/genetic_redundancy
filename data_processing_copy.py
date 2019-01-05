

import csv
import os
import pandas as pd
import numpy as np

# from gene list file read in a list of all the gene names 
gene_file = open('data/yeast_gene_list.csv')
stress_dataset = np.genfromtxt('data/stress_dataset.txt', unpack = True, usecols = (0), dtype = 'str')
transcription_dataset = np.genfromtxt('data/transcription_dataset.txt', unpack = True, usecols = (0), dtype = 'str')
grw_meta_dataset = np.genfromtxt('data/growth_metabolism_dataset.txt', unpack = True, usecols = (0), dtype = 'str')

head = gene_file.readline()
gene_list = set()
dat_dict = {}
dat_dict['gene'] = []
for line in gene_file.readlines():
    num_gene = line.strip().split(',')
    noquote_gene = num_gene[1].strip('"')
    gene_list.add(noquote_gene)
    dat_dict[noquote_gene] = []

os.chdir('data')

dataset = grw_meta_dataset
dataset_name = 'growth_metabolism_matrix'

directories_included = []
for directory in os.listdir(os.getcwd()):
    if directory[-8:] in dataset:
        directories_included.append(directory)
        for pcl in os.listdir(directory):
            filename = (('%s/%s') %(directory, pcl))
            try:
                f = open(filename, encoding = 'utf-8', errors = 'ignore')
                print('accesses pcl files!!')
            except FileNotFoundError:
                print('AHHHH cant find file!', pcl)
            header = f.readline()
            header = header.strip().split('\t')
        

#==============================================================================
#         for x in header: 
#             if x.lower().find('replicate') != -1: 
#                 print(directory, 'col:', header.index(x))
#             elif x.lower().find('rep') != -1:
#                 print(directory, 'col:', header.index(x))
#==============================================================================
            
                
            for c in range(len(header)): 
                header[c] = directory + '_' + header[c] 
            dat_dict['gene'] = dat_dict['gene'] + (header[3:])
            line2 = f.readline()
            lines = f.readlines()
            num_conditions = len(header[3:])
            
            genedict = {}
            for line in lines:
                linelist = line.strip().split('\t')
                gene = linelist[0]
                genedict[gene] = linelist[3:]          
            
            # this is likely.. the genes used in the study don't look at all the genome
            # fill these empty genes with NAs for now
            empty = ['NA'] * num_conditions
            
            #find the genes that weren't represented in the expression set
            missing_genes = dat_dict.keys() - genedict.keys()
        
            #fill the rows where these genes are with 0s 
            for g in missing_genes:
                if g != 'gene':
                    genedict[g] = empty
            
            # then add the dict for the particular dataset to the bigger one (which will be all
            # datasets put together)
            for k in genedict.keys():
                if k in dat_dict.keys():
                    dat_dict[k] = (dat_dict[k] + genedict[k])



pd.DataFrame.from_dict(data=dat_dict, orient='index').to_csv(('../data/%s.csv' %dataset_name), header=False)





