'''
making stdev cutoff matrix
 ** We decided that the variance of some of the single mutants generated in the 
    other clean_redundancy_matrix were kind of high. Our solution was this: 
    make another dataset that eliminates these genes with a standard deviation 
    greater than 10% of the mean (so only include rows where stdev < mean +/- 
    (0.1*mean))
11/16

'''

import sys 
import pandas as pd 
import numpy as np

# file is gonna be ~/PLB498/data/fitness_data/clean/clean_redundancy_matrix26.csv

f = pd.read_csv(sys.argv[1], header = 0)
temp = sys.argv[2]
f['stdev'] = np.sqrt(f['Variance'])
print(f.head())

frames = []
num_rows = f.shape[0]
for i in range(num_rows):
    if f['stdev'][i] < (f['SMF'][i] * 0.1):
        col = pd.DataFrame(f.iloc[i:])
        frames.append(col)
        
new_df = pd.concat(frames, axis = 0)
new_df.columns = ['gene', 'fitness', 'variance', 'stdev']
new_df = new_df.set_index('gene')
new_df.to_csv('../data/fitness_data/clean/stdev_cutoff_matrix_%s.csv' %temp)



