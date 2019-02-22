'''
this script is gonna be a combination of data_processing and combine_datasets
    1. first we're gonna read in the genes list and make that the keys for the dictionary
    2. next we're gonna read in every expression file in the raw_data folder
    3. for each expression file, we're gonna add the expression levels to each key in our
       gene dictionary (so be iterating through the keys first). if a dataset doesn't have a value
       for a particular gene, put an NA there instead
       *in this dictionary theres gonna be a key for the colnames called 'gene'
        we will put the experiment names in these
    4. once we have gone through every file, write this dictionary to a file

LETS GO !
11/8/18 8:55 PM

'''


import csv
import os
import pandas as pd
import numpy as np
import re
import datetime

dat_dict = {} # this will be the dictionary everything goes into
dat_dict['gene'] = [] # this is for the header. gonna be experiment_conditions names

# from gene list file read in a list of all the gene names
gene_names = pd.read_csv('data/yeast_gene_list.csv', usecols = [1])
for g in gene_names['x']:
    dat_dict[g] = []
print(gene_names['x'])

os.chdir('data/replicates_processed')


directories_included = []
for directory in os.listdir(os.getcwd()):
    directories_included.append(directory)
    for pcl in os.listdir(directory):
        filename = (('%s/%s') %(directory, pcl))
        try:
            #f = open(filename, encoding = 'utf-8', errors = 'ignore)
            f = open(filename)
            print('accesses pcl files!!')
        except FileNotFoundError:
            print('AHHHH cant find file!', pcl)
        header = f.readline()
        header = header.strip().split('\t') # so this gives me the number of experiments/individual conditions within a pcl file

        for c in range(len(header)):  # for each condition in each directory
            header[c] = directory + '_' + header[c] # I want to keep track of the conditions based on their experiment name (for README later)
            #header[c] = directory + '_' + c
            header[c] = re.sub('\W', '_', header[c])

        dat_dict['gene'] = dat_dict['gene'] + (header[3:]) # skipping the first 3 cols of each pcl because are all redundant (YORF, NAME, GWEIGHT)

        pcl_content = f.readlines()
        num_conditions = len(header[3:])

        genedict = {}
        for line in pcl_content:
                linelist = line.strip().split('\t')
                gene = linelist[0]
                # adding this bit 12/1
                content = []
                for i in linelist[3:]:
                    content.append(i)
                    # the stuff here was only filling Nas... not sure why but trying to just get rid of this for now
                    # if i.isnumeric():
                    #     content.append(i)
                    # else:
                    #     i = 'NA'
                    #     content.append(i)

                genedict[gene] = content

        # this is likely.. the genes used in the study don't look at all the genome
        # fill these empty genes with NAs for now
        empty = ['NA'] * num_conditions

        #find the genes that weren't represented in the expression set
        missing_genes = dat_dict.keys() - genedict.keys()
        #fill the rows where these genes are with NAs
        for g in missing_genes:
            if g != 'gene':
                genedict[g] = empty

        # then add the dict for the particular dataset to the bigger one (which will be all
        # datasets put together)
        for k in genedict.keys():
            if k in dat_dict.keys():
                dat_dict[k] = (dat_dict[k] + genedict[k])

d = datetime.datetime.today()
date = d.strftime('%m-%d-%Y')
pd.DataFrame.from_dict(data=dat_dict, orient='index').to_csv(('../../data/SGD_yeast_expression_dat.%s.tab' %date), header=False, sep = '\t')
