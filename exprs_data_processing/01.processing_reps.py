'''
 this script needs to take input of what a replicate looks like in a dataset
 and then average between each replicate appropriately
2/15/19
'''

import os
import pandas as pd
import string
import sys

directory = sys.argv[1]
os.chdir('raw/SGD_clean_headers/%s' %directory)
df = pd.read_csv(sys.argv[2], index_col = 0, sep = '\t')
rep_naming = sys.argv[3]

header_list = list(df.columns.values)

frames = []
averages = []
prev_tret = header_list[2] # start off with first column

def get_average(cols, clist, treatment):
    newdf = pd.concat(cols, axis = 1)# take average of the frames
#    print('how many columns?', newdf.shape[1])
#    print('which cols?', clist)
    colname = 'avg %s' % treatment
#    print(colname)
    newdf[colname] = newdf.mean(axis=1)
    return newdf[colname]

clst = []
for c in header_list[2:]:
    repID = c[c.find('%s' %rep_naming):]
    treatment = c[:c.find('%s' %rep_naming)]
    if c == header_list[-1]: # this is so ugly but idc it works
        col = pd.DataFrame(df[c]) # grab that column and add it to the frames (to be averaged)
        clst.append(c)
        averages.append(col)
        frames.append(get_average(averages, clst, treatment))
        averages = []
        clst = []
    elif treatment == prev_tret:  # if the we are still on the same treatment
        col = pd.DataFrame(df[c]) # grab that column and add it to the frames (to be averaged)
        clst.append(c)
        averages.append(col)
    else:
        if averages != []:
            frames.append(get_average(averages, clst, prev_tret))
            averages = []
            clst = []
        col = pd.DataFrame(df[c]) # grab that column and add it to the frames (to be averaged)
        clst.append(c)
        averages.append(col)
        prev_tret = treatment

newdf = pd.concat(frames, axis = 1)
print(newdf)
outfile = sys.argv[2] + '_clean'
try:
    os.makedirs('../../../data/replicates_processed/%s' %directory)
    print('made the new directory')
    newdf.to_csv('../../../data/replicates_processed/%s/%s' %(directory, outfile), sep = '\t')
    print('saved the file')
except FileExistsError:
    print('that directory has already been made')
    newdf.to_csv('../../../data/replicates_processed/%s/%s' %(directory, outfile), sep = '\t')
