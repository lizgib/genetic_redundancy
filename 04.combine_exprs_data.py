'''
This script will be replacing the 04.get_all_exprs_data.py script I wrote last semester
Instead of using the SGD data, I will be running my analyses using a manually curated dataset from
M3D (Many Microbe Microarray Database)
Using this script will address some of the problems I had with combining the SGD data.
The data is currently in 3 dataframes (5520, 6954, 8119)
This script will:
    1. concatenate the three dataframes together
    2. check to make sure there are no duplicate columns (think there are only 248 conditions)
    3. drop rows (genes) that are not present in the fitness dataset

1/14/19
'''

import pandas as pd

g5520 = pd.read_csv('../Yeast_Genome_S98_v2_norm/avg_Yeast_Genome_S98_v2_exps247probes5520.tab', sep = '\t', index_col = 0)
g6954 = pd.read_csv('../Yeast_Genome_S98_v2_norm/avg_Yeast_Genome_S98_v2_exps247probes6954.tab', sep = '\t', index_col = 0)
g8119 = pd.read_csv('../Yeast_Genome_S98_v2_norm/avg_Yeast_Genome_S98_v2_exps247probes8119.tab', sep = '\t', index_col = 0)

print(list(g5520))



