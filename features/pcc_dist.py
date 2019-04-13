'''
export PATH=/mnt/home/azodichr/miniconda3/bin:$PATH
### should ssh dev-intel16-k80
'''
import os,sys
import pandas as pd
import numpy as np
import random
from scipy.stats.stats import pearsonr
from scipy import stats
import matplotlib.pyplot as plt
#from scipy.stats import chisqprob <- wont import this for me on hpc

file = sys.argv[1]
SAVE = 'outputs/distance/PCC_dist_mat'
df = pd.read_csv('data/'+file, sep='\t', index_col = 0, header = 0)
pcc = df.T.corr(method='pearson').round(3)
pcc_dist = 1 - pcc
pcc_dist.to_csv(SAVE, index=True, header=True,sep="\t")