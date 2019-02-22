'''
Takes in a list of directories and cleans the column headers
of each file in each directory. Returns the dataframe with the
new, clean column names

2/15/19
'''

import sys
import pandas as pd
import os

def clean_dat_boi(df):
    header_list = list(df.columns.values)
    clean_header = []
    for c in header_list[2:]:
        c = c.lower()
        c  = c.replace(" ", "")
        c = c.replace('_', '') # just covering my ass on this one
        repID = c.find('rep')
        clean_header.append(c)
    clean_header.insert(0, 'NAME')
    clean_header.insert(1, 'GWEIGHT')
    df.columns = clean_header
    return df


with open('pubmedIDS.txt') as f:
    pubmedIDS = f.read().splitlines()

os.chdir('raw/SGD_exprs_data')

files_cleaned = 0
for directory in os.listdir(os.getcwd()):
    for ID in pubmedIDS:
        if ID in directory:
            for pcl in os.listdir(directory):
                filename = (('%s/%s') %(directory, pcl))
                try:
                    df = pd.read_csv(filename, sep = '\t', index_col = 0, skiprows = [1])
                    print('accesses pcl files!!')
                    clean_dat_boi(df)
                    print('dat boi been cleaned')
                    files_cleaned += 1
                    try:
                        os.makedirs('../SGD_clean_headers/%s' %directory)
                        df.to_csv('../SGD_clean_headers/%s/%s' %(directory, pcl), sep = '\t')
                    except FileExistsError:
                        df.to_csv('../SGD_clean_headers/%s/%s' %(directory, pcl), sep = '\t')
                    print('he has been saved')
                except FileNotFoundError:
                    print('AHHHH cant find file!', pcl)
