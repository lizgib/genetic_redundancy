'''
dont think im using this anymore as of 04-01-2019

normalize the datasets
INPUTS:
    combined_data.csv
OUTPUTS:
    normalized_exp_dat.csv
    optional : combined_dat_boxplt.png
               normalized_boxplt.png
LAST EDITED: 10/12
'''

#########################
# QUANTILE NORMALIZATION
#########################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys, os, traceback
import sklearn.preprocessing


combined_data_1 = open('data/SGD_yeast_expression_dat.02-21-2019.NAremove.tab')
header = combined_data_1.readline()
file = combined_data_1.readlines()
new_dat = []
print('The file has been read in at least')
for line in file:
    linelist = line.strip().split('\t')
    genename = linelist[0]
    restoffile = linelist[1:]
    new_dat.append(restoffile)

combined_data = pd.DataFrame(new_dat)
print('combined dataset has been put into pandas dataframe')


try:
    combined_data = combined_data.astype('float')
    print('the stupid astype thing worked for the pandas dataframe')
except ValueError:
    print('noooooo')
# SAVED ON 10/12
#fig1 = plt.figure(1, figsize= (20,8))
#combined_data.boxplot()
#fig1.savefig('outputs/combined_dat_boxplt.png')

 #SOURCE FOR THIS FUNCTION : https://github.com/ShawnLYU/Quantile_Normalize

def quantileNormalize(df_input):
    cols_normalized = 0
    df = df_input.copy()
    #compute rank
    dic = {}
    for col in df:
        dic.update({col : sorted(df[col])})
    sorted_df = pd.DataFrame(dic)
    rank = sorted_df.mean(axis = 1).tolist()
    #sort
    for col in df:
        t = np.searchsorted(np.sort(df[col]), df[col])
        df[col] = [rank[i] for i in t]
        cols_normalized += 1
        if cols_normalized in [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]:
            	print(cols_normalized)
    return df

normalized = quantileNormalize(combined_data)
date = datetime.datetime.today().strftime('%d-%m-%Y')
outfile = 'SGD_yeast_expression_dat_norm_' + date

#get NAs in np format
normalized = normalized.replace("?",np.nan)
normalized = normalized.replace("NA",np.nan)
normalized = normalized.replace("",np.nan)

normalized.to_csv(outfile, sep = '\t')


# SAVED ON 10/12
#fig2 = plt.figure(2, figsize= (20,8))
#normalized.boxplot()
#fig2.savefig('outputs/normalized_boxplt.png')


## 10/12 2:19 PM This looks like the data has been normalized... I saved some boxplots
## of the input (not normalized) and then how it looked when it was normalized
## they are in the outputs folder... I will show siobhan or dr. shiu at our
## meeting to make sure they look ok but to me they look "normalized"
